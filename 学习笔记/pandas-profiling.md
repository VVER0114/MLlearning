# pandas-profiling

pandas数据描述工具

## 应用

```python
from pandas_profiling import ProfileReport
profile = ProfileReport(df, title = "Pandas Profiling Report")
```

## 导入

```python
#生成jupyter报告
profile.to_widgets()

#生成HTML报告
profile.to_notebook_iframe()
```

## 保存

```python
profile.to_file("your_report.html")
profile.to_file("your_report.json")
```



[报告例子](file://C:/Users/Water/Documents/Python/jupyter/your_report.html)









