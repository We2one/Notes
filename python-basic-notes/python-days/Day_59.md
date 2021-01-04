### Scrapy 中间件

#### Scrapy 中间件

+ 中间件是 Scrapy 的核心理念.使用中间件可以对爬虫**请求发起前**与**请求返回后**对数据进行定制化修改,从而适应不同情况的爬虫
+ scrapy 中间件:
  1. 爬虫中间件
  2. 下载中间件
+ Scrapy 框架目录中, 存在 **middlewares.py** 文件(中间件文件)
+ Scrapy 框架中使用 selenium:
  1. 在 **middlewares.py** 文件中找到项目下载的中间件类的 **process_request()** 方法
  2. **process_request()** 方法 : 需要填写使用 selenium 的内容
  3. 在 **settings.py** 文件中进行配置使用下载中间件
     1. **spider_MIDDLEWARES (爬虫中间件) **
     2. **DOWNLOADER_MIDDLEWARES (下载中间件) ** : 配置使用即可 (取消注释)

#### Scrapy 发送 post 请求 

+ 请求方法主要有 get 和 post 两种

  1. **GET 请求** : **yield Scrapy.Request** 对象完成
  2. **POST 请求** : **yield Scrapy.FormRequest** 对象

+ **Scrapy.FormRequest** 语法

  ```python
  Scrapy.FormRequest{
      Url, # post 请求的 url
      Data, # post 请求的请求参数
      Callback, # 处理请求的返回内容的回调函数
  }
  ```

  

#### Scrapy 自定义文件和图片下载类

+ Scrapy 提供两个 item Pipeline 专门用于下载文件和图片

  1. **FilesPipeline** 
  2. **ImagesPipeline**

+ 使用步骤

  1. 在配置文件 中的 pipelines 配置这两个类

     ```python
     # 图片
     ITEM_PIPELINES = {
     'Scrapy.pipelines.files.Images.ImagesPipeline': 1,
     }
     # 文件
     ITEM_PIPELINES = {'Scrapy.pipelines.files.FilesPipeline': 1,
     }
     ```

     

  2. 在配置文件 **settings.py** 中,使用 **FILE_STORE** 指定文件中的下载目录

     ```python
     FILES_STORE = './Image/'
     ```

  3. 在spider 解析一个包含文件下载链接的页面时,将所有需要的 url 地址收集到一个列表,赋值给 item 的 file_url 字段 (`item['file_urls']`).FilePipeline 在处理每一项 item 时,会读取 `item['file_urls']`,对其中每一个 url 进行下载

  4. 对于 ImagePipelines 还可以在 **settings.py** 内设置生成图片信息

     1. 为图片生成缩略图和大图,这样就会有三张下载图片 (原图、缩略图、大图)

        ```python
        IMAGES_THUMBS = {
        	'small': (50, 50),
        	'big': (270, 270),
        }
        ```

        

     2. 过滤尺寸过小的图片

        ```python
        IMAGES_MIN_WIDTH = 110
        IMAGES_MIN_HEIGHT = 110
        ```

##### 文件下载

 1. 在 spider 中提取 文件的链接

    ```python
    import scrapy
    from ..mysettings import custom_settings
    from ..items import DowmMatplotlibItem
    from scrapy.linkextractors import LinkExtractor
    
    
    class MatplotlibSpiderSpider(scrapy.Spider):
        name = 'matplotlib_spider'
        # allowed_domains = ['www']
        custom_settings = custom_settings
        start_urls = ['https://matplotlib.org/examples/index.html']
    
        def parse(self, response):
            le = LinkExtractor(restrict_xpaths=['//div[@class="toctree-wrapper compound"]/ul/li/ul'])
            links = le.extract_links(response)
    
            for link in links:
                yield scrapy.Request(link.url, callback=self.parse_detail, encoding='utf-8')
    
        def parse_detail(self, response):
            # print(response)
            # 提取下载链接
            url = response.xpath('//a[@class="reference external"]/@href').extract_first()
            # print(url)
            # urljoin:可以将相对url变成绝对url
            new_url = response.urljoin(url)
            # print(new_url)
            item = DowmMatplotlibItem()
            # 下载链接：类型是list
            # 只需要将下载链接放到这个属性位置，就可以自动下载
            item['file_urls'] = [new_url]
            yield item
    ```

