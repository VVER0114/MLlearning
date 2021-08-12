# dbf导入——simpledbf

## 导入dbf文件

```python
from simpledbf import Dbf5
dbf = Dbf5('fileName.dbf', codec='utf-8')
```

## 文件转换

- 1. 转csv
     ```python
     dbf.to_csv('filename.csv')
     ```

- 2. 转DataFrame
     ```python
     df = dbf.to_dataframe()
     ```
