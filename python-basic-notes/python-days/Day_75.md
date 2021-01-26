### Pyecharts

#### Pyecharts 绘图

#### 词云图

+ 实例

  ```python
  from collections import Counter
  from PIL import Image
  import pandas as pd
  import numpy as np
  import jieba
  import os
  from pyecharts import options as opts
  from pyecharts.charts import WordCloud
  
  with open('./resource/ham_5000.utf8', encoding='utf-8') as f:
  	ham_email = f.readlines()
  # print(ham_email) 5000
  
  with open('./resource/spam_5000.utf8', encoding='utf-8') as f:
  	spam_email = f.readlines()
  # print(spam_email) 5000
  
  # 合并文件
  total_text = ham_email + spam_email
  # print(len(total_text)) 10000
  
  cnt = Counter(jieba.cut(''.join(ham_email).replace(' ', ''), cut_all=False))
  # print([(i, j) for i, j in cnt.items()])
  cnt_list = [(i, j) for i, j in cnt.items()]
  c = (
      WordCloud()
      .add("", cnt_list, word_size_range=[12, 55], textstyle_opts=opts.TextStyleOpts(font_family="cursive"), shape="circle", mask_image="F:/PPT资源/进阶：中国风素材/素材 (92).png")
      .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"), tooltip_opts=opts.TooltipOpts(is_show=True),)
      .render("wordcloud_custom_mask_image.html")
  )
  ```

  