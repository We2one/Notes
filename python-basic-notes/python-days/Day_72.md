### Pandas

#### 数据处理

##### 数据标准化

+ 三种标准化处理 **离差标准化数据**、**标准差标准化数据**、**小数定标标准化数据**

+ **离差标准化数据**

  + 离差标准化是对原始数据的一种线性变换，结果是将原始的数据映射到[0,1] 区间之间
  + *X = (X-min)/(max-min)*
    + max 为样本数据的最大值
    + min 为样本数据的最小值
    + max-min 为极差
    + 利差标准化保留了原始数据值之间的联系，是消除量纲和数据取值范围影响最简 单的方法

+ **标准差标准化数据**

  + 标准差标准化也叫零均值标准化或分数标准化，是当前使用最广泛的数据标 准化方法。经过该方法处理后的均值为 0，标准差为 1，
  + *X=(x - x的反)/σ*
    + **X反** 为原始数据的均值
    + **σ** 为原始数据的标准差。
  + 标准差后的值区间不局限于[0,1]，并且存在负值。同时也不难发现，标准差 标准化和离差标准化一样不会改变数据的分布情况。

+ **小数定标标准化数据**

  + 通过移动数据的小数位数，将数据映射到区间[-1,1]之间，移动的小数位数 取决于数据绝对值的最大值
  + *X=X/10^k*

+ 三种标准化特点

  1. 离差标准化方法简单，便于理解，标准化后的数据限定在[0,1]区间内；
  2. 标准差标准化受数据分布的影响较小；
  3. 小数定标标准化方法的适用范围广，并且受数据分布的影响较小，相比较于 前面两种方法而言该方法适用程度适中。

+ 实例

  ```python
  import numpy as np
  import pandas as pd
  
  infos = pd.read_excel("./学生信息.xlsx", index_col=0)
  print("转化前:\n", infos)
  
  # 离差标准化 -- 最小最大标准化
  # def min_max_scalar(val):
  # 	return (val- val.min()) / (val.max() - val.min())
  #
  #
  # infos["score"] = infos["score"].transform(min_max_scalar)
  # infos["hight"] = infos["hight"].transform(min_max_scalar)
  # print("转化后:\n", infos)
  
  # 标准差标准化
  # def stand_scalar(val):
  # 	mean_val = val.mean()
  # 	std_val = val.std()
  # 	return (val-mean_val) /std_val
  #
  #
  # infos["score"] = infos["score"].transform(stand_scalar)
  # infos["hight"] = infos["hight"].transform(stand_scalar)
  # print("转化后:\n", infos)
  
  
  # 小数定标标准化, 将数据转化为小数减少数据间误差
  def abs_max_log_scalar(val):
  	# exp1 = val.abs()
  	# exp2 = exp1.max()
  	# exp3 = np.log10(exp2)
  	# exp4 = np.ceil(exp3)
  	# k = 10 ** exp4
  	k = 10 ** (np.ceil(np.log10((val.abs()).max())))
  	return val / k
  
  infos["score"] = infos["score"].transform(abs_max_log_scalar)
  infos["hight"] = infos["hight"].transform(abs_max_log_scalar)
  print("转化后:\n", infos)
  ```

  

##### 数据转换

+ **哑变量处理类别数据**

  1. **哑变量处理** : 将非数字型数据转化为哑变量存储

  2. **`pd.get_dummies(data, prefix=None, prefix_sep="_", dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None,)` : 进行数据的哑变量转化**

     + 参数

       | 参数           | 描述                                                         |
       | -------------- | ------------------------------------------------------------ |
       | **data**       | 可以是数组类型，Series类型，DataFrame类型                    |
       | **prefix**     | 可以字符串，字符串列表，或字符串的字典类型，默认为None。给输出的列添加前缀，如prefix="A",输出的列会显示类似 |
       | **prefix_sep** | 设置前缀跟分类的分隔符sepration，默认是下划线"_"             |
       | **dummy_na**   | bool，默认为False如果忽略False NaN，请添加一列以指示NaN。    |
       | **columns**    | 要编码的DataFrame中的列名。如果columns为“无”，则将转换所有对象或类别为dtype的列 。 |
       | **sparse**     | 是否应使用`SparseArray`（True）或常规NumPy数组（False）支持伪编码列。 |
       | **drop_first** | 布尔型，默认为False，指是否删除第一列                        |
       | **dtype**      | 新列的数据类型。仅允许单个dtype。                            |

       

