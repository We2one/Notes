### Python 可视化模块 Matplotlib

#### 画图的基本步骤

##### 一、创建画布

+ 导包 : `import matplotlib.pyplot as plt` (绘制子图必须创建画布)

+ 创建画布 : `plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=Figure, clear=False, **kwargs)`

  + 参数

    | 参数          | 描述                                                         |
    | ------------- | ------------------------------------------------------------ |
    | **num**       | 图像编号或名称，数字为编号 ，字符串为名称                    |
    | **figsize**   | 指定figure (画布) 的宽和高，单位为英寸                       |
    | **dpi**       | 参数指定绘图对象的**分辨率**，即每英寸多少个像素，缺省值为80    1英寸等于2.5cm,A4纸是 21*30cm的纸张 |
    | **facecolor** | 背景颜色                                                     |
    | **edgecolor** | 边框颜色                                                     |
    | **frameon**   | 是否显示边框                                                 |

+ 应对不显示中文与显示中文后不显示正负号

  ```python
  # 默认不支持显示中文,需要将字体改为 雅黑
  plt.rcParams['font.sans-serif'] = 'SimHei'
  # 设置中文后不显示正负号,设置显示负号
  plt.rcParams['axes.unicode_minus'] = False
  ```

  

+ 实例

  ```python
  import matplotlib.pyplot as plt
  
  # 创建画布
  plt.figure()
  
  # 默认不支持显示中文,需要将字体改为 雅黑
  plt.rcParams['font.sans-serif'] = 'SimHei'
  # 设置中文后不显示正负号,设置显示负号
  plt.rcParams['axes.unicode_minus'] = False
  ```

  

##### 二、画图

