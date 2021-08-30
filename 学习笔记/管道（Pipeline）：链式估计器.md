#管道（Pipeline）：链式估计器

[`Pipeline`](https://scikit-learn.org.cn/view/716.html)可用于将多个估计器链接为一个。这很有用，因为在处理数据时通常会有固定的步骤顺序，例如特征选择，归一化和分类。[`Pipeline`](https://scikit-learn.org.cn/view/716.html)在这里有多种用途：

- 便捷和封装

  只需要对数据集调用一次[fit](https://scikit-learn.org.cn/lists/91.html#方法)和[predict](https://scikit-learn.org.cn/lists/91.html#方法)，就可以适配一系列评估器。

- 联合参数选择

  您可以对管道中估计器的所有参数进行一次[网格搜索](https://scikit-learn.org.cn/view/99.html)。

- 安全

  转换器（ transformers）和预测器（predictors）使用相同的样本训练，管道有助于避免将统计数据从测试数据泄漏到经过交叉验证训练的模型中。

除最后一个管道外，管道中的所有估计器都必须是转换器（即必须具有[转换（transform）](https://scikit-learn.org.cn/lists/91.html#方法)方法）。最后的估计器可以是任何类型（转换器，分类器等）。

## 构造

管道是由包含（键，值）对的列表构建的，其中键是包含此步骤名称的字符串，而值是估计器对象

```python
estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

功能函数[`make_pipeline`](https://scikit-learn.org.cn/view/717.html)是构造管道的简写。它使用可变数量的估计器并返回管道，而且自动填充名称：
```python
>>> make_pipeline(Binarizer(), MultinomialNB())
Pipeline(steps=[('binarizer', Binarizer()), ('multinomialnb', MultinomialNB())])
```

## 访问

管道的估计器在`steps`属性中以列表形式存储，但是可以对管道建立索引并通过索引或名称（通过`[idx]`）来访问管道：

```python
>>> pipe.steps[0]
('reduce_dim', PCA())
>>> pipe[0]
PCA()
>>> pipe['reduce_dim']
PCA()
```



## 方法

- 假设该Pipline共有n个学习器

- transform,依次执行各个学习器的transform方法

- fit,依次对前n-1个学习器执行fit和transform方法,第n个学习器(最后一个学习器)执行fit方法

- predict,执行第n个学习器的predict方法

- score,执行第n个学习器的score方法

- set_params,设置第n个学习器的参数

- get_param,获取第n个学习器的参数

### fit、transform、fit_transform的区别
- fit：拟合，得到相关方法的参数
- transform：转换，使用方法将X转换
- fit_transform：先拟合后转换

  

## 例子

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline([('sc', StandardScaler()),
                    ('pca', PCA(n_components=2)),
                    ('clf', LogisticRegression(random_state=1))
                    ])
pipe_lr.fit(X_train, y_train)
pipe_lr.score(X_test, y_test)
```

