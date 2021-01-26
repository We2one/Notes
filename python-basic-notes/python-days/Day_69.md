### Pandas 

#### Pandas 的分组聚合

##### 使用 groupby 方法进行分组

+ `DF_name.groupby(self, by=None, axis=0, level=None, as_index: bool = True, sort: bool = True, group_keys: bool = True, squeeze: bool = no_default, observed: bool = False, dropna: bool = True,)` : 提供分组聚合步骤中的**拆分功能**，能根据**索引**或**字段**对数据进行 分组

  + 参数

    | 参数           | 描述                                                         |
    | -------------- | ------------------------------------------------------------ |
    | **by**         | 接收 list，string，mapping 或者 generator。用于确定进行 分组的依据。无默认。<br>&emsp;**list** : 根据多个条件分组<br>&emsp;**string** : 根据一个条件分组 |
    | **axis**       | 接收 int。表示操作的轴向，默认对行进行操作。默认为 0         |
    | **level**      | 接收 int 或者索引名，代表标签所在级别。默认为 None。         |
    | **as_index**   | 接收 boolearn。表示聚合后的聚合标签是否以 DataFrame 索引形式输出。默认为 True。 |
    | **sort**       | 接收 boolearn。表示是否依据分组标签进行排序。默认为 True     |
    | **group_keys** | 接收 boolearn。表示是否显示分组标签的名称。默认为 True。     |
    | **squeeze**    | 接收 boolearn。表示是否在允许的情况下对返回数据进行降 维，默认为 False。 |

  + 分组后获取的是 DataFrame 类 不可以直接查看,需要遍历 `group.groups` 获取 key 值 ，使用 `group.get_group(key)` 获取分组属性

  + 实例

    ```python
    import numpy as np
    import pandas as pd
    
    detail = pd.read_excel('./学生信息.xlsx', index_col=0)
    # print(detail.columns)
    """
    Index(['Unnamed: 0', 'cls_id', 'group_id', 'name', 'hight', 'score', '性别'], dtype='object')
    """
    
    group1 = detail.groupby(by="cls_id")
    # 返回的是 DataFrame 类,不可以直接查看，但是可以遍历
    # print(group1)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F065389E10>
    
    for key in group1.groups:
    	# 分组的键
    	print(key)
    	# 根据键获取每组的内容
    	print(group1.get_group(key))
    	"""
    	A
    	      cls_id  group_id name  hight  score 性别
    	Stu_0      A         1  赵朝贺    170   99.0  男
    	Stu_1      A         1  张向丹    172   98.0  女
    	Stu_2      A         1  孙成林    185   97.5  男
    	Stu_3      A         2  王子婧    190   96.0  女
    	Stu_4      A         2   王博    173   89.0  男
    	Stu_5      A         2  余泽昌    156   85.0  男
    	B
    	       cls_id  group_id name  hight  score 性别
    	Stu_6       B         1  申琳艳    162   99.0  女
    	Stu_7       B         1   冯淼    165   78.0  女
    	Stu_8       B         1  曹迟星    189   89.0  男
    	Stu_9       B         2  王亚东    178   88.0  男
    	Stu_10      B         2  吴亚成    175   92.0  男
    	"""
    
    # 求每个班级的成绩最大值
    out1 = group1["score"].max()  # 返回一个 Series
    print(out1)
    """
    cls_id
    A    99.0
    B    99.0
    Name: score, dtype: float64
    """
    out2 = group1[["score"]].max()  # 返回一个 DataFrame
    print(out2.reset_index())
    """
    cls_id   score
    A        99.0
    B        99.0
    """
    
    # 分组多个内容
    group2 = detail.groupby(by=["cls_id", "group_id"])
    
    for key in group2.groups:
    	print(key)
    	print(group2.get_group(key))
    	"""
    	('A', 1)
    	      cls_id  group_id name  hight  score 性别
    	Stu_0      A         1  赵朝贺    170   99.0  男
    	Stu_1      A         1  张向丹    172   98.0  女
    	Stu_2      A         1  孙成林    185   97.5  男
    	('A', 2)
    	      cls_id  group_id name  hight  score 性别
    	Stu_3      A         2  王子婧    190   96.0  女
    	Stu_4      A         2   王博    173   89.0  男
    	Stu_5      A         2  余泽昌    156   85.0  男
    	('B', 1)
    	      cls_id  group_id name  hight  score 性别
    	Stu_6      B         1  申琳艳    162   99.0  女
    	Stu_7      B         1   冯淼    165   78.0  女
    	Stu_8      B         1  曹迟星    189   89.0  男
    	('B', 2)
    	       cls_id  group_id name  hight  score 性别
    	Stu_9       B         2  王亚东    178   88.0  男
    	Stu_10      B         2  吴亚成    175   92.0  男
    	"""
    
    out3 = group2["score"].max()
    out3 = out3.reset_index()  # 将索引变为正常的一列
    print(out3)  # <class 'pandas.core.frame.DataFrame'>
    """
      cls_id  group_id  score
    0      A         1   99.0
    1      A         2   96.0
    2      B         1   99.0
    3      B         2   92.0
    """
    ```

