# pandas绘图

## 安德鲁斯曲线Andrews curves

**pandas.plotting.andrews_curves**

安德鲁斯曲线允许将多变量数据绘制为使用样本属性创建的大量曲线作为傅立叶级数的系数。

通过绘制每个类别的这些曲线，可以可视化数据集群。 属于同一类样品的曲线通常会更靠近在一起并形成较大的结构。

其中x系数对应于每个维度的值，t在-pi和+pi之间线性间隔。那么，每一行的框架都对应于一条曲线。

```python
df = pd.read_csv(
    'https://raw.github.com/pandas-dev/'
    'pandas/master/pandas/tests/io/data/csv/iris.csv'
)
pd.plotting.andrews_curves(df, 'Name')
```

![](https://pandas.pydata.org/pandas-docs/stable/_images/pandas-plotting-andrews_curves-1.png)

## Bootstrap plot 

**pandas.plotting.bootstrap_plot**

用booststrap的方法画出不确定数据的平均值，中位数，中点值（（最大+最小）/2）

用于视觉评估统计量的不确定性

```python
s = pd.Series(np.random.uniform(size=100))
pd.plotting.bootstrap_plot(s)
```

![](https://pandas.pydata.org/pandas-docs/stable/_images/pandas-plotting-bootstrap_plot-1.png)

## 滞后图Lag plots

**pandas.plotting.lag_plot**

滞后图用于检查数据集
1. **模型适用性**。
2. [**异常值**](https://www.statisticshowto.com/statistics-basics/find-outliers/)（具有极高或极低值的数据点）。
3. **随机性**（没有模式的数据）。
4. [**序列相关/自相关**](https://www.statisticshowto.com/serial-correlation-autocorrelation/)（时间序列中的误差项从一个时期转移到另一个时期）。
5. [**季节性**](https://www.statisticshowto.com/timeplot/#seasonality)（定期发生的时间序列数据的周期性波动）。

```python
from pandas.plotting import lag_plot
plt.figure()
data = pd.Series(0.1 * np.random.rand(1000) +
0.9 * np.sin(np.linspace(-99 * np.pi, 99 * np.pi, num=1000)))
lag_plot(data
```

![](https://pic1.zhimg.com/80/v2-e9e53ab371ac1e796d0b914af2df2cfc_720w.jpg)

## 平行坐标parallel coordinates

**pandas.plotting.parallel_coordinates**

平行坐标是绘制多变量数据的绘图技术。 它允许人们看到数据中的聚类，并可视觉地估计其他统计信息。

使用平行坐标点表示为连接的线段。 每个垂直线代表一个属性。 一组连接的线段表示一个数据点。 趋向于集群的点将会更接近

```python
df = pd.read_csv('https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/iris.csv')
>>> pd.plotting.parallel_coordinates( df, 'Name', color=('#556270', '#4ECDC4', '#C7F464'))
```

![平行坐标](https://pandas.pydata.org/pandas-docs/stable/_images/pandas-plotting-parallel_coordinates-1.png)

## 散点矩阵scatter matrix

**pandas.plotting.scatter_matrix**

```python
from pandas.plotting import scatter_matrix
df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
```



![](https://pic2.zhimg.com/80/v2-d67681c87ca5fbc920d2530a840007a1_720w.jpg)

## 密度图

使用Series.plot.kde（）和DataFrame.plot.kde（）方法创建密度图

```python
ser = pd.Series(np.random.randn(1000))
ser.plot.kde()
```

![](https://pic1.zhimg.com/80/v2-12bced8bfbe62e70806169db763c2acc_720w.jpg)

