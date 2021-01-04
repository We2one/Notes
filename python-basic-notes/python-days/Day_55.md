### 验证码高级和破解加密(一)

#### 滑块验证码破解

##### 使用的技术

1. selenium + Chrome 浏览器完成自动登录
2. 使用 **ActionChains** 控制鼠标操作 (鼠标按住 -- 鼠标拖动 -- 鼠标释放)
   + 鼠标动作链 : `from selenium.webdriver.common.action_chains import ActionChains`
3. 使用物理知识 (加速度) 模拟人的拖动轨迹 (先加速后减速)
4. 使用 Pillow 库完成图像的缺失值计算

#### JS 加密

+ **加密** 的过程就是把 **明文** 变成 **密文** 的过程
+ **解密** 的过程就是把 **密文** 变成 **明文** 的过程
+ 网页数据加密有很多种: **JS加密**、**Base64加密**、**CSS加密**
+ **JS加密** 加密对象 AJAX

#### CSS 加密

+ 查看源码发现源码内字体为乱码或与页面上显示的文字不同 : 可能是二进制或者 CSS 加密

+ 从源码中**寻找字体链接**,取出字体链接

+ 代码下载字体链接文件

+ 使用 **fontcreator** 软件打开下载出来的字体文件，判断网页显示与字体文件中字体代码是否对应

+ 分析字体文件,生成 unicode 码对应文字表

+ 实例:

  ```python
  import io
  import re
  import time
  import requests
  from lxml import etree
  from fontTools.ttLib import TTFont
  
  def css_decode(page_content):
  	"""
  	CSS 字体样式解密
  	page_content: 原页面内容
  	return 新页面内容
  	"""
  	# 1. 从 page_content 中提取 css 链接
  	# print(page_content)
  	css_href = re.search(r'href="(//s3plus\.meituan\.net/.*?\.css)">', page_content).group(1)
  	# 2. 请求 css 链接,从响应中提取 woff 文件链接
  	css_url = "http:" + css_href
  	print(css_url)
  	css_content = requests.get(css_url).text
  	woff_href = re.findall(r',url\("(//s3plus\.meituan\.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/.*?\.woff)"', css_content)
  	data = {}
  	for woff_url in woff_href:
  		file_name = woff_url.split('/')[-1]
  		woff_content = requests.get('http:' + woff_url).content
  		with open(file_name, 'wb') as f:
  			f.write(woff_content)
  		font = TTFont(io.BytesIO(woff_content))
  		keys = font.getGlyphOrder()
  		values = list(
  			'1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工'
  			'服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安'
  			'广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养'
  			'卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精'
  			'屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医'
  			'正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成'
  			'云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙'
  			'恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡'
  			'厦府铺内侧元购前幢滨处向座下県凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本'
  			'单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦'
  			'字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错'
  			'没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做'
  			'排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找'
  			'些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞'
  			'片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕')
  		# print(keys, font)
  		# 3. 下载 woff
  		# print(len(keys[2:]), len(values))
  		for i, v in zip(keys[2:], values):
  			# print(i, v)
  			k = i[3:]
  			data[k] = v
  	print(data)
  	for k, v in data.items():
  		page_content = page_content.replace(f'&#x{k};', v)
  	return page_content
  
  def parse_page(page_content):
  	"""
  	提取数据
  	"""
  	tree = etree.HTML(page_content)
  	li_list = tree.xpath('//div[@id="shop-all-list"]/ul/li')
  	for li in li_list:
  		title = li.xpath('.//div[@class="tit"]//h4/text()')
  		print(title)
  		# 字体样式
  		comment_num_list = li.xpath('.//div[@class="comment"]/a[1]/b//text()')
  		comment_num = ''.join(comment_num_list)
  		print(comment_num)
  		# print(comment_num_list)
  
  def get_content(url):
  	headers = {
  		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
  		'Host': 'www.dianping.com',
  		'Cookie': 'fspop=test; cye=beijing; _lxsdk_cuid=175b4e35d85c8-0e591a964cdc8d-3b3d590a-1fa400-175b4e35d86c8; _lxsdk=175b4e35d85c8-0e591a964cdc8d-3b3d590a-1fa400-175b4e35d86c8; _hc.v=858d803b-f268-4c16-5828-4d6880711028.1605057601; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1605057622,1605058581; s_ViewType=10; cy=1; _lxsdk_s=175b4e35d89-cb6-059-b7a%7C%7C178; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1605065836',
  	}
  	response = requests.get(url, headers=headers)
  	# print(response.text)
  	# 对相应内容做一个css解密就可以了-
  	# 解密的过程就是使用字体文件替换其中特殊字体的过程。
  	time.sleep(5)
  	page_content = css_decode(response.text)
  	# print(page_content)
  	return page_content
  	# return response.text
  
  def main():
  	base_url = 'http://www.dianping.com/search/keyword/155/0_%E5%92%8C%E8%B0%90%E5%B9%BF%E5%9C%BA'
  	page_content = get_content(base_url)
  	parse_page(page_content)
  
  if __name__ == '__main__':
  	main()
  ```

  

#### Base 64 加密

##### Base 64 原理

+ **base 64** 原理: 先将源文件以标准字节 (byte) 为单位转化为二进制,一个字节占 8 位(bit),这样源文件就形成了每 8 个bit 一组的一串二进制,然后将这些二进制串以 base64 特有的规则 (每个字节占 6 个位)再转化为 base 64 格式的字符.

+ **重点** : 查看页面时发现有乱码问题, 寻找页面的 **字体链接**

  + 方法:
    1.  在 NetWork 内 查找 **font** 文件，文件后缀为 **.woff**,找到后下载 
    2.  使用 **fontcreator** 软件打开下载出来的字体文件，判断网页显示与字体文件中字体代码对应关系
    3.  编写代码解析,生成文字对应字典

+ 实例:

  ```python
  import re
  import io
  import time
  import base64
  import requests
  from lxml import etree
  from fontTools.ttLib import TTFont
  
  def base_decode(page_content):
  	font_base64 = re.search(r'base64,(.*?)\'\)', page_content, re.S).group(1)
  	font_content = base64.b64decode(font_base64)
  	font = TTFont(io.BytesIO(font_content))
  	with open('iconfont.woff', 'wb') as fp:
  		fp.write(font_content)
  	font.saveXML('font.xml')
  	# print(font.getGlyphOrder())
  	# print(font.getBestCmap())
  	res = {str(hex(k))[2:]: str(int(v[-2:])-1) for k, v in font.getBestCmap().items()}
  	# print(res)
  	# 替换文本中信息
  	for k, v in res.items():
  		page_content = page_content.replace(f'&#x{k};', v)
  	return page_content
  
  def get_content(url):
  	"""
  	发送请求获取响应内容
  	<link rel="icon" href="https://pages.anjukestatic.com/usersite/site/img/global/1/favicon.ico" type="image/ico">
  	"""
  	headers = {
  		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
  
  	}
  	response = requests.get(url, headers=headers)
  	page_content = base_decode(response.text)
  	return page_content
  
  def main():
  	base_url = 'https://bj.zu.anjuke.com/'
  	page_content = get_content(base_url)
  	# print(page_content)
  	tree = etree.HTML(page_content)
  	div_list = tree.xpath('//div[@class="zu-itemmod"]')
  	for div in div_list:
  		title = div.xpath('.//h3/a/b/text()')[0]
  		price = div.xpath('.//div[@class="zu-side"]/p//b/text()')[0]
  		print(title + "\t" + price)
  
  if __name__ == '__main__':
  
  	main()
  ```

  

