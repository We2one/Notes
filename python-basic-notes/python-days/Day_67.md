### Pandas

#### Pandas 简介

+ Pandas (Panel data & data analysis), 是基于 Numpy 的专用于数据分析的工具

+ Pandas 的主要数据结构是 **Series**（带标签的一维同构数组）与 **DataFrame**（带标签的，大小可变的，二维异构表格）
+ [Pandas 官档](https://www.pypandas.cn/docs/getting_started/dsintro.html#dataframe)

#### Pandas 优势

+ Pandas 适用于处理以下类型的数据：
  + 与 SQL 或 Excel 表类似的，含异构列的表格数据;
  + 有序和无序（非固定频率）的时间序列数据;
  + 带行列标签的矩阵数据，包括同构或异构型数据;
  +  任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。
+ Pandas 优势
  1. 处理浮点与非浮点数据里的缺失数据，表示为 NaN；
  2. 大小可变：插入或删除 DataFrame 等多维对象的列；
  3. 自动、显式数据对齐：显式地将对象与一组标签对齐，也可以忽略标签，在 Series、DataFrame 计算时自动与数据对齐；
  4. 强大、灵活的分组（group by）功能：拆分-应用-组合数据集，聚合、转换数据；
  5.  把 Python 和 NumPy 数据结构里不规则、不同索引的数据轻松地转换为 DataFrame 对象；
  6. 基于智能标签，对大型数据集进行切片、花式索引、子集分解等操作；
  7. 直观地合并（merge）、**连接（join）**数据集；
  8.  灵活地重塑（reshape）、**透视（pivot）**数据集；
  9. 轴支持结构化标签：一个刻度支持多个标签；
  10.  成熟的 IO 工具：读取文本文件（CSV 等支持分隔符的文件）、Excel 文件、数据库等来源的数据，利用超快的 HDF5 格式保存 / 加载数据；
  11.  时间序列：支持日期范围生成、频率转换、移动窗口统计、移动窗口线性回归、日期位移等时间序列功能。

#### 主要数据结构

1. Series 是**带标签的一维数组**，可存储整数、浮点数、字符串、Python 对象等类型的数据。轴标签统称为索引。

   + 创建 : `pd.Series(self, data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)`

   + data 参数 支持以下数据类型

     1. **Python 字典** : `pd.Series({'b': 1, 'a': 0, 'c': 2})`
     2. **多维数组**  : data 是多维数组时，index 长度必须与 data 长度一致。没有指定 index 参数时，创建数值型索引，即 [0, ..., len(data) - 1]。
     3. **标量值（如，5）**  : data 是标量值时，必须提供索引。Series 按索引长度重复该标量值。

   + Series 属性

     ```python
     import pandas as pd
     import numpy as np
     
     index = ["stu0", "stu1", "stu2", "stu3"]
     value = [
     	["张三", 13, 1],
     	["李四", 32, 2],
     	["王五", 23, 1],
     	["小二", 12, 1],
     ]
     se = pd.Series(index=index, data=value)
     print(se)
     print(se.ndim)  # 1
     print(se.dtype)  # object
     print(se.shape)  # (4,)
     print(se.index)  # Index(['stu0', 'stu1', 'stu2', 'stu3'], dtype='object')
     print(se.values)  # [list(['张三', 13, 1]) list(['李四', 32, 2]) list(['王五', 23, 1]) list(['小二', 12, 1])]
     ```

     

2. DataFrame 是由**多种类型的列构成的二维标签数据结构**，类似于 Excel 、SQL 表，或 Series 对象构成的字典。DataFrame 是最常用的 Pandas 对象，与 Series 一样，

   + `pd.DataFrame(self, data=None, index: Optional[Axes] = None, columns: Optional[Axes] = None, dtype: Optional[Dtype] = None, copy: bool = False,)`

     + 参数

       | 参数        | 描述             |
       | ----------- | ---------------- |
       | **data**    | 数据             |
       | **index**   | 行索引           |
       | **columns** | 列索引           |
       | **copy**    | 是否允许生成副本 |

   + DataFrame 支持多种类型的输入

     1. 一维 ndarray、列表、字典、Series 字典
     2. 二维 numpy.ndarray
     3. 结构多维数组或记录多维数组
        1. Series
        2. DataFrame

   + 创建方式

     1. 逐个传入行列与数据信息

        ```python
        import pandas as pd
        
        # 创建 DataFrame
        # 一、逐个传入行索引、列索引、数据部分
        # 行索引
        index = ["stu0", "stu1", "stu2", "stu3"]
        # 列索引
        columns = ["name", "age", "group"]
        
        # 数据部分
        value = [
        	["张三", 13, 1],
        	["李四", 32, 2],
        	["王五", 23, 1],
        	["小二", 12, 1],
        ]
        
        df = pd.DataFrame(data=value, index=index, columns=columns)
        """
             name  age  group
        stu0   张三   13      1
        stu1   李四   32      2
        stu2   王五   23      1
        stu3   小二   12      1
        """
        ```

     2. 字典形式传入数据 (以列名称作为字典的 key, 每一列的值作为字典的 values)

        ```python
        import pandas as pd
        
        # 创建 DataFrame
        
        # 二、字典形式传入数据
        index = ["stu0", "stu1", "stu2", "stu3"]
        dict1 = {
        	"name": ["张三", "李四", "王五", "小二",],
        	"age": [12, 21, 32, 32],
        	"group": [1, 2, 1, 1],
        }
        df1 = pd.DataFrame(dict1, index=index)
        print(df1)
        """
             name  age  group
        stu0   张三   12      1
        stu1   李四   21      2
        stu2   王五   32      1
        stu3   小二   32      1
        """
        ```

   + 属性

     + **shape** : 行列数
     + **ndim** : 维度
     + **size** : 大小 (内部数据数目)
     + **dtypes** : DataFrame 内属性类型, 以列数返回,多种类型的话向上选取数据类型，字符串返回为 object 而非 string
     + **values** : 数据部分
     + **index** : 行索引
     + **columns** : 列索引

   + 修改索引

     1. 修改整个行索引 : `df.columns = 新的行索引`
     2. 修改列部分索引名称 : `df.rename(columns={"旧名称1": "新名称1", "旧名称2": "新名称2"}, inplace=True)`
     3. 修改行部分索引名称 : `df.rename(index={"旧名称1": "新名称1", "旧名称2": "新名称2"}, inplace=True)`

#### Pandas 读写数据

+ Pandas 读取到的文件会保存为 DataFrame 数据.
+ Pandas 一般读取 csv、txt、excel 文件(.xlsx 与 .xls)

##### 文本文件读取

+ 读取方式常为 `pd.read_文件格式()`

+ 参数

  | 参数                            | 描述                                                         |
  | ------------------------------- | ------------------------------------------------------------ |
  | **filepath_or_buffer**          | FilePathOrBuffer : 文件路径及文件名 或者缓存                 |
  | **sep=","**、**delimiter=None** | 分隔符 delimiter 与 sep 同时只可以出现一个                   |
  | **encoding**                    | 编码方式                                                     |
  | **header="infer"**              | 自动识别列索引,也可以将值设为列索引的指定行 **header="2"**   |
  | **index_col=None**              | 选择某一列作为行索引                                         |
  | **nrows=None**                  | 取出行数,默认取出所有                                        |
  | **usecols=None**                | 需要选择哪些列，默认None<br>&emsp;1. **None** 读取所有列<br>&emsp;2. **int** 读取第几列<br>&emsp;3. **list** int 列表 读取这个列表中对应的列<br>&emsp;4. **string** excel的方式读取，例如："A:F"表示A到F列，"A,D,E:H"表示A和D和E到H列 |
  | **names=None**                  | 对读取的列重命名,也可以读取数据之后再重命名                  |
  | **sheet_name=0**                | 读Excel的时候读取指定名称的表单，也可以是索引，默认0         |
  | **skiprows=None**               | 跳过哪些行                                                   |
  | **keep_default_na**             | 是否保留空值，默认True                                       |
  | **dtype**                       | 设置列的类型，例如，{‘a’: np.float64, ‘b’: np.int32}         |

##### 写入文本文件

+ 写入方式 : `DF_name.to_保存类型()`

+ 参数

  | 参数                                               | 描述                                                         |
  | -------------------------------------------------- | ------------------------------------------------------------ |
  | **path_or_buf: Optional[FilePathOrBuffer] = None** | 保存文件路径和文件名                                         |
  | **sep: str = ","**                                 | 分隔符                                                       |
  | **float_format: Optional[str] = None**             | 写浮点数的格式，’%.0f’                                       |
  | **header: Union[bool_t, List[str]] = True**        | 是否输出表头 (将列索引保存到文档中)，默认True                |
  | **index: bool_t = True**                           | 是否输出索引 (将行索引保存到文档中)，默认True                |
  | **columns: Optional[Sequence[Label]] = None**      | 列名称,可以是列表形式,表示存储的列                           |
  | **mode: str = "w"**                                | 设置写入模式，默认"w"                                        |
  | **sheet_name**                                     | **Excel专有**,表单名称，默认"Sheet1"<br>&emsp;可以指定为 **int** 代表分表的序号，从 0 (代表第一个表) 开始<br>&emsp;也可以指定为分表的名称 |

+ 特殊情况 : 写入excel 文件

  + 将不同的 dataframe 保存到同一个 excel 的不同 sheet 中去
  + 在 同一个 sheet 中添加数据

  + 实例

    ```python
    import numpy as np
    import pandas as pd
    
    index = ["stu0", "stu1", "stu2", "stu3"]
    dict1 = {
    	"name": ["张三", "李四", "王五", "小二", ],
    	"age": [12, 21, 32, 32],
    	"group": [1, 2, 1, 1],
    }
    df1 = pd.DataFrame(dict1, index=index)
    writer = pd.ExcelWriter('../read_excel/学生信息.xlsx')
    df1.to_excel(
    			 excel_writer=writer,
    			 index=False,
                 sheet_name="0"
                 )
    
    df1.to_excel(
    			 excel_writer=writer,
    			 index=False,
    			 header=False,
    			 startrow=5,
                 sheet_name="0"
                 )
    writer.close()
    ```

#### DataFrame 查询

##### DataFrame 的索引（查询操作）

1. 直接索引

   + **对单列数据的访问**：DataFrame 的单列数据为一个 Series。根据 DataFrame 的定义可以 知晓 DataFrame 是一个带有标签的二维数组，每个标签相当每一列的列名。有以下两种方式 来实现对单列数据的访问。

     1. 以字典访问某一个 key 的值的方式使用对应的列名，实现单列数据的访问。
     2. 以属性的方式访问，实现单列数据的访问

   + 查询实例

     + 访问某些列 : `df_name[ [列索引1, 列索引2, ...] ]`
     + 访问某些行的某些列 : `df_name[ [列索引1, 列索引2, ...] ][ 行下标1: 行下标2]` 或 `df_name[ 行下标1 : 行下标2][ [列索引1, 列索引2, ...] ]`

   + 实例

     ```python
     import pandas as pd
     
     index = ["stu0", "stu1", "stu2", "stu3"]
     columns = ["name", "age", "group"]
     # 数据部分
     value = [["壮壮", 19, 1],
              ["大壮", 20, 2],
              ["张杰", 19, 1],
              ["樊浩", 17, 2]]
     df = pd.DataFrame(index=index, columns=columns, data=value)
     out = df["name"]
     # print(df)
     """	
          name  age  group
     stu0   壮壮   19      1
     stu1   大壮   20      2
     stu2   张杰   19      1
     stu3   樊浩   17      2
     """
     # 1. 使用索引名称
     print(out["stu1"])  # 大壮
     
     # 2. 使用索引下标
     print(out[2])  # 张杰
     
     # 3. 使用索引名称的切片
     print(out["stu2":"stu2"])
     """
     stu2    张杰
     Name: name, dtype: object
     """
     # 4. 使用索引下标的切片
     print(out[2:3])
     """
     stu2    张杰
     Name: name, dtype: object
     """
     # 5. 使用索引名称的列表
     print(out[["stu1"]])
     """
     stu1    大壮
     Name: name, dtype: object
     """
     # 6. 使用索引下标的列表
     print(out[[2]])
     """
     stu2    张杰
     Name: name, dtype: object
     """
     # 7. head 的形式
     print(out.head(3))
     """
     stu0    壮壮
     stu1    大壮
     stu2    张杰
     Name: name, dtype: object
     """
     # 8. tail 的形式
     print(out.tail(3))
     """
     stu1    大壮
     stu2    张杰
     stu3    樊浩
     Name: name, dtype: object
     """
     
     # 访问多个值
     print(out["stu0":"stu3"])
     """
     stu0    壮壮
     stu1    大壮
     stu2    张杰
     stu3    樊浩
     Name: name, dtype: object
     """
     print(out[["stu1", "stu2"]])
     """
     stu1    大壮
     stu2    张杰
     Name: name, dtype: object
     """
     print(out[1:3])
     """
     stu1    大壮
     stu2    张杰
     Name: name, dtype: object
     """
     ```

     

2. loc 与 iloc 索引方式

   + `DF_name.loc[行信息, 列信息]` 同时获取指定范围内的行列数据 ，不可以使用下标
     + **行信息** : 起始行值 : 结束行值; 也可以使用 关键字/布尔索引
     + **列信息** : 起始列值 : 结尾列值; 也可以使用 关键字/布尔索引
   + `DF_name.iloc[]` 同时行列索引, 只能使用下标