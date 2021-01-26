### Pandas

#### DataFrame 的增删改操作

##### DataFrame 的增加

+ **增加列** : `df["新的列名1"， "新的列名2"]` DataFrame 增加一列只需要**新建一个列索引**,并在该索引下的数据进行赋值操作即可

  ```python
  import pandas as pd
  
  index = ["stu0", "stu1", "stu2", "stu3"]
  dict1 = {
  	"name": ["张三", "李四", "王五", "小二", ],
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
  # 添加列
  df1.loc[:, '科目'] = ["Python", "Java", "C++", "Go"]
  print(df1)
  """
       name  age  group      科目
  stu0   张三   12      1  Python
  stu1   李四   21      2    Java
  stu2   王五   32      1     C++
  stu3   小二   32      1      Go
  """
  ```

  

+ **增加行** : DataFrame 添加一行,需要给各个属性赋值

  ```python
  import pandas as pd
  
  index = ["stu0", "stu1", "stu2", "stu3"]
  dict1 = {
  	"name": ["张三", "李四", "王五", "小二", ],
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
  # 添加行
  
  df1.loc["stu4", :] = ["王二", 33, 2]
  print(df1)
  """
       name   age  group
  stu0   张三  12.0    1.0
  stu1   李四  21.0    2.0
  stu2   王五  32.0    1.0
  stu3   小二  32.0    1.0
  stu4   王二  33.0    2.0
  """
  ```

##### DataFrame 的修改

+ 修改 DataFrame 中的数据 : 

  + 原理 : 将需要修改的数据提取出来,重新赋值成为新数据
  + 注意 : 数据更改直接针对 DataFrame **原数据更改**,操作**无法撤销**,如果做出更改需要**对更改条件做确认**,**对数据进行备份** 
  + 注意 : 如果对列索引内的原数据**直接修改**将会**更改整列的数据为修改数据**,需要与**布尔数组索引结合使用**才可以做到**定位修改**

+ 实例

  + 修改所有

    ```python
    import pandas as pd
    
    index = ["stu0", "stu1", "stu2", "stu3"]
    dict1 = {
    	"name": ["张三", "李四", "王五", "小二", ],
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
    
    # 修改所有分组为 3 组
    df1.loc[:, "group"] = 3
    print(df1)
    """
         name  age  group
    stu0   张三   12      3
    stu1   李四   21      3
    stu2   王五   32      3
    stu3   小二   32      3
    """
    ```

  + 布尔索引

    ```python
    import pandas as pd
    
    index = ["stu0", "stu1", "stu2", "stu3"]
    dict1 = {
    	"name": ["张三", "李四", "王五", "小二", ],
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
    # 通过布尔索引定向修改偶数年龄成员为 3 组
    mark = df1.loc[:, "age"] % 2 == 0
    df1.loc[mark, "group"] = 3
    print(df1)
    """
         name  age  group
    stu0   张三   12      3
    stu1   李四   21      2
    stu2   王五   32      3
    stu3   小二   32      3
    """
    ```

##### DataFrame 的删除

+ `pd.drop(self, labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors="raise",)`

+ 删除行: `df.drop(axis=0, labels=["行名称"], inplace=True)` 与 `df.drop(index=)`

+ 删除列: `df.drop(axis=1, labels=["列名称"], inplace=True)` 与 `df.drop(columns=)`

+ 参数

  | 参数        | 描述                                                         |
  | ----------- | ------------------------------------------------------------ |
  | **labels**  | 指示标签，表示行标或列标                                     |
  | **axis**    | **axis=0** : 删除某些行<br>**axis=1** : 如果要删除某列       |
  | **index**   | 删除行,传入行索引 `.index`                                   |
  | **columns** | 删除列                                                       |
  | **level**   | 针对有两级行标或列标的集合；<br>&emsp;**level = 1**：表示按第2级行删除整行；（即第二列）<br>&emsp;**level = 0**：默认取 0，表示按第1级行标删除整行；（即第一列） |
  | **inplace** | inplace 默认情况下为**False**，表示保持原来的数据不变<br>**True** 则表示在原来的数据上改变。 |
  | **errors**  | **{'ignore', 'raise'}**, 错误处理等级, 默认 **raise**        |

+ 实例

  ```python
  import pandas as pd
  
  index = ["stu0", "stu1", "stu2", "stu3"]
  dict1 = {
  	"name": ["张三", "李四", "王五", "小二", ],
  	"age": [12, 21, 32, 32],
  	"group": [1, 2, 1, 1],
  }
  df1 = pd.DataFrame(dict1, index=index)
  
  """
       name  age  group
  stu0   张三   12      1
  stu1   李四   21      2
  stu2   王五   32      1
  stu3   小二   32      1
  """
  
  # 删除操作
  # df1.loc[:, "明年年龄"] = df1.loc[:, "age"] + 1
  # print(df1)
  # mark = df1.loc[:, "group"] == 2
  # print(df1[mark])
  # df1.drop(df1[mark].index, inplace=True)
  # print(df1)
  """
       name  age  group  明年年龄
  stu1   李四   21      2    22
       name  age  group  明年年龄
  stu0   张三   12      1    13
  stu2   王五   32      1    33
  stu3   小二   32      1    33
  """
  ```