##### 使用统计分析函数聚合数据

+ 利用统计分析函数对分组后对象进行计算和合并

+ Groupby 对象常用的描述性统计函数

  | 函数              | 描述                      | 函数               | 描述                               |
  | ----------------- | ------------------------- | ------------------ | ---------------------------------- |
  | **group.count**   | 计算分组的数目,包括缺失值 | **group.cumcount** | 对每个分组中组员进行标记，0 至 n-1 |
  | **group.head(n)** | 返回每组的前 n 个值       | **group.size**     | 返回每组的大小                     |
  | **group.max**     | 返回每组的最大值          | **group.min**      | 返回每组的最小值                   |
  | **group.mean**    | 返回每组的均值            | **group.std**      | 返回每组的标准差                   |
  | **group.median**  | 返回每组的中位数          | **group.sum**      | 返回每组的和                       |

##### 使用 agg 函数进行聚合数据

+ `DF_name.agg(self, func=None, axis=0, *args, **kwargs)` :支持对每个分组应用多个函数，包括 Python 内置函数或自定义函 数。同时这个方法也能够直接对 DataFrame 进行应用操作,等同于 **aggregate**

+ 参数

  | 参数     | 描述                                                   |
  | -------- | ------------------------------------------------------ |
  | **func** | 接收 list、dict、function。表示应用于每行/每列的 函数  |
  | **axis** | 接收 0 或者 1，代表操作的轴向，默认为 0，表示行 的方向 |

+ 实例

  ```python
  import pandas as pd
  
  detail = pd.read_excel('../学生信息.xlsx', index_col=0)
  
  group1 = detail.groupby(by="cls_id")
  
  print(group1[["score", "hight"]].agg(["max", "min"]).reset_index())
  """
    cls_id score       hight     
             max   min   max  min
  0      A  99.0  85.0   190  156
  1      B  99.0  78.0   189  162
  """
  ```

+ 对不同列 统计不同数量指标

  ```python
  import pandas as pd
  
  detail = pd.read_excel('../学生信息.xlsx', index_col=0)
  
  group1 = detail.groupby(by="cls_id")
  
  # 对不同列统计不同数量的统计指标
  print(group1[["score", "hight"]].agg({"score": "max", "hight": np.mean}).reset_index())
  """
    cls_id  score       hight
  0      A   99.0  174.333333
  1      B   99.0  173.800000
  """
  ```

+ 使用自定义函数

  ```python
  import numpy as np
  import pandas as pd
  
  detail = pd.read_excel('../学生信息.xlsx', index_col=0)
  
  group1 = detail.groupby(by="cls_id")
  
  # 最大值减最小值
  def max_min(val):
  	out = val.max() - val.min()
  	return out
  
  print(group1[["score", "hight"]].agg({"score": ["max", "min"], "hight": [np.mean, max_min]}).reset_index())
  """
    cls_id score             hight        
             max   min        mean max_min
  0      A  99.0  85.0  174.333333      34
  1      B  99.0  78.0  173.800000      27
  """
  ```

+ 操作对象是 Series 而不是 DataFrame 的时候

  ```python
  import pandas as pd
  
  detail = pd.read_excel('../学生信息.xlsx', index_col=0)
  
  # 操作对象是一个 series 时
  def add_value(val):
  	out = val + 10
  	return out
  
  detail["hight_10"] = detail["hight"].agg(add_value)
  print(detail[["hight", "hight_10"]])
  """
          hight  hight_10
  Stu_0     170       180
  Stu_1     172       182
  Stu_2     185       195
  Stu_3     190       200
  Stu_4     173       183
  Stu_5     156       166
  Stu_6     162       172
  Stu_7     165       175
  Stu_8     189       199
  Stu_9     178       188
  Stu_10    175       185
  """
  ```

##### transfrom 转换

+ `DF_name.transfrom()` : Transform 方法能够对整个 DataFrame 的所有元素进行操作。且 transform 方法只有一个参数“func”，表示对 DataFrame 操作的函数

+ transform 方法还能够对 DataFrame 分组后的对象 GroupBy 进行操作, 常用于数据标准化

+ transform 和 agg 的**区别** : 在于 transform 对于整列数据的**每一个元素**进行运 算，而 agg 以**整列**进行运算。

+ 实例

  ```python
  import pandas as pd
  
  detail = pd.read_excel('../学生信息.xlsx', index_col=0)
  
  # 将身高由 cm 变为 m
  # group1 = detail["hight"].transform(lambda x: x/100)
  # print(group1)
  """
  Stu_0     1.70
  Stu_1     1.72
  Stu_2     1.85
  Stu_3     1.90
  Stu_4     1.73
  Stu_5     1.56
  Stu_6     1.62
  Stu_7     1.65
  Stu_8     1.89
  Stu_9     1.78
  Stu_10    1.75
  Name: hight, dtype: float64
  """
  
  # def transform_0_1(val):
  # 	val_max = val.max()
  # 	val_min = val.min()
  # 	return (val - val_min) / (val_max - val_min)
  #
  #
  # print(detail.groupby('cls_id')['score'].transform(transform_0_1))
  
  # group1 = detail.groupby(by="cls_id")["score"].transform(lambda x: max(x))
  # print(group1)
  """
  Stu_0     99.0
  Stu_1     99.0
  Stu_2     99.0
  Stu_3     99.0
  Stu_4     99.0
  Stu_5     99.0
  Stu_6     99.0
  Stu_7     99.0
  Stu_8     99.0
  Stu_9     99.0
  Stu_10    99.0
  Name: score, dtype: float64
  """
  ```