+ **离散化**

  + 离散的概念

    + 某些模型算法，要求数据是离散的，此时就需要将连续型特征（数值型）变 换成离散型特征（类别型）
    + 连续特征的离散化就是在数据的取值范围内设定若干个离散的划分点，将取 值范围划分为一些离散化的区间，最后用不同的符号或整数值代表落在每个子区 间中的数据值
    + 此离散化涉及两个子任务 : **确定分类数**以及**如何将连续型数据映射到这 些类别型数据上**

  + **离散化方法——等宽法**

    + 将数据的值域分成具有相同宽度的区间，区间的个数由数据本身的特点决定 或者用户指定，与制作频率分布表类似。pandas 提供了 cut 函数，可以进行连 续型数据的等宽离散化

    + `pd.cut(x, bins, right: bool = True, labels=None, retbins: bool = False, precision: int = 3, include_lowest: bool = False, duplicates: str = "raise", ordered: bool = True,)` : 将连续数据离散化

      + 参数

        | 参数               | 描述                                                         |
        | ------------------ | ------------------------------------------------------------ |
        | **x**              | 被切分的类数组（array-like）数据，必须是1维的（不能用DataFrame） |
        | **bins**           | bins是被切割后的区间（或者叫“桶”、“箱”、“面元”），有3中形式：一个int型的标量、标量序列（数组）或者pandas.IntervalIndex 。一个int型的标量. 当bins为一个int型的标量时，代表将x平分成bins份。x的范围在每侧扩展0.1%，以包括x的最大值和最小值。标量序列. 标量序列定义了被分割后每一个bin的区间边缘，此时x没有扩 .pandas.IntervalIndex<br/>定义要使用的精确区间。 |
        | **right**          | bool型参数，默认为True，表示是否包含区间右部。比如如果bins=[1,2,3]，right=True，则区间为(1,2]，(2,3]；right=False，则区间为(1,2),(2,3)。 |
        | **labels**         | 给分割后的bins打标签，比如把年龄x分割成年龄段bins后，可以给年龄段打上诸如青年、中年的标签。labels的长度必须和划分后的区间长度相等，比如bins=[1,2,3]，划分后有2个区间(1,2]，(2,3]，则labels的长度必须为2。如果指定labels=False，则返回x中的数据在第几个bin中（从0开始）。 |
        | **retbins**        | bool型的参数，表示是否将分割后的bins返回，当bins为一个int型的标量时比较有用，这样可以得到划分后的区间，默认为False。 |
        | **precision**      | 保留区间小数点的位数，默认为3.                               |
        | **include_lowest** | bool型的参数，表示区间的左边是开还是闭的，默认为false，也就是不包含区间左部（闭）`duplicates`：是否允许重复区间。有两种选择：`raise`：不允许，`drop`：允许。 |

    + 缺陷 : 若数据分布不均匀，那么各个类的数目也会变得非常不均匀，有些区间包含许多数据， 而另外一些区间的数据极少，这会严重损坏所建立的模型

  + **离散化方法——等频法**

    + 等频法离散化的方法相比较于等宽法离散化而言，避免了类分布不均匀的问 题，但同时却也有可能将数值非常接近的两个值分到不同的区间以满足每个区间 中固定的数据个数。
    + `cut()` 或 `qcut()`

  + **离散化方法——基于聚类分析的方法**

    + 一维聚类的方法包括两个步骤：
      1. 将连续型数据用聚类算法（如 K-Means 算法等）进行聚类
      2. 处理聚类得到的簇，将合并到一个簇的连续型数据做同一标记。
      3. 聚类分析的离散化方法需要用户指定簇的个数，用来决定产生的区间数。
    + k-Means 聚类分析的离散化方法可以很好地根据现有特征的数据分布状况 进行聚类，但是由于 k-Means 算法本身的缺陷，用该方法进行离散化时依旧需要 指定离散化后类别的数目。此时需要配合聚类算法评价方法，找出最优的聚类簇 数目

+ 非数值转换为数值
+ 连续数据转化为离散数据