##### DataFrame 的排序

+ `pd.sort_values(self,  by, axis=0, ascending=True, inplace=False, kind="quicksort", na_position="last", ignore_index=False, key: ValueKeyFunc = None,`)` : **默认根据行标签对所有行排序，或根据列标签对所有列排序，或根据指定某列或某几列对行排序。**

  + 参数

    | 参数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | **axis**         | **{0 or ‘index’, 1 or ‘columns’}**, default 0，默认按照列排序，即纵向排序；如果为1，则是横向排序。 |
    | **by**           | **str or list of str**；如果axis=0，那么by="列名"；如果axis=1，那么by="行名"。 |
    | **ascending**    | 布尔型，True则升序，如果by=['列名1','列名2']，则该参数可以是[True, False]，即第一字段升序，第二个降序。 |
    | **inplace**      | 布尔型，是否用排序后的数据框替换现有的数据框,默认为 否 False |
    | **kind**         | 排序方法，**{‘quicksort’, ‘mergesort’, ‘heapsort’}**, default ‘quicksort’ |
    | **na_position**  | **{‘first’, ‘last’}**, default ‘last’，默认缺失值排在最后面。 |
    | **ignore_index** | bool, default False，如果为True，则生成的轴将标记为0，1，…，n-1。 |

    

+ `pd.sort_index(self, axis=0, level=None, ascending: bool = True, inplace: bool = False, kind: str = "quicksort", na_position: str = "last", sort_remaining: bool = True, ignore_index: bool = False, key: IndexKeyFunc = None,)` : **既可以根据列数据，也可根据行数据排序。**,**必须指定by参数，即必须指定哪几行或哪几列；无法根据index名和columns名排序（由.sort_index()执行）**

+ 参数

  | 参数               | 描述                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | **axis**           | **{0 or ‘index’, 1 or ‘columns’}**, default 0，默认按照列排序，即纵向排序；如果为1，则是横向排序。 |
  | **level**          | 默认None，否则按照给定的level顺序排列                        |
  | **ascending**      | 布尔型，True则升序，如果by=['列名1','列名2']，则该参数可以是[True, False]，即第一字段升序，第二个降序。 |
  | **inplace**        | 布尔型，是否用排序后的数据框替换现有的数据框,默认为 否 False |
  | **kind**           | 排序方法，**{‘quicksort’, ‘mergesort’, ‘heapsort’}**, default ‘quicksort’ |
  | **na_position**    | **{‘first’, ‘last’}**, default ‘last’，默认缺失值排在最后面。 |
  | **sort_remaining** | bool, default True 如果为True，并且按级别和索引排序是多级的，则按其他排序<br/>在按指定级别排序后，也按顺序排列级别。 |
  | **ignore_index**   | bool, default False，如果为True，则生成的轴将标记为0，1，…，n-1。 |

  

#### Pandas 的统计分析

+ Numpy 中的**统计学函数**

  | 函数        | 说明   | 函数     | 说明   |
  | ----------- | ------ | -------- | ------ |
  | `np.min`    | 最小值 | `np.max` | 最大值 |
  | `np.mean`   | 均值   | `np.ptp` | 极差   |
  | `np.median` | 中位数 | `np.std` | 标准差 |
  | `np.var`    | 方差   | `np.cov` | 协方差 |
  
+ Pandas 库基于 Numpy 也可以使用这些函数对数据进行描述性统计 (**可以同时求多个数据的值** : `DF_name[[col_name1, col_name2]].max()`)

  | 函数               | 说明     | 函数                     | 说明                     |
  | ------------------ | -------- | ------------------------ | ------------------------ |
  | `DF_name.min`      | 最小值   | `DF_name.max`            | 最大值                   |
  | `DF_name.mean`     | 均值     | `DF_name.ptp`            | 极差                     |
  | `DF_name.median`   | 中位数   | `DF_name.std`            | 标准差                   |
  | `DF_name.var`      | 方差     | `DF_name.mode`           | 众数                     |
  | `DF_name.quantile` | 四分位数 | `DF_name.count`          | 非空值数目               |
  | `DF_name.describe` | 描述统计 | `DF_name.value_counts()` | 返回频数统计,仅限 Series |

+ 数值型需要统计众数，众数出现的次数等信息,需要利用 astype() 进行类型转换,转化为非数值型

+ `DF_name.describe()` : 够一次性得出数据框所有数值型特征的非空 值数目、均值、四分位数、标准差

  ```python
  import pandas as pd
  
  index = ["stu0", "stu1", "stu2", "stu3"]
  dict1 = {
  	"name": ["张三", "李四", "王五", "小二", ],
  	"age": [12, 21, 32, 32],
  	"group": [1, 2, 1, 1],
  }
  df1 = pd.DataFrame(dict1, index=index)
  # print(df1[1:3][["age"]])
  
  
  # df1.drop()
  """
       name  age  group
  stu0   张三   12      1
  stu1   李四   21      2
  stu2   王五   32      1
  stu3   小二   32      1
  """
  
  # 描述性统计
  print(df1.describe())
  """
               age  group
  count   4.000000   4.00
  mean   24.250000   1.25
  std     9.673848   0.50
  min    12.000000   1.00
  25%    18.750000   1.00
  50%    26.500000   1.00
  75%    32.000000   1.25
  max    32.000000   2.00
  """
  ```

  

#### Pandas 的时间数据

+ Pandas 提供了 6 种时间相关的类

+ Pandas 时间模块说明

  | 类名称             | 描述                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | **Timestamp**      | 最基础的时间类。表示**某个时间点**。在绝大多数场景中的时间数据都是 Timestamp 形式的时间。 |
  | **Timedelta**      | 表示**不同单位的时间**，例如 1 天，1.5 小时，3 分钟，4 秒等，而非具体的某个 是时间段。 |
  | **DatetimeIndex**  | **一组 Timestamp 构成的 Index**，可以用来作为 Series 或者 DataFrame 的索引。 |
  | **TimedeltaIndex** | **一组 Timedelta 构成的 Index**，可以作为 Series 或者 DataFrame 的索引。 |

  

##### Timestamp 时间戳类型

+ `pd.to_datetime(arg, unit=None, errors="raise")` 可以将时间相关的字符串转换为 Timestamp,方便查看时间属性

  + 参数

    | 参数          | 描述                                |
    | ------------- | ----------------------------------- |
    | **arg**       | 字符串, timedelta类, 列表 or Series |
    | **unit=None** | 时间单位,默认为"ns"                 |

+ 时间属性

  | 属性       | 说明 | 属性             | 说明           |
  | ---------- | ---- | ---------------- | -------------- |
  | **year**   | 年   | **week**         | 一年中的第几周 |
  | **mouth**  | 月   | **quarter**      | 季度           |
  | **day**    | 日   | **weekofyear**   | 一年中第几周   |
  | **hour**   | 时   | **dayofyear**    | 一年中的第几天 |
  | **minute** | 分   | **dayofweek**    | 一周第几天     |
  | **second** | 秒   | **weekday**      | 一周第几天     |
  | **data**   | 日期 | **weekday_name** | 星期名称       |
  | **time**   | 时间 | **isap_year**    | 是否闰年       |

+ 转换实例

  ```python
  import pandas as pd
  
  str1 = "2020-02-02"
  str2 = "2020/02/02"
  
  # pd.to_timedelta() 将时间字符串转化为 Pandas 的标准时间类型
  t1 = pd.to_datetime(str1)
  print(t1, type(t1))  # 2020-02-02 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
  
  t2 = pd.to_datetime(str2)
  print(t2, type(t2))  # 2020-02-02 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
  
  print(t2.date())  # 2020-02-02
  print(t2.time())  # 00:00:00
  print(f"年份: {t2.year}")  # 年份: 2020
  print(f"月: {t2.month}")  # 月: 2
  print(f"日: {t2.day}")  # 日: 2
  print(f"时: {t2.hour}")  # 时: 0
  print(f"分: {t2.minute}")  # 分: 0
  print(f"秒: {t2.second}")  # 秒: 0
  print(f"是否闰年: {t2.is_leap_year}")  # 是否闰年: True
  
  # 时间字符串列表转换
  time_list = [str1, str2]
  out = pd.to_datetime(time_list)  # DatetimeIndex(['2020-02-02', '2020-02-02'], dtype='datetime64[ns]', freq=None)
  
  print([tmp.year for tmp in out])  # [2020, 2020]
  
  detail = pd.read_excel('../meal_order_detail.xlsx',
                         index_col=0, # 以第 0 列 作为索引
                         )
  
  # print(detail.head())
  print(detail.dtypes)
  """
  order_id                      int64
  dishes_id                     int64
  logicprn_name               float64
  parent_class_name           float64
  dishes_name                  object
  itemis_add                    int64
  counts                        int64
  amounts                       int64
  cost                        float64
  place_order_time     datetime64[ns]
  discount_amt                float64
  discount_reason             float64
  kick_back                   float64
  add_inprice                   int64
  add_info                    float64
  bar_code                    float64
  picture_file                 object
  emp_id                        int64
  dtype: object
  """
  
  detail["day"] = detail["place_order_time"].dt.day
  print(detail[["place_order_time", "day"]])
  """
  detail_id   place_order_time  day                
  2956      2016-08-01 11:05:36    1
  """
  ```


##### Timedelta 时间间隔类型

+ 时间戳 - 时间戳 = 时间间隔

+ 时间间隔 / 时间间隔 = 间隔的具体数字