#### Pandas 的透视表和交互表

##### 透视表

+ **透视表** : 数据透视表，是一种**交互式的表**，可以进行某些计算。之所以被称 为透视表，主要是由于*数据的行、列索引发生变化，透视表会立即生成新的数据* 表格。在 python 中，可以理解透视表为一个 plus 版本的分组聚合

+ 利用 pivot_table 函数可以实现透视表

+ `pd.pivot_table(data, values=None, index=None, columns=None, aggfunc="mean", fill_value=None, margins=False, dropna=True, margins_name="All", observed=False,)`

  + 参数

    | 参数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | **data**         | 接收 **DataFrame**。表示创建表的数据。 无默认                |
    | **values**       | 接收**字符串**。用于指定想要**聚合的数据 字段名**，默认使用全部数据。默认为 None<br>&emsp;当全部数据列数很多时，若只想要显示某列，可以通过指定 values 参数来 实现 |
    | **index**        | 接收 **string** 或者 **list**。表示**行分组键**,使用列名称。 默认为 None<br>&emsp;pivot_table 函数在创建透视表的时候分 组键 index 可以有多个 |
    | **columns**      | 接收 **string** 或者 **list**。表示**列分组键**用行名称。 默认为 None |
    | **aggfunc**      | 接收 functions。表示聚合函数，默认 mean<br>&emsp;在不特殊指定聚合函数 aggfunc 时，会**默认使用 numpy.mean** 进行聚合运算， numpy.mean 会**自动过滤掉非数值类型数据**。可以通过指定 aggfunc 参数修改聚 合函数 |
    | **fill_value**   | 当某些数据不存在时，会自动填充 NaN，因此可以指定 fill_value 参数， 表示当存在缺失值时，以指定数值进行填充 |
    | **margins**      | 接收 boolean。表示汇总功能的开关， 设为 True 后结果集中会出现名 为”ALL”的行和列，默认为 True |
    | **dropna**       | 接收 boolean。表示是否删除掉全为 NaN 的列，默认为 False      |
    | **margins_name** | 汇总后名称,默认是 ALL                                        |
    | **observed**     |                                                              |

    

##### 交叉表

+ **交叉表** : 交叉表是一种**特殊的透视表**，主要用于**计算分组频率**。可以利用 pandas 提 供的 crosstab 函数制作交叉表

+ **与透视表不同**之处 : 在于 crosstab 函数中的 index，columns，values 填入的都是对应的从 Dataframe 中取出的某 一列。

+ values 和 aggfunc 必须同时出现,或者同时不出现

  + 同时不出现 : 频数统计、统计每组的数目
  + 同时不出现 : 简单透视表

+ `pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name: str = "All", dropna: bool = True, normalize=False,)`

  + 参数

    | 参数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | **index**        | 接收 **string** 或者 **list**。表示行索引键                  |
    | **columns**      | 接收 **string** 或者 **list**。表示行索引键                  |
    | **values**       | 接收 array。表示聚合数据，默认为 None。                      |
    | **rowname**      |                                                              |
    | **colnames**     |                                                              |
    | **aggfunc**      | 接收 function。表示**聚合函数**，默认为 None。               |
    | **margins**      | 接收 boolearn。表示**汇总功能的开关**，设为 True 后结果集中会出 现名为”ALL”的行和列。 |
    | **margins_name** | 汇总后名称,默认是 All                                        |
    | **dropna**       | 接收 boolearn，表示**是否删除掉全部为 NaN 的列**，默认为 False |
    | **normalize**    | 接收 boolearn。表示**是否对值进行标准化**。默认为 False。    |

  + 实例

    ```python
    import pandas as pd
    
    
    infos = pd.read_excel("../学生信息.xlsx")
    print(infos)
    
    group1 = infos.groupby(by="cls_id")["hight"].max()
    
    print(group1)
    
    # data 对部分数据进行透视
    # index 行分组键 --- 使用列名称
    # value 关注的数据
    out = pd.pivot_table(
    		data=infos,
    		index="cls_id",
    		values="hight",
    		aggfunc="max",
    	)
    print(out)
    """
            hight
    cls_id       
    A         190
    B         189
    """
    
    out1 = pd.crosstab(
    	index=infos["cls_id"],  # 以 cls_id 作为行索引
    	columns=infos["group_id"],  # group_id 作为列索引
    	values="hight",
    	aggfunc="max"
    )
    print(out1)
    """
    group_id      1      2
    cls_id                
    A         hight  hight
    B         hight  hight
    """
    ```

    