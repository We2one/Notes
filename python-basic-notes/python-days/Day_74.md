### Pyecharts

#### Pyecharts 绘图

##### 地图绘制 Geo

+ 实例

  ```python
  from pyecharts.charts import Geo
  import pyecharts.options as opts
  from pyecharts.globals import ChartType, SymbolType
  
  geo = (
  	Geo()
  		.add_schema(
  		maptype='china',
  		itemstyle_opts=opts.ItemStyleOpts(
  			color="#777776",
  			border_color="#222"
  		)
  	)
  		.add(
  		"",
  		# 显示点
  		[("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
  		type_=ChartType.EFFECT_SCATTER,
  		color="white",
  	)
  		.add(
  		# 显示线
  		"geo",
  		[("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
  		type_=ChartType.LINES,
  		# 显示蓝色行动箭头
  		effect_opts=opts.EffectOpts(
  			symbol=SymbolType.ARROW, symbol_size=6, color="blue"
  		),
  		linestyle_opts=opts.LineStyleOpts(curve=0.2),
  	)
  		.set_global_opts(
  		title_opts=opts.TitleOpts(
  			title="中国"
  		)
  	)
  		.render("china.html")
  )
  ```

##### 时间轴组件 TimeLine

+ 实例

  ```python
  """
  .--,       .--,
   ( (  \.---./  ) )
    '.__/o   o\__.'
       {=  ^  =}
        >  -  <
       /       \
      //       \\
     //|   .   |\\
     "'\       /'"_.-~^`'-.
        \  _  /--'         `
      ___)( )(___
     (((__) (__)))    高山仰止,景行行止.虽不能至,心向往之。
  """
  from pyecharts.charts import Geo, Timeline
  import pyecharts.options as opts
  from pyecharts.globals import ChartType, SymbolType
  t1 = Timeline()
  for i in range(2015, 2020):
  	geo = (
  
  		Geo()
  			.add_schema(
  			maptype='china',
  			itemstyle_opts=opts.ItemStyleOpts(
  				color="#777776",
  				border_color="#222"
  			)
  		)
  			.add(
  			"",
  			# 显示点
  			[("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
  			type_=ChartType.EFFECT_SCATTER,
  			color="white",
  		)
  			.add(
  			# 显示线
  			"geo",
  			[("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
  			type_=ChartType.LINES,
  			# 显示蓝色行动箭头
  			effect_opts=opts.EffectOpts(
  				symbol=SymbolType.ARROW, symbol_size=6, color="blue"
  			),
  			linestyle_opts=opts.LineStyleOpts(curve=0.2),
  		)
  			.set_global_opts(
  			title_opts=opts.TitleOpts(
  				title="中国"
  			),
  			visualmap_opts=opts.VisualMapOpts()
  		)
  	)
  	t1.add(geo, "{}年".format(i))
  
  t1.render("时间轴.html")
  
  ```

  

##### Map 地图

+ 实例

  ```python
  from pyecharts.charts import Map
  import pyecharts.options as opts
  from translate import Translator
  import pandas as pd
  
  trans = Translator(from_lang='chinese', to_lang="english")
  out = trans.translate("日本")
  print(out)
  data = pd.read_excel('../截至2月17日22时37分疫情数据.xlsx')
  # print(data)
  """
          城市             时间   死亡数    治愈数     疑似数     省份    确诊数
  0    China  截至2月17日22时37分  1772  11279  7264.0     亚洲  70642
  1    China  截至2月17日22时37分   105   1425  1563.0  今日增加值   2048
  2       湖北  截至2月17日22时37分  1696   6693     0.0     湖北  58182
  """
  mark = data["省份"] == data["城市"]
  data = data.loc[mark, ["省份", "确诊数"]]
  # print(data)
  """
        省份    确诊数
  2     湖北  58182
  20    广东   1322
  """
  # print(data["确诊数"].reset_index().values.tolist())
  data.drop_duplicates(subset=["省份"], inplace=True)
  
  china_map = (
  	Map()
  	.add(
  		series_name="xxx",
  		data_pair=data.values.tolist(),
  		maptype="china",
  		is_map_symbol_show=False
  	)
  	.set_global_opts(
  		# 视觉映射设置
  		visualmap_opts=opts.VisualMapOpts(
  			# 分段
  			is_piecewise=True,
  			pieces=[
  				{"max": 100, "label": "<100", "color": "#F0FFFF"},
  		        {"min": 100, "max": 500, "label": "100-500", "color": "	#5F9EA0"},
  		        {"min": 500, "max": 1000, "label": "500-1000", "color": "#00FFFF"},
  		        {"min": 1000, "max": 2000, "label": "1000-2000", "color": "#0000FF"},
  		        {"min": 2000, "max": 5000, "label": "2000-5000", "color": "#8A2BE2"},
  		        {"min": 5000, "max": 10000, "label": "5000-10000", "color": "#D2691E"},
                  {"min": 10000, "label": ">10000", "color": "#A52A2A"},
  			],
  		)
  	)
  	.render("一疫情分布图.html")
  )
  ```


##### 组合多图 Page()

+ 实例

  ```python
  from geo_map import t1
  from word_map import world_map
  # from map_img import china_map
  from pyecharts.charts import Page
  page = Page(layout=Page.DraggablePageLayout)
  
  page.add(t1)
  page.add(world_map)
  # page.add(china_map)
  page.render("组合.html")
  ```

  