+ 画图步骤

  1. 准备数据 (x,y 轴数据)

  2. 传入数据 : `plt.plot(*args, scalex=True, scaley=True, data=None, **kwargs)`

     1. `plt.plot()` 两种使用方式

        1. 单条线绘制 : `plot([x], y, [fmt], data=None, **kwargs)`
        2. 多条先一起绘制 : `plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)`

     2. 可选参数 `[fmt]` : 可选参数`[fmt]` 是一个字符串来定义图的基本属性如：**颜色（`color`）**，**点型（`marker`）**，**线型（`linestyle`）**，

        + **fmt** 形式
          
     + 具体形式 `fmt = '[color][marker][line]'`
       
     + 两种接收参数方式
       
       + fmt**接收的是每个属性的单个字母缩写**，例如：`plot(x, y, 'bo-')` # 蓝色圆点实线
       
       + 若属性用的是全名则不能用`fmt`参数来组合赋值,应该用关键字参数对单个属性赋值
       
            ```python
            plot(x,y2,color='green', marker='o', linestyle='dashed', linewidth=1, markersize=6)
         ```
       
     + 常见的颜色参数 :**colors** (也可以对关键字参数`color`赋十六进制的RGB字符串如 `color='#900302'`)
       
          | 参数值 | 描述             |
          | ------ | ---------------- |
          | **b**  | **蓝** blue      |
          | **g**  | **绿** green     |
          | **r**  | **红** red       |
          | **c**  | **蓝绿** cyan    |
          | **m**  | **洋红** magenta |
          | **y**  | **黄** yellow    |
          | **k**  | **黑** black     |
       | **w**  | **白** white     |
       
       
       
     + 点型参数 : **Markers** (用关键字参数对单个属性赋值，如：`marker='+'`这个只有简写，英文描述不被识别)
       
          | 参数值 | 描述                                 |
          | ------ | ------------------------------------ |
          | **.**  | **点标记** point marker              |
          | **,**  | **像素标记** pixel marker            |
          | **o**  | **圆圈标记** circle marker           |
          | **v**  | **下三角标记** triangle_down marker  |
          | **^**  | **上三角标记** triangle_up marker    |
          | **<**  | **左三角标记** triangle_left marker  |
          | **>**  | **右三角标记** triangle_right marker |
          | **1**  | **向下标记** tri_down marker         |
          | **2**  | **向上标记** tri_up marker           |
          | **3**  | **向左标记** tri_left marker         |
          | **4**  | **向右标记** tri_right marker        |
          | **s**  | **方块标记** square marker           |
          | **p**  | **五边形标记** pentagon marker       |
          | *****  | **星花*标记** star marker            |
          | **h**  | **六边形标记1** hexagon1 marker      |
          | **H**  | **六边形标记2** hexagon2 marker      |
          | **+**  | **加号标记** plus marker             |
          | **x**  | **x标记** x marker                   |
          | **D**  | **方菱形标记** diamond marker        |
          | **d**  | **瘦菱形标记** thin_diamond marker   |
          | **\|** | **竖线标记** vline marker            |
       | **_**  | **下划线标记** hline marker          |
       
       
       
     + 线型参数 : **Line Style** (用关键字参数对单个属性赋值，如：`linestyle='-'`)
       
          | 参数值 | 描述                           |
          | ------ | ------------------------------ |
          | **_**  | solid line style **实线**      |
          | **__** | dashed line style **虚线**     |
          | **_.** | dash-dot line style **点画线** |
       | **:**  | dotted line style **点线**     |
       
          

  3. 添加 x, y 轴说明 : `plt.xlabel()` 与 `plt.ylabel`

     ```python
     plt.xlabel('日期')
     plt.ylabel('温度/℃')
     ```

  4. 设置 x,y 轴刻度,更改其原有刻度

     1. 显示 x 轴数字信息为 周日期显示 : `plt.xticks(rotation=旋转度数)`

        ```python
        plt.xticks(x_data, labels=["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日", ])
        ```

     2. 显示 y 周信息 ，改变其跨度 : `plt.yticks()`

        ```python
        plt.yticks(np.arange(-10, 41, 5))
        ```

  5. 增加点位上的显示信息 : `plt.text(x坐标, y坐标, "显示信息")` 在每个数据上显示其数值信息，使用 zip 对两轴数据压缩后进行显示

     ```python
     # 增加显示信息
     # plt.text(2, 9, "13")
     for x, y in zip(x_data, y_data):
     	plt.text(x, y+1, y)
     ```

  6. 增加图例，图例列表内数据与画图顺序一一对应 : `plt.legend(["第一条线表示信息", "第二条线表示信息"])`

     ```
     # 增加图例, 和画图顺序保持一致
     plt.legend(["北京", "上海"])
     ```

