### Python 可视化模块 Matplotlib

#### 雷达图

+ 应用场景: 对一个对象从多个维度,多个方向进行描述

+ `plt.polar(theta, r, **kwargs)`

  + 参数

    | 参数      | 描述                                                         |
    | --------- | ------------------------------------------------------------ |
    | **theta** | `np.linspace(0, np.pi*2, n, endpoint=False)` 将 圆周分为 n 份 **之后需要 添加最后一个值为第一个值,作为闭合** |
    | **r**     | data 数据,以列表形式传入,**之后需要 添加最后一个值为第一个值,作为闭合** |

+ 实例

  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  
  angles = np.linspace(0, np.pi*2, 5, endpoint=False)
  
  data = [2, 3.5, 4, 4.5, 5]
  label = ["生存评分", "输出评分", "团战评分", "KDA", "发育评分"]
  label.append(label[0])
  
  # 组成数据集合
  # 生成 五个角度 的 度数
  angles = np.hstack((angles, angles[0:1]))
  print(angles)
  
  # 生成五个角度的数据
  data.append(data[0])
  print(data)
  plt.figure()
  
  # 默认不支持显示中文,需要将字体改为 雅黑
  plt.rcParams['font.sans-serif'] = 'SimHei'
  # 设置中文后不显示正负号,设置显示负号
  plt.rcParams['axes.unicode_minus'] = False
  
  plt.polar(angles, data)
  
  # 修改刻度
  plt.xticks(angles, label)
  
  plt.legend(["GGboy"], loc="lower right")
  
  plt.show()
  ```

  

#### 饼图

+ 绘制时不需要传入百分比数据,传入原始数据,会自动转换为百分比

+ `plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, normalize=None, data=None)`

  + 参数:

    | 参数              | 描述                                                         |
    | ----------------- | ------------------------------------------------------------ |
    | **x**             | **必选参数**,绘图数据                                        |
    | **labels**        | (每一块)饼图外侧显示的说明文字                               |
    | **explode**       | (每一块)离开中心距离,突出显示                                |
    | **colors**        | 饼图颜色                                                     |
    | **autopct**       | 控制饼图内百分比设置(没有用空格补齐)                         |
    | **shadow**        | 是否有阴影                                                   |
    | **labeldistance** | label绘制位置,相对于半径的比例, 如<1则绘制在饼图内侧         |
    | **startangle**    | 起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起 |
    | **radius**        | 控制饼图半径                                                 |
    | **counterclock**  | 是否让饼图按逆时针顺序呈现；                                 |
    | **wedgeprops**    | 设置饼图内外边界的属性，如边界线的粗细、颜色等；             |
    | **textprops**     | 设置饼图中文本的属性，如字体大小、颜色等；                   |
    | **center**        | 指定饼图的中心点位置，默认为原点                             |
    | **frame**         | 是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置； |

    

#### 箱线图

+ 应用场景: 查看数据的分布是否集中或对称,查看数据中是否有异常值

+ 计算四分位数 : `np.quantile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)`

  + 参数

    | 参数                | 描述                                                         |
    | ------------------- | ------------------------------------------------------------ |
    | **a**               | 数组,输入数组或可以转换为数组的对象。                        |
    | **q**               | 浮点数的array_like,要计算的分位数或分位数序列，必须在0到1之间（含0和1）<br>介于0-1的float，用来计算是几分位的参数，如四分之一位就是25，如要算两个位置的数就(25,75) |
    | **axis**            | 用于计算分位数的一个或多个轴。默认值为沿着数组的展平版本计算分位数 |
    | **out**             | 放置结果的备用输出数组。它的形状和缓冲区长度必须与预期的输出相同，但是（必要时）将强制转换（输出的）类型。 |
    | **overwrite_input** | 如果为True，则允许通过中间计算来修改输入数组*a*，以节省内存。在这种情况下，此功能完成后输入*a*的内容 是不确定的。 |
    | **interpolation**   | **{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}**<br>指定当所需分位数位于两个数据点之间时要使用的插值方法 ：`i < j`:<br>&emsp;+ **linear**：，其中 i 的索引的小数部分被 j 和包围<br>&emsp;+ **lower**: i<br>&emsp;+ **higher**: j<br>&emsp;+ **midpoint**: 中间点 `(i+j)/2`<br>&emsp;+ **nearest** : 最近值 `i`或`j`，以最近的一个为准。 |

  + 实例

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    
    arr = np.random.randint(1, 10, 10)
    print(arr)
    # arr = [7, 7, 6, 5, 2, 2, 8, 6, 4, 7]
    print(np.quantile(arr, (0.25, 0.50, 0.75)))
    """
    [3 6 3 8 9 7 5 3 7 8]
    [3.5  6.5  7.75]
    ```

    

+ `plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_ticks=True, autorange=False, zorder=None, *, data=None)`

  + 参数

    | 参数             | 描述                                                  |
    | ---------------- | ----------------------------------------------------- |
    | **x**            | 指定要绘制箱线图的数据                                |
    | **notch**        | 是否是凹口的形式展现箱线图，默认非凹口                |
    | **sym**          | 指定异常点的形状，默认为+号显示                       |
    | **vert**         | 是否需要将箱线图垂直摆放，默认垂直摆放                |
    | **whis**         | 指定上下须与上下四分位的距离，默认为1.5倍的四分位差； |
    | **positions**    | 指定箱线图的位置，默认为[0,1,2…]                      |
    | **width**        | 指定箱线图的宽度，默认为0.5                           |
    | **patch_artist** | 是否填充箱体的颜色                                    |
    | **meanline**     | 是否用线的形式表示均值，默认用点来表示                |
    | **showmeans**    | 是否显示均值，默认不显示                              |
    | **showcaps**     | 是否显示箱线图顶端和末端的两条线，默认显示            |
    | **showbox**      | 是否显示箱线图的箱体，默认显示                        |
    | **showfliers**   | 是否显示异常值，默认显示                              |
    | **boxprops**     | 设置箱体的属性，如边框色，填充色等                    |
    | **labels**       | 为箱线图添加标签，类似于图例的作用                    |
    | **filerprops**   | 设置异常值的属性，如异常点的形状、大小、填充色等      |
    | **medianprops**  | 设置中位数的属性，如线的类型、粗细等                  |
    | **meanprops**    | 设置均值的属性，如点的大小、颜色等                    |
    | **capprops**     | 设置箱线图顶端和末端线条的属性，如颜色、粗细等        |
    | **whiskerprops** | 设置须的属性，如颜色、粗细、线的类型等                |

    