2. 更改 **items.py**

   ```python
   import scrapy
   
   
   class DowmMatplotlibItem(scrapy.Item):
       # define the fields for your item here like:
       # name = scrapy.Field()
       file_urls = scrapy.Field()
       files = scrapy.Field()
       # pass
   ```

3. 配置 item 管道 : **settings.py**

   ```python
   'ITEM_PIPELINES': {
   	   'dowm_matplotlib.pipelines.DowmMatplotlibPipeline': 300,
   	},
   ```

   

4. 配置文件存储位置 : **settings.py**

   ```python
   'FILES_STORE': 'files',
   ```

5. 文件下载时更改文件名 : **pipelines.py**

   ```python
   from itemadapter import ItemAdapter
   from scrapy.pipelines.files import FilesPipeline
   
   
   class DowmMatplotlibPipeline(FilesPipeline):
   
       def file_path(self, request, response=None, info=None, *, item=None):
           url = request.url
           filename = url.split('/')[-1]
           dirname = url.split('/')[-2]
           return f'{dirname}/{filename}'
   ```

##### 图片下载

1. 修改 **mysettings.py** 作为下载图片配置

   ```python
   
   custom_settings = {
   	'ROBOTSTXT_OBEY': False,
   	# 'COOKIES_ENABLED': False,
   	'DEFAULT_REQUEST_HEADERS': {
   		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   		'Accept-Language': 'en',
   		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
   		              'Chrome/86.0.4240.111 Safari/537.36 ',
   	},
   	# 'DOWNLOADER_MIDDLEWARES': {
   	#    'down_img.middlewares.DownImgDownloaderMiddleware': 543,
   	# },
   	'ITEM_PIPELINES': {
   		'scrapy.pipelines.images.ImagesPipeline': 300,
   	},
   	# 文件下载位置
   	# 'FILES_STORE': 'files',
   	# 图片下载配置
   	'IMAGES_STORE': 'images',
   	'IMAGES_THUMBS': {
   		'big': (300, 300),
   		'small': (100, 100)
   	}
   
   	# 日志配置
   	# 'LOG_ENABLED':'True',#开启日志记录
   	# 'LOG_ENCODING':'utf-8',#日志的编码
   	# 'LOG_FILE':'hupu.log',#日志文件的保存文件名
   	# 'LOG_LEVEL':'DEBUG',#日志级别
   
   }
   ```

   

2. 编写代码 ,返回 item 

   ```python
   import scrapy
   from ..mysettings import custom_settings
   
   
   class ImgSpiderSpider(scrapy.Spider):
       name = 'img_spider'
       # allowed_domains = ['www']
       start_urls = []
       custom_settings = custom_settings
       for i in range(0, 180, 30):
           base_url = f"http://lcoc.top/bizhi/api.php?cid=360new&start={i}&count=30"
           start_urls.append(base_url)
   
       def parse(self, response):
           # for data in response.json()['data']:
           #     print(data)
           item = {}
           item['image_urls'] = [data['url'] for data in response.json()['data']]
           yield item
   ```

   

#### Scrapy 传入 cookies

1. 在 **settings.py** 中设置 : `COOKIES_ENABLED = False`