+ 实例

  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  
  # 默认不支持显示中文,需要将字体改为 雅黑
  plt.rcParams['font.sans-serif'] = 'SimHei'
  # 设置中文后不显示正负号,设置显示负号
  plt.rcParams['axes.unicode_minus'] = False
  
  # 创建画布
  plt.figure()
  
  # 画图
  # 1. 准备数据,x 轴数据, y 轴数据
  x_data = np.arange(1, 8)
  y_data = [10, 12, 9, 8, -4, 8, 9]
  y_data1 = [-10, -9, -8, 0, 8, 0, -4]
  
  plt.plot(x_data, y_data, marker='4')
  plt.plot(x_data, y_data1, marker="^")
  
  # x,y 轴说明
  plt.xlabel('日期')
  plt.ylabel('温度/℃')
  
  # 设置 x 轴刻度
  # 对其原有刻度信息，显示为字符串
  # plt.xticks(x_data, labels=["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日", ])
  plt.xticks(x_data[::2], labels=["星期一", "星期三", "星期五", "星期日", ])
  # 更改 y 轴刻度
  plt.yticks(np.arange(-10, 41, 5))
  
  # 增加显示信息
  # plt.text(2, 9, "13")
  for x, y in zip(x_data, y_data):
  	plt.text(x, y+1, y)
  
  # 增加图例, 和画图顺序保持一致
  plt.legend(["北京", "上海"])
  
  
  # 显示数据
  plt.title('天气预报')
  
  # 保存数据
  plt.savefig("天气预报.png")
  
  plt.show()
  
  ```

  

##### 三、显示数据

+ 修饰信息 (标题, x/y 轴设置)

  + 增加标题 `plt.title()`

  + 保存数据 (必须在显示图像之前,渲染之后)

    ```python
    # 保存数据
    plt.savefig("天气预报.png")
    ```

+ 显示数据 : `plt.show()`

#### 绘制子图

+ 绘制子图必须要创建画布

+ 绘制多个子图步骤

  1. 为准备绘制的每个子图分配空间 (`fig.add_subplot(图片占行数, 图片占列数, 第几个图片)` : 将画布分为多好航多少列，每一个图所占位置,在该位置内绘制该图)

     ```python
     import numpy as np
     import matplotlib.pyplot as plt
     
     # 子图的绘制必需窗间画布
     fig = plt.figure()
     
     # sin 函数 cos 函数
     
     fig.add_subplot(2, 2, 1)
     # 绘制第一个子图
     fig.add_subplot(2, 2, 2)
     # 绘制第二个子图
     fig.add_subplot(2, 2, 3)
     # 绘制第三个子图
     fig.add_subplot(2, 2, 4)
     # 绘制第四个子图
     ```

  2. 设置子图间间距 : `fig.subplots_adjust()` (**wspace** 调整子图之间的宽度 [0, 1] 之间的值 [0.5表示子图间宽度占子图宽度的 50%], **hspace** 调整子图之间的高度 [0, 1] 之间的值 [0.5表示子图间高度占子图高度的 50%] )

     ```python
     # 调整子图间间距
     # wspace 调整子图之间的宽度 [0, 1] 之间的值
     # hspace 调整子图之间的高度 [0, 1] 之间的值
     fig.subplots_adjust(wspace=1, hspace=0.5)
     ```

  3. 在准备的空间内绘制需要的图形

  4. 对绘制图形添加各种属性

+ 实例

  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  
  # 子图的绘制必需窗间画布
  fig = plt.figure()
  
  # 准备数据
  x_data = np.arange(-2*np.pi, 2, 0.1)
  sin_data = np.sin(x_data)
  cos_data = np.cos(x_data)
  
  # sin 函数 cos 函数
  fig.add_subplot(2, 2, 1)
  # 绘制第一个子图, 添加关于此子图的配制
  plt.plot(x_data, sin_data, marker='>')
  
  fig.add_subplot(2, 2, 2)
  # 绘制第二个子图, 添加关于此子图的配制
  plt.scatter(x_data, cos_data, marker='*')
  
  fig.add_subplot(2, 2, 3)
  # 绘制第三个子图, 添加关于此子图的配制
  plt.scatter(sin_data, cos_data)
  
  fig.add_subplot(2, 2, 4)
  # 绘制第四个子图, 添加关于此子图的配制
  plt.scatter(sin_data*2, cos_data*2)
  
  plt.show()
  ```

  

#### 折线图

+ 应用场景 : 随着某个因素 (时间) 的变化，因变量的变化趋势 
+ `plt.plot()`
+ 显示 网格线 : `plt.grid()`

#### 散点图

+ 应用场景 : 

  + 随着某个因素 (时间) 的变化，因变量的变化趋势  
  + 查看数据的分布	

