### Python Numpy 进阶

#### 数组的运算

##### 算术运算 

+ 算术运算符

  | 运算符 | 描述                                                         |
  | ------ | ------------------------------------------------------------ |
  | **+**  | 对应位置相加,三种相加情况<br>&emsp;1. 满足广播机制相加<br>&emsp;2. 数组**形状**相同<br>&emsp;3. 对数组加固定值 |
  | **-**  | 对应位置相减                                                 |
  | *****  | 对应位置相乘                                                 |
  | **/**  | 数组除法                                                     |
  | **%**  | 数组求余                                                     |
  | ****** | 指数                                                         |

  

##### 逻辑运算

+ 逻辑运算符,需要与 `np.any(arr_name)`、`np.all(arr_name)` 搭配使用 代表所有都需要满足条件或者 部分满足

  | 运算符         | 描述                                                         |
  | -------------- | ------------------------------------------------------------ |
  | **and**、**&** | 返回布尔值,与<br>&emsp;**and** : 只支持两边都为 True 的情况，对于列表布尔对比会报错<br>&emsp;**&** : 位运算符,可以对列表布尔数组进行与运算 |
  | **or**         | 返回布尔值,或                                                |
  | **not**        | 返回布尔值,非                                                |
  | **~**          | 取反,返回布尔值                                              |
  | **np.all()**   | 所有元素都满足条件，才返回True                               |
  | **np.any()**   | 只要一个满足条件，返回True                                   |

+ 实例

  ```python
  import numpy as np
  
  arr1 = np.arange(16).reshape(4, 4)
  """
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]
   [12 13 14 15]]
  """
  
  arr2 = np.arange(100, 116).reshape(4, 4)
  """
  [[100 101 102 103]
   [104 105 106 107]
   [108 109 110 111]
   [112 113 114 115]]
  """
  
  print(np.any(arr1 > 14))  # True
  print(np.all(arr1 < 200))  # True
  
  print(~(arr1 > 12))
  """
  [[ True  True  True  True]
   [ True  True  True  True]
   [ True  True  True  True]
   [ True False False False]]
  """
  
  # 将 True作为布尔索引 引入数组 然后返回数组元素
  print(arr1[(arr1 > 12)])
  '''
  [13 14 15]
  '''
  ```

  

##### 关系运算

+ 关系运算符 : 对应位置元素比较

  | 运算符 | 描述                                       |
  | ------ | ------------------------------------------ |
  | **>**  | 大于, 返回布尔数组显示数组内每个值比较结果 |
  | **<**  | 小于, 返回布尔数组显示数组内每个值比较结果 |
  
+ 实例

  ```python
  import numpy as np
  
  arr1 = np.arange(16).reshape(4, 4)
  """
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]
   [12 13 14 15]]
  """
  
  arr2 = np.arange(100, 116).reshape(4, 4)
  """
  [[100 101 102 103]
   [104 105 106 107]
   [108 109 110 111]
   [112 113 114 115]]
  """
  
  out = arr2 > arr1
  print(out)
  """
  [[ True  True  True  True]
   [ True  True  True  True]
   [ True  True  True  True]
   [ True  True  True  True]]
  """
  ```

  

####  Numpy 读写文件

#####  二进制文件

+ `np.save(file, arr, allow_pickle=True, fix_imports=True)` : 以二进制形式保存数据

  + 参数

    | 参数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | **file**         | 文件路径和文件名                                             |
    | **arr**          | 需要保存的数组                                               |
    | **allow_pickle** | **布尔值**,允许使用Python pickles保存对象数组(可选参数,默认即可) |
    | **fix_imports**  | 为了方便Pyhton2中读取Python3保存的数据(可选参数,默认即可)    |

    

+ `np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')` : 从二进制文件读取数据

  + 参数

    | 参数             | 描述                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | **file**         | 文件路径和文件名                                             |
    | **mmap_mode**    | {None, 'r+', 'r', 'w+', 'c'}, 可选参数,读写方法              |
    | **allow_pickle** | **布尔值**,允许使用Python pickles保存对象数组(可选参数,默认即可) |
    | **fix_imports**  | 为了方便Pyhton2中读取Python3保存的数据(可选参数,默认即可)    |
    | **encoding**     | 编码格式,默认为 **ASCII**                                    |

    

+ `np.savez(file, *args, **kwds)` : 将多个数组保存至一个文件,读取时为字典形式

  + 参数

    | 参数         | 描述                                                         |
    | ------------ | ------------------------------------------------------------ |
    | **file**     | 文件路径和文件名                                             |
    | ***args**    | 要存储的数组,可以写多个,如果没有给数组指定Key,Numpy将默认从’arr_0’,'arr_1’的方式命名 |
    | **/*/*kwds** | 可选参数, 可以指定数组保存时的 **key** 值<br>&emsp;`np.savez(file_path, name=arr1, age=arr2, gendel = arr3)` |

  + 实例

    ```python
    import numpy as np
    arr1 = np.arange(16).reshape(4, 4)
    """
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]
    """
    
    arr2 = np.arange(100, 116).reshape(4, 4)
    """
    [[100 101 102 103]
     [104 105 106 107]
     [108 109 110 111]
     [112 113 114 115]]
    """
    
    arr3 = np.arange(12, 24).reshape(4, 3)
    """
    [[12 13 14]
     [15 16 17]
     [18 19 20]
     [21 22 23]]
    """
    # 读取 save 保存的文件
    np.save('./arr3', (arr1, arr2))
    print(np.load('./arr3.npy'))
    """
    [[[  0   1   2   3]
      [  4   5   6   7]
      [  8   9  10  11]
      [ 12  13  14  15]]
    
     [[100 101 102 103]
      [104 105 106 107]
      [108 109 110 111]
      [112 113 114 115]]]
    """
    # 读取 savez 保存的 npz 文件
    np.savez('./arr3.npy', arr1, arr2, arr3)
    print(np.load('./arr3.npy.npz', 'r')['arr_1'])
    """
    [[100 101 102 103]
     [104 105 106 107]
     [108 109 110 111]
     [112 113 114 115]]
    """
    ```

    

+ 存储是可以省略拓展名、读取是不能省略拓展名

#####  读取文本格式的数据 (TXT CSV 格式)

+ `np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)` : 将数组写入到某种分隔符隔开的文本文件

  + 参数

    | 参数          | 描述                                                         |
    | ------------- | ------------------------------------------------------------ |
    | **fname**     | 文件名或文件句柄,如果文件名结束`.gz`，文件将自动以压缩gzip格式保存。 `loadtxt`透明地理解gzip文件。 |
    | **X**         | 1D或2D array_like,要保存到文本文件的数据。                   |
    | **fmt**       | str或strs序列，**可选**,单个格式（％10.5f），格式序列或多格式字符串 |
    | **delimiter** | **分隔符**，str，**可选**，分隔列的字符串或字符。            |
    | **newline**   | **换行符** ： str，**可选**，字符串或字符分隔线。            |
    | **header**    | **header** ： str，可选，将在文件开头写入的字符串。          |
    | **footer**    | **页脚** ： str，可选，将写在文件末尾的字符串。              |
    | **comments**  | **评论** ： str，可选，将附加到`header`和`footer`字符串的字符串，以将其标记为注释。默认值：'＃' |
    | **encoding**  | {None，str}，可选，用于编码输出文件的编码。不适用于输出流。如果编码不是'bytes'或'latin1'，您将无法在NumPy版本<1.14中加载该文件。默认为'latin1'。 |

    

+ `np.loadtxt(fname, dtype=float, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None)` : 把文件加载到一个二维数组中,不可以加载包含缺失值的文件

  + 参数

    | 参数           | 描述                                              |
    | -------------- | ------------------------------------------------- |
    | **fname**      | **路径和文件名**                                  |
    | **dtype**      | **读取数据类型**,默认的 Float                     |
    | **comments**   | 跳过文件中指定参数开头的行（即不读取）            |
    | **delimiter**  | **分隔符**，str，**可选**，分隔列的字符串或字符。 |
    | **converters** | 对读取的数据进行预处理                            |
    | **skiprows**   | 选择跳过的行数                                    |
    | **usecols**    | 指定需要读取的列                                  |
    | **unpack**     | 选择是否将数据进行向量输出                        |
    | **ndim**       |                                                   |
    | **encoding**   | 对读取的文件进行预编码                            |
    | **max_rows**   | 读取最大行数                                      |

+ `np.genfromtxt(fname, dtype=float, comments='#', delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=None)` : 可以加载包含缺失值的文件，当读取数据类型预加载为 int 时,缺失数据填充为 -1, 当为其他类型时填充为 None

####  数组排序

##### 直接排序

+ `arr.sort(self, axis=-1, kind=None, order=None)` : 直接排序

  ```python
  import numpy as np
  
  np.random.seed(1)
  
  # 产生随机数
  random_num = np.random.randint(1, 10, 6)
  """
  [6 9 6 1 1 2]
  """
  
  random_num.sort()
  # 等同于
  # print(sorted(random_num))  # 不改变原数组值
  """
  [1 1 2 6 6 9]
  """
  ```

  

##### 间接排序

+ `arr.argsort(self, axis=-1, kind=None, order=None)` : 返回重新排序值的下标，根据下标获取需要的值,默认 axis 值为 -1

  ```python
  import numpy as np
  
  np.random.seed(1)
  
  # 产生随机数
  random_num = np.random.randint(1, 10, 6)
  """
  [6 9 6 1 1 2]
  下标
   0 1 2 3 4 5
  """
  
  # 间接排序
  # print(np.argsort(random_num))
  # 等同于
  # print(random_num.argsort())
  sort_index = random_num.argsort()
  """
  排序后下标
  [3 4 5 0 2 1]
  对应值
  [1 1 2 6 6 9]
  """
  # 获取对应值, 根据下标
  print(random_num[sort_index[0]])  # 最小值 1
  print(random_num[sort_index[-1]])  # 最大值 9
  print(random_num)  # [6 9 6 1 1 2]  不改变原数组值
  arr2 = np.random.randint(1, 30, size=(3, 4))
  print(arr2)
  """
  [[ 6 12 13  9]
   [10 12  6 16]
   [ 1 17  2 13]]
  """
  arr2_sort = arr2.argsort()
  """
  [[0 3 1 2]
   [2 0 1 3]
   [0 2 3 1]]
  """
  arr2_sort = arr2.argsort(axis=0)
  """
  [[2 0 2 0]
   [0 1 1 2]
   [1 2 0 1]]
  """
  ```

  

#### 数组去重与重复

##### 数组去重

+ `np.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)` : 找出数组中的唯一值并返回已排序结果  (去除数组中的重复数字，并进行从小到大排序之后输出,多维数组去重后展平为一维数组)

  + 参数

    | 参数               | 描述                                                         |
    | ------------------ | ------------------------------------------------------------ |
    | **ar**             | 传入数组                                                     |
    | **return_index**   | 默认为 **False**; 为 **True** 时,返回**新列表**中的每个元素在**原列表**中**第一次**出现的索引值，因此元素个数与新列表中元素个数一样 |
    | **return_inverse** | 默认为 **False**;为 **True** 时 返回**原列表**中的每个元素在**新列表**中出现的索引值，因此元素个数与原列表中元素个数一样 |
    | **return_counts**  | 返回数目                                                     |
    | **axis**           | 按轴去重,默认为 None<br>&emsp;**0** : 去掉重复行<br>&emsp;**1** : 去掉重复的列 |

  + 实例

    ```python
    import numpy as np
    np.random.seed(1)
    
    # 随机整数
    arr = np.random.randint(1, 10, 6)
    """
    [6 9 6 1 1 2]
    """
    arr_list = np.random.randint(1, 10, size=(2, 4))
    """
    [[8 7 3 5]
     [6 3 5 3]]
    """
    
    print(np.unique(arr))
    """
    [1 2 6 9]
    """
    
    print(np.unique(arr_list))
    """
    [3 5 6 7 8]
    """
    
    out_arr2 = np.tile(arr_list, (2, 2))
    """
    [[8 7 3 5 8 7 3 5]
     [6 3 5 3 6 3 5 3]
     [8 7 3 5 8 7 3 5]
     [6 3 5 3 6 3 5 3]]
    """
    print(np.unique(out_arr2, axis=1))
    """
    [[3 5 7 8]
     [5 3 3 6]
     [3 5 7 8]
     [5 3 3 6]]
    """
    print(np.unique(out_arr2, axis=0))
    """
    [[6 3 5 3 6 3 5 3]
     [8 7 3 5 8 7 3 5]]
    """
    ```

    

##### 数组重复

+ `np.tile(A, reps)` 和 `np.repeat(a, repeats, axis=None)` : 进行数组重复

+ 区别

  + tile 函数是对数组进行重复操作
  + repeat 函数是对数组 中的每个元素进行重复操作

+ 参数

  + `np.repeat(a, repeats, axis=None)`

    | 参数        | 描述                    |
    | ----------- | ----------------------- |
    | **a**       | 被重复数据              |
    | **repeats** | 重复次数,整数或整数序列 |
    | **axis**    | **可选**, 重复轴        |

  + `np.tile(A, reps)`

    | 参数     | 描述                    |
    | -------- | ----------------------- |
    | **A**    | 被重复数组              |
    | **reps** | 重复次数,整数或整数序列 |

+ 实例

  + **repeat** 重复 : 如果**repeats** 是一个序列,如果是一维数组,序列长度必须和一维数组长度一致;如果是二维数组,序列需要和二维数组**行**长度一致

    ```python
    import numpy as np
    
    np.random.seed(1)
    
    # 随机整数
    arr = np.random.randint(1, 10, 6)
    """
    [6 9 6 1 1 2]
    """
    arr_list = np.random.randint(1, 10, size=(2, 4))
    """
    [[8 7 3 5]
     [6 3 5 3]]
    """
    
    # 重复函数 np. repeat、np.tile
    out = np.repeat(arr, 2)
    """
    [6 6 9 9 6 6 1 1 1 1 2 2]
    """
    # 必须一一对应 第一行重复 2 次 第二行 重复 4 次
    out_arr = np.repeat(arr_list, [2, 4], axis=0)
    """
    [[8 7 3 5]
     [8 7 3 5]
     [6 3 5 3]
     [6 3 5 3]
     [6 3 5 3]
     [6 3 5 3]
    """
    ```

  + **tile** : **reps** 为序列 **(m, n)** 时,表示生成新的数组为 **m 行**， 每行重复 **n 次**

    ```python
    import numpy as np
    
    np.random.seed(1)
    
    # 随机整数
    arr = np.random.randint(1, 10, 6)
    """
    [6 9 6 1 1 2]
    """
    arr_list = np.random.randint(1, 10, size=(2, 4))
    """
    [[8 7 3 5]
     [6 3 5 3]]
    """
    
    # 将数组作为整体重复
    out = np.tile(arr, 2)
    """
    [6 9 6 1 1 2 6 9 6 1 1 2]
    """
    out_arr = np.tile(arr_list, 2)
    """
    [[8 7 3 5 8 7 3 5]
     [6 3 5 3 6 3 5 3]]
    """
    out_arr1 = np.tile(arr, (2, 2))
    """
    变为 2列的 数组 重复两次
    [[6 9 6 1 1 2 6 9 6 1 1 2]
     [6 9 6 1 1 2 6 9 6 1 1 2]]
    """
    out_arr2 = np.tile(arr_list, (2, 2))
    """
    [[8 7 3 5 8 7 3 5]
     [6 3 5 3 6 3 5 3]
     [8 7 3 5 8 7 3 5]
     [6 3 5 3 6 3 5 3]]
    """
    ```

    

#### 数组的运算

+ 统计分析方法

  | 方法          | 描述         |
  | ------------- | ------------ |
  | **sum()**     | 求和         |
  | **mean()**    | 求平均数     |
  | **std()**     | 标准差       |
  | **var()**     | 方差         |
  | **max()**     | 求最大值     |
  | **argmax()**  | 最大值的索引 |
  | **min()**     | 求最小值     |
  | **argmin()**  | 最小值的索引 |
  | **cumsum()**  | 累计和       |
  | **cumprod()** | 累计积       |

  