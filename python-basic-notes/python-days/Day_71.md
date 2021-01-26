### Pandas

#### 数据处理

##### 数据清洗

+ 收集的数据存在脏数据、异常数据、空数据
  + **重复值处理**

    + 检测与处理重复值

      1. 记录重复 (重复行) series unique : 不限于两行内容完全一致,关键列信息一致也可以认为是重复行

         1. 方法一、利用列表 (list) 进行去重 , 自定义去重函数

         2. `DF_name.drop_duplicates(self, subset: Optional[Union[Hashable, Sequence[Hashable]]] = None, keep: Union[str, bool] = "first", inplace: bool = False, ignore_index: bool = False,)`

            + 参数

              | 参数             | 描述                                                         |
              | ---------------- | ------------------------------------------------------------ |
              | **subset**       | 列名，可选，默认为None，选取某几列,如果存在重复列,认为原 DF 中该行重复 |
              | **keep**         | **{‘first’, ‘last’, False}**, 默认值 ‘first’<br>&emsp;**first**： 保留第一次出现的重复行，删除后面的重复行。<br>&emsp;**last**： 删除重复项，除了最后一次出现。<br>&emsp;**False**：删除所有重复项。 |
              | **inplace**      | 布尔值，默认为False，是否直接在原数据上删除重复项或删除重复项后返回副本。（inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本。） |
              | **ignore_index** | 忽略 列                                                      |

      2. 特征重复 (重复列)  -- 根据两列之间的相关性 (相似度) 来确定

         + **相似度[-1, 1]**

           + **1** : 正相关 
           + **0** : 无关
           + **-1** : 负相关

         + `df.corr(self, method="pearson", min_periods=1)`

           + 参数

             + **method** : *{"pearson", "kendall", "spearman"}* 计算相似度的方法， 默认 pearson ,常用

           + 实例

             ```python
             import pandas as pd
             
             df1 = pd.DataFrame([
             	[10, 20],
             	[50, 100],
             	[20, 40]],
             	columns=["A", "B"]
             )
             
             # method 计算相似度的方法， 默认 pearson ,常用
             # 可选 {"pearson", "kendall", "spearman"}
             
             print(df1.corr(method="pearson"))
             """
             正相关
                  A    B
             A  1.0  1.0
             B  1.0  1.0
             """
             df2 = pd.DataFrame([
             	[10, 0],
             	[50, 100],
             	[20, -20]],
             	columns=["A", "B"]
             )
             
             print(df2.corr(method="pearson"))
             """
                       A         B
             A  1.000000  0.921551
             B  0.921551  1.000000
             """
             ```

             

  + **空值 (缺失值) 处理**

    1. 检测缺失值
       1. 使用 `DF_name.isnull()` 的方式判断, 如果是缺失值返回 True,否则返回 False (通常与 sum() 连用 `.isnull().sum()` 返回空值的数目) ***常用于 Series***

          ```python
          import pandas as pd
          
          df2 = pd.DataFrame([
          	[10, ],
          	[50, 100],
          	[20, -20]],
          	columns=["A", "B"]
          )
          
          # 检测缺失值
          print(df2.isnull())
          """
                 A      B
          0  False   True
          1  False  False
          2  False  False
          """
          print(df2.isnull().sum())
          """
          A    0
          B    1 1个缺失值
          dtype: int64
          """
          print(df2.notnull())
          print(df2.notnull().sum())
          """
                A      B
          0  True  False
          1  True   True
          2  True   True
          A    3
          B    2
          dtype: int64
          """
          ```

       2. `DF_name.notnull()` : 如果不是缺失值返回 True , 否则返回 False **常用于 *Series***

       3. `DF_name.info()` : **常用于 *DataFrame***

          ```python
          import pandas as pd
          
          df2 = pd.DataFrame([
          	[10, ],
          	[50, 100],
          	[20, -20]],
          	columns=["A", "B"]
          )
          
          print(df2.info())
          """
          <class 'pandas.core.frame.DataFrame'>
          RangeIndex: 3 entries, 0 to 2
          Data columns (total 2 columns):
           #   Column  Non-Null Count  Dtype  
          ---  ------  --------------  -----  
           0   A       3 non-null      int64  
           1   B       2 non-null      float64
          dtypes: float64(1), int64(1)
          memory usage: 176.0 bytes
          None
          """
          ```

    2. 处理缺失值

       1. 删除 : `DF_name.dropna(self, axis=0, how="any", thresh=None, subset=None, inplace=False)`

          + 参数

            | 参数        | 描述                                                         |
            | ----------- | ------------------------------------------------------------ |
            | **axis**    | **{0 or 'index', 1 or 'columns'}, default 0** **0** --> 删除行 , **1** --> 删除列 |
            | **how**     | **{'any', 'all'}, default 'any'**<br>&emsp;**any** --> 该行或列存在空值则删除<br>&emsp;**all** -->  该行或列全为空值则删除 |
            | **thresh**  | **int, optional**设定阈值，缺失值个数大于该阈值，整行(axis=0)或整列(axis=1)才会被删除 |
            | **subset**  | subset=[1,2]， 删除指定列（1,2）中包含缺失值的行             |
            | **inplace** | 默认为 False 不改变原数据 , 为 True 时改变其原数据           |

          + 实例

            ```python
            import pandas as pd
            
            df2 = pd.DataFrame([
            	[10, ],
            	[50, 100],
            	[20, -20]],
            	columns=["A", "B"]
            )
            
            # 处理缺失值
            df2.dropna(axis=0, how="any", inplace=True)
            print(df2)
            """
                A      B
            1  50  100.0
            2  20  -20.0
            """
            ```

            

       2. 填充 : `DF_name["计量填充"]/DF_name完全填充.fillna(self, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None,)`

          + 参数

            | 参数        | 描述                                                         |
            | ----------- | ------------------------------------------------------------ |
            | **value**   | **填充值** 与 method 只能同时存在一个                        |
            | **method**  | **{‘pad’, ‘ffill’,‘backfill’, ‘bfill’, None}, default None**<br>&emsp;**pad/ffill**：用**前一个**非缺失值去填充该缺失值<br>&emsp;**backfill/bfill**：用***\*下一个\****非缺失值填充该缺失值<br>&emsp;***\*None\****：指定一个值去替换缺失值（缺省默认这种方式） |
            | **axis**    | 修改填充方向                                                 |
            | **inplace** | True、False<br>&emsp;**True**：直接修改原对象<br>&emsp;**False**：创建一个副本，修改副本，原对象不变（缺省默认） |
            | **limit**   | limit参数：限制填充个数                                      |

       3. 插值法 : 在自变量和因变量之间的，建立一个模型（方程）新得数据输入模型---产生插值结果

          + **线性插值 interp1d ** : 自变量和因变量之间具有一次线性关系（y=ax+b） 多元一次

          + **多项式,非线性插值 lagrange ** : 拉格朗日 拟合的是一个多项式；自变量和因变量是线性关系和非线性关系都可以很好的拟合

          + 实例

            ```python
            from scipy.interpolate import interp1d  # 线性插值
            # 线性插值不能很好地拟合非线性问题
            from scipy.interpolate import lagrange
            # 拉格朗日 拟合的是一个多项式；自变量和因变量是线性关系和非线性关系都可以很好的拟合
            
            import numpy as np
            import pandas as pd
            
            x_data = np.array([1, 2, 3, 4, 5, 6, 7])
            y_data = np.array([3, 5, 7, 9, np.nan, np.nan, 15])  # 2x+1
            y_data2 = np.array([2, 8, 18,32, np.nan, np.nan, 98])  # 2* x^2
            
            df = pd.DataFrame(data={"A":x_data, "B":y_data})
            print(df)
            
            # b_nona = df["B"].notnull()
            # print(b_nona)
            # 取出非空值
            new_df = df.dropna(how='any', axis=0) # axis=0删除行
            
            # 插值的使用
            # 1、拟合方程(模型)
            linear = interp1d(new_df["A"], new_df["B"])
            # print("插值结果", linear([5,6]))  # 预测
            
            # lagrange 限制输入数据类型为数组
            lar = lagrange(new_df["A"].values, new_df["B"].values)
            print("插值结果", lar([5,6]), type(lar([5,6])))
            print('-'*50)
            # na_mask = df["B"].isnull()
            # new_x = df.loc[na_mask, "A"]  # 新的输入数据
            # print(new_x.values)
            # new_y = linear(new_x.values)  # 新的输出数据
            # df.loc[na_mask, "B"] = new_y
            #
            # print("插值后的结果\n", df)
            ```

            

  + **异常值处理**

    + 检测与处理异常值

      + 异常值是指数据中个别值的数值明显偏离其他的数值,有时也称为 **离群点**
      + 检测异常值 : 监测数据中是否有录入错误以及不合理的数据

    + **具体业务法**

      + 根据对业务的理解，制订一个合理的范围,超出此范围则为异常值

    + **3 σ(sigma)原则**

      + 又称为 **拉依达法则**，假设数据属于正态分布数据,返回不属于正态分布的数据 *仅适用于对正态或近似正态分布的样本数据进行处理*
      + 该法则就是先假设一组检测数据只含有随机误差，对原始数据进行计算处理得到标准差，然后按一定的概率确定一个区间，认 为误差超过这个区间的就属于异常值。
      + 数据的数值分布几乎全部集中在区间(μ-3σ,μ+3σ)内，超出这个范围的 数据仅占不到 0.3%。故根据小概率原理，可以认为超出 3σ的部分数据为异常数 据。 表

    + **箱线图分析法**

      + 提供了识别异常值得一个标准，即异常值通常被定义为**小于 QL-1.5IQR** 或**大于 QU+1.5IQR** 的值
      + **QL** 称为下四分位数，表示全部观察值中有四分之一的数据取值比它小。
      + **QU** 称为上四分位数，表示全部观察值中有四分之一的数据取值比它大。
      + **IQR** 称为四分位数间距，是上四分位数 QU 与下四分位数 QL 之差，其间包含 了全部观察值的一半。
      + 四分位数给出了数据分布的中心、散布和形状的某种指示，具有一定的鲁棒 性，即 25%的数据可以变得任意远而不会很大地扰动四分位数，所以异常值通常 不能对这个标准施加影响。鉴于此，箱线图识别异常值的结果比较客观，因此在 识别异常值方面具有一定的优越性

    + 实例

      ```python
      import numpy as np
      import pandas as pd
      import matplotlib.pyplot as plt
      
      # 产生数据 (50 人的成绩) 生成异常值 [-10, 120]
      # arr = np.random.uniform(-10, 120, size=50)
      arr = np.random.uniform(-10, 0, size=3)
      # 生成 50 个数据
      arr = np.hstack((arr, np.arange(200, 400, 4)))
      # print(arr)
      df = pd.DataFrame({"成绩": arr})
      
      # print(df)
      # 异常值处理
      
      # 1. 具体业务法
      def get_normal_score(val):
      	low = 0
      	high = 100
      	return low <= val <= high
      
      # 在正常范围 返回 True 异常值返回 False
      mark1 = df["成绩"].transform(get_normal_score)
      final_df1 = df.loc[mark1, :]
      
      # 3 σ 法
      def three_sigma(val):
      	# 均值
      	mean_val = val.mean()
      	std_val = val.std()
      	low = mean_val - 3 * std_val
      	high = mean_val + 3 * std_val
      	return (low <= val) & (val <= high)
      
      mark2 = df["成绩"].transform(three_sigma)
      print(mark2.values, mark2.shape)
      final_df2 = df.loc[mark2, :]
      print(type(final_df2))
      
      # 箱线图分析法 (最小值、最大值、下四分位数(QL)、上四分位数(QU)、中位数)
      # IQR = QU - QL
      # low = QL - 1.5 * IQR
      # high = QU + 1.5 * IQR
      def box_analysis(val):
      	# 上下四分位数
      	QL, QU = val.quantile([0.25, 0.75])
      	IQR = QU - QL
      	low = QL - 1.5 * IQR
      	high = QU + 1.5 * IQR
      	return (low <= val) & (val <= high)
      
      mark3 = df["成绩"].transform(box_analysis)
      print(mark3.values, mark3.shape)
      final_df3 = df.loc[mark3, :]
      print(type(final_df3))
      print(final_df3)
      ```

      