+ `plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=cbook.deprecation._deprecated_parameter, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)`

  + 参数

    | 参数           | 描述                                                         |
    | -------------- | ------------------------------------------------------------ |
    | **x,y**        | 表示的是大小为(n,)的数组，也就是我们即将绘制散点图的数据点   |
    | **s**          | 一个实数或者是一个数组大小为(n,)，这个是一个可选的参数。     |
    | **c**          | 颜色，也是一个可选项。默认是蓝色'b',表示的是标记的颜色，或者可以是一个表示颜色的字符，或者是一个长度为n的表示颜色的序列等等 |
    | **marker**     | 标记的样式，默认的是'o'                                      |
    | **cmap**       | Colormap实体或者是一个colormap的名字，cmap仅仅当c是一个浮点数数组的时候才使用。如果没有申明就是image.cmap |
    | **norm**       | Normalize实体来将数据亮度转化到0-1之间，也是只有c是一个浮点数的数组的时候才使用。如果没有申明，就是默认为colors.Normalize。 |
    | **vmin、vmax** | 实数，当norm存在的时候忽略。用来进行亮度数据的归一化         |
    | **alpha**      | 实数，0-1之间 (阿尔法值)                                     |
    | **linewidths** | 标记点的长度。                                               |
    | **edgecolors** | 边缘颜色                                                     |
    | **facecolor**  | 内部颜色                                                     |

    

#### 柱状图

+ 应用场景 : 少量对象在做对比分析时使用

+ 柱状图与直方图的异同

  + 相同点 : 使用柱子代表高度

  + 区别

    |      | 柱状图                         | 直方图(频数分布图)                                 |
    | ---- | ------------------------------ | -------------------------------------------------- |
    | 间隙 | 柱子之间是有间隙的             | 柱子之间间隙很小，只有当某一值为空时才会有很宽间隙 |
    | x 轴 | x 轴是一条线,描述分类变量      | x轴是分类变量,描述数值变量                         |
    | Y轴  | 柱形图的Y轴可以是数值          | 直方图的Y轴是频率                                  |
    | 描述 | 一般用来描述称名数据或顺序数据 | 一般用来描述等距数据或等比数据                     |

    

+ `plt.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)`

  + 参数

    | 参数       | 描述                                                         |
    | ---------- | ------------------------------------------------------------ |
    | **x**      | x坐标　int,float                                             |
    | **height** | 条形的高度                                                   |
    | **width**  | 线条的宽度 0~1，默认是0.8                                    |
    | **bottom** | 条形的起始位置 也就是y轴的起始坐标                           |
    | **align**  | 条形的中心位置 center”,"lege"边缘                            |
    | **data**   | 1. **color** :条形的颜色<br>2. **edgecolor** : 边框的颜色<br>3. **linewidth** : 边框的宽度<br>4. **tick_label** : 下标的标签 可以是元组类型的字符组合<br>5. **log** : y轴使用科学计算法表示<br>6. **orientation** : 竖直："vertical"，水平条："horizontal" |

    

#### 直方图

+ 直方图概念: 直方图是一种**统计报告图**，形式上也是一个个的长条形，但是直方图用**长条形的面积表示频数**，所以**长条形的高度表示频数组距频数/组距**，**宽度表示组距**，其长度和宽度均有意义。当宽度相同时，一般就用长条形长度表示频数。

+ `plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, *, data=None, **kwargs)`

  + 参数

    | 参数         | 描述                                                         |
    | ------------ | ------------------------------------------------------------ |
    | **x**        | **必选参数**,绘图数据                                        |
    | **bins**     | 划分间隔，可以采用 **整数**来指定**间隔的数量**，然后由程序由间隔的数量来确定每一个间隔的范围，也可以通过**列表**来直接**指定间隔的范围** |
    | **range**    | **可选**,全局间隔(min, max)，tuple 类型 **如果bins为列表形式，则range对其无影响** |
    | **density**  | **True** : 频率直方图<br>**False** : 频数直方图,显示的是**频数统计结果** |
    | **color**    | 更换直方图颜色                                               |
    | **histtype** | 可选{'bar', 'barstacked', 'step', 'stepfilled'}之一，默认为bar，推荐使用默认配置，step使用的是梯状，stepfilled则会对梯状内部进行填充，效果与bar类似 |
    | **align**    | 可选{'left', 'mid', 'right'}之一，默认为'mid'，控制柱状图的水平分布，left或者right，会有部分空白区域，推荐使用默认 |
    | **log**      | bool，默认False,即y坐标轴是否选择指数刻度                    |
    | **stacked**  | bool，默认为False，是否为堆积状图                            |
    
    

