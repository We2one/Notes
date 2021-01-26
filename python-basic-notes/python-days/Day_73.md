### Pyecharts

#### 认识 Pyecharts

+ Pyecharts 用于生成 echarts 图表的类库

#### Pyecharts 简单图例绘制

##### 全局配置项

+ 全局配置项可通过 `set_global_options` 方法设置
+ 主要设置内容 : 
  + **TitleOpts** : 标题配置项
  + **LegendOpts** : 图例配置项
  + **ToolboxOpts** : 工具箱配置项
  + **VisualMapOpts** : 视觉映射配置项
  + **TooltipOpts** : 提示配置项
  + **DataZoomOpts** : 区域缩放配置项

##### 系列配置项

+ 可以使用 `set_series_options` 方法设置

+ 主要用来配置**字体**、**颜色**、**线条灯**具体的参数。

+ **Label_Opts**

  + **formatter: "{b}: {c}"** 设置 : 标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板和回调函数均支持 \n 换行

  + 模板变量: *{a}、{b}、{c}、{d}* 分别代表系列名、数据名、数据值等

  + 在 **trigger** 为 axis 时,有多个系列的数据,可以通过{a0}、{a1}、{a2} 等索引方式表示系列索引

  + 不同图表下  *{a}、{b}、{c}、{d}* 有不同的含义:

    + **折线 (区域) 图、柱状 (条形) 图、K 线图** : 

      | 变量    | 描述     |
      | ------- | -------- |
      | **{a}** | 系列名称 |
      | **{b}** | 类目值   |
      | **{c}** | 数值     |
      | **{d}** | 无       |

    + **散点 (气泡) 图**

      | 变量    | 描述     |
      | ------- | -------- |
      | **{a}** | 系列名称 |
      | **{b}** | 数据名称 |
      | **{c}** | 数值数组 |
      | **{d}** | 无       |

    + **地图**

      | 变量    | 描述     |
      | ------- | -------- |
      | **{a}** | 系列名称 |
      | **{b}** | 区域名称 |
      | **{c}** | 合并数值 |
      | **{d}** | 无       |

    + **饼图、仪表图、漏斗图**

      | 变量    | 描述       |
      | ------- | ---------- |
      | **{a}** | 系列名称   |
      | **{b}** | 数据项名称 |
      | **{c}** | 数值       |
      | **{d}** | 百分比     |

      

##### 数据格式

+ Pyecharts 本质上在做的事情就是将 Echarts 的配置项由 Python dict 序列化为 JSON 格式，所以 Pyecharts 支持什么格式的数据类型取决于 JSON 支持什么数据类型。
+ 可以使用 Series.tolist()进行快速转换

#### 图表绘制

+ **链式调用**
+ **先定义再增加信息**

##### 柱状图 Bar

+ 实例

  ```python
  from pyecharts.charts import Bar
  import pyecharts.options as opts
  
  b = (
  	Bar()
  	.add_xaxis([
  		"名字很长的X轴标签1",
  		"名字很长的X轴标签2",
  		"名字很长的X轴标签3",
  		"名字很长的X轴标签4",
  		"名字很长的X轴标签5",
  		"名字很长的X轴标签6",
  	])
  	.add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
  	.add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
  	.set_global_opts(
  		xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
  		title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
  	)
  	.set_series_opts(
  
  	)
  	.render("bar_01.html")
  
  )
  ```

##### 饼图 Pie

+ 实例

  ```python
  import pandas as pd
  from pyecharts.charts import Pie
  from pyecharts import options as opts
  
  data = pd.read_excel('./Python地区分校人数.xlsx')
  
  pie = (
      Pie()
      .add(series_name="地区",
           data_pair=data.values,  # 传入数据
           radius=['50%', '75%'],  # 内外径
           rosetype='radius',  # 设置玫瑰图类型
           )
      # 添加全局配置
      .set_global_opts(
          title_opts=opts.TitleOpts(
              title="Python地区人数占比图"
          ),
          legend_opts=opts.LegendOpts(
              is_show=True,
          )
      )
      .set_series_opts(
          # 设置显示样式
          label_opts=opts.LabelOpts(
              is_show=True,
              formatter="{b}:{c}"
          )
      )
      .render('python地区分布人数占比.html')
  )
  ```

##### 折线图 Line

+ 实例

  ```python
  import numpy as np
  from pyecharts.charts import Line
  from pyecharts import options as opt
  
  x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
  y_data = np.random.random(7)*100000
  # print(y_data)
  
  line = (
  	Line()
  	.add_xaxis(x_data)
  	.add_yaxis(series_name="收益", y_axis=y_data)
  	.set_series_opts(
  
  	)
  	.render("每日收益.html")
  )
  ```

##### 组合图绘制

+ 步骤

  1. 创建网格 : `grid = Grid()`
  2. 添加子图 : `grid.add(子图类型, 子图设置)`

+ 实例

  ```python
  import pandas as pd
  import numpy as np
  import pyecharts.options as opts
  from pyecharts.charts import Line, Pie
  from pyecharts.charts import Grid
  
  data = pd.read_excel('../Python地区分校人数.xlsx')
  
  pie = (
  	Pie()
  		.add(series_name="地区",
  	         data_pair=data.values,  # 传入数据
  	         radius=['50%', '75%'],  # 内外径
  	         rosetype='radius',  # 设置玫瑰图类型
  	         )
  		# 添加全局配置
  		.set_global_opts(
  		title_opts=opts.TitleOpts(
  			title="Python地区人数占比图"
  		),
  		legend_opts=opts.LegendOpts(
  			is_show=True,
  			pos_left="15%",
  			pos_right="40%"
  		),
  		yaxis_opts=opts.AxisOpts(
  			position="right"
  		)
  	)
  		.set_series_opts(
  		label_opts=opts.LabelOpts(
  			is_show=True,
  			formatter="{b}:{c}"
  		)
  	)
  	# .render('python地区分布人数占比.html')
  )
  
  x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
  y_data = np.random.random(7) * 100000
  line = (
  	Line()
  		.add_xaxis(x_data)
  		.add_yaxis(series_name="收益", y_axis=y_data)
  		.set_series_opts(
  
  	)
  		.set_global_opts(
  		yaxis_opts=opts.AxisOpts(
  			position="left"
  		),
  		legend_opts=opts.LegendOpts(
  			pos_left="15%",
  			pos_right="40%"
  		)
  	)
  	# .render("每日收益.html")
  )
  
  grid = Grid(
  	init_opts=opts.InitOpts(
  		width="1400px",
  		height="500px"
  	)
  )
  
  grid.add(
  	line,
  	grid_opts=opts.GridOpts(
  		pos_left="80%",
  		pos_right="0%",
  	),
  	is_control_axis_index=True
  )
  grid.add(
  	pie,
  	grid_opts=opts.GridOpts(
  		pos_left="0%",
  		pos_right="40%",
  	),
  	is_control_axis_index=True
  )
  grid.render("组合图.html")
  
  ```

  