2. 传入 headers 以及 cookies

   ```python
   DEFAULT_REQUEST_HEADERS = {
   	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   	'Accept-Language': 'en',
   	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
   	              'Chrome/86.0.4240.111 Safari/537.36 ',
   	'Cookie': 'bid=CoeRTKFpiwM; ct=y; viewed="26829016"; gr_user_id=088ced06-085b-4aae-a412-332678552bf7; '
   	          '_vwo_uuid_v2=D243AD866FE90C1D85F50A705C208AEA8|f2724fa9e3985fc77b217e280acee6a9; ll="108288"; '
   	          'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=1bd6cff7-f857-4e8b-bf9f-dd30f84d06c2; '
   	          'gr_cs1_1bd6cff7-f857-4e8b-bf9f-dd30f84d06c2=user_id%3A0; '
   	          'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_1bd6cff7-f857-4e8b-bf9f-dd30f84d06c2=true; '
   	          '__utma=30149280.1254049736.1604713689.1604970054.1605579398.7; __utmc=30149280; '
   	          '__utmz=30149280.1605579398.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_douban=1; '
   	          '__utma=81379588.1902083457.1604715878.1604729806.1605579398.3; __utmc=81379588; '
   	          '__utmz=81379588.1605579398.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; '
   	          '_pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1605579400%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl'
   	          '%3D_hHIPU6Eexl9EzuwI4EfR2r-gzFYrVPvEUxfHpRNNWUSmYzOu7B-Fda29exu2mEo%26wd%3D%26eqid'
   	          '%3Dc96ea70100058f68000000035fb33275%22%5D; _pk_ses.100001.3ac3=*; '
   	          'Hm_lvt_cfafef0aa0076ffb1a7838fd772f844d=1605579416; '
   	          'Hm_lpvt_cfafef0aa0076ffb1a7838fd772f844d=1605579416; _pk_id.100001.3ac', 
   }
   ```

####  自定义 settings

+ 自定义 **my_settings.py**

  ```python
  import random
  
  custom_settings = {
  	'ROBOTSTXT_OBEY': False,
  	'COOKIES_ENABLED': False,
  	'DEFAULT_REQUEST_HEADERS': {
  	  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  	  'Accept-Language': 'en',
  	  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
  	                'Chrome/86.0.4240.111 Safari/537.36 ',
  	  'Cookie': 'UM_distinctid=175d009d1191cf-046fe260b1b903-303464-144000-175d009d11b599; '
  	            'PHPSESSID=ghb6s0hpk06emn97trd8e3ga60; Hm_lvt_2b65b835db5cae63ad487fd29631b1c7=1605513104,1605592827; '
  	            'Hm_lpvt_2b65b835db5cae63ad487fd29631b1c7=1605592827; '
  	            'CNZZDATA1000267376=2018095290-1605512919-http%253A%252F%252Fwww.iltaw.com%252F%7C1605591653 ',
  	},
  	# 'DOWNLOADER_MIDDLEWARES' : {
  	#    'animal_word.my_settings.Proxy_Middle': 543,
  	# },
  	# ITEM_PIPELINES = {
  	#    'animal_word.pipelines.AnimalWordPipeline': 300,
  	# }
  
  	# 日志配置
  	# 'LOG_ENABLED':'True',#开启日志记录
  	# 'LOG_ENCODING':'utf-8',#日志的编码
  	# 'LOG_FILE':'hupu.log',#日志文件的保存文件名
  	# 'LOG_LEVEL':'DEBUG',#日志级别
  
  }
  
  
  class Proxy_Middle(object):
  
  	def __init__(self):
  		self.proxy_list = [
              '117.45.150.13:4275',
              '180.104.215.0:4258',
              '114.227.104.186:4275',
  		]
  		self.USER_AGENT = [
  			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
              "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
              "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
              "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
              "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
              "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
              "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
              "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
              "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
              "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
              "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
          ]
  
  	def process_request(self, request, spider):
  
  		ip = random.choice(self.proxy_list)
  		request.meta['proxy'] = 'http://' + ip
  
  		# 设置随机请求头
  
  		user_agent = random.choice(self.USER_AGENT)
  		request.headers.setdefault('user-agent', user_agent)
  ```

+ 在 spider 中调用 简便配置 : `from ..mysettings import custom_settings`

  ```python
  custom_settings = custom_settings
  ```

  