### Scrapy 框架初步

#### Scrapy 简介

+ Scrapy 是一个为了爬取网站数据、提取结构性数据而编写的应用框架
+ Scrapy 使用了 **Twisted 异步网络框架**处理网络通讯,可以加快下载速度,不需要去实现异步框架,包含了各种中间件接口.

#### Scrapy 架构图

##### Scrapy 架构图

+ **Scrapy Engine (引擎) ** : 负责 spider、ItemPipeline、Downloader、Scheduler 中间的通讯、信号、数据传递等
+ **Scheduler (调度器) ** : 负责接受引擎发送过来的 Requests 请求,并按照一定的方式进行整理排列,入队,当引擎需要时,交还给引擎
+ **Downloader (下载器) ** : 负责下载 Scrapy Engine (引擎) 发送的所有 Requests 请求,并将其获取到的 Responses 交还给 Scrapy Engine (引擎) , 由引擎交给 spider 来处理
+ **spider (爬虫) ** : 负责处理所有 Response,从中分析数据,获取 Item 字段需要的数据,并将需要跟进的 URL 提交给引擎,再次进入 Scheduler (调度器)
+ **Item Pipeline (管道) ** : 负责处理 spider 中获取到的 Item, 并进行后期处理 (详细分析、过滤、存储等)
+ **Downloader Middlewares (下载中间件) ** : 自定义拓展下载功能的组件
+ **SpiderMiddlewares (spider 中间件) ** : 自定义**拓展**和**操作**引擎和 **spider中间通信** 的功能组件 (比如进入 spider 的 Response 和 从 spider 出去的 Requests)

##### Scrapy 运作流程

1. 引擎询问 spider 需要处理的网站
2. spider 回应 引擎询问
3. 引擎向 spider 请求 处理网站 URL
4. spider 传递给引擎 网站 URL
5. 引擎将对网站的 request 请求 发送给调度器排序入队
6. 调度器将请求排序入队,返回处理好的 request 请求 给引擎
7. 引擎获取 调度器处理好的 request 请求
8. 引擎将request 请求发送给下载器
9. 下载器按照下载中间件的设置下载文件,如果下载成功返回数据给引擎;如果下载失败,将失败记录下来告诉调度器,之后重新下载
10.  引擎将下载好的东西经过下载中间件处理后 发送给 spider (responses 默认交给 def parse() 函数处理)
11.  spider 将引擎发给的数据进行处理, 返回两个结果 : 需要跟进的 URL 以及 获取到的 Item 数据
12.  引擎将 Item 发送给管道,将 需要跟进的 URL 发送给 调度器,然后继续循环获取数据,知道获取所有数据
13.  只有将调度器中不存在 任何 requests 后,整个程序停止 (对于失败的 URL , Scrapy 也会重新下载)

##### Scrapy 爬虫步骤

1. 新建项目 (Scrapy startproject project_name) : 新建一个爬虫项目
2. 明确目标 (编写 item.py) : 明确需要爬取的目标
3. 制作爬虫 (spiders/xxspider.py) : 制作爬虫并开始爬取网页
4. 存储内容 (pipelines.py) : 设置管道存储爬取内容

#### Scrapy 源码分析

##### spider

+ spider 类定义了如何爬取某个网站,包括 : 爬取动作(有无跟进链接)、提取内容(爬取 item)
+ **class Scrapy.spider** : 是最基本的类,所有编写爬虫必须继承这个类
+ 主要用到**函数**及**调用顺序**
  1. `__init__()` : 初始化爬虫命名以及 start_urls(开始 url) 列表
  2. `start_requests()` : 调用 `make_requests_from_url()` 生成 Requests 对象交给 Scrapy 下载并返回 response
  3. `parse()` : 解析 response, 并返回 item 或 Requests (需要指定回调函数).Item 传给 Item pipline 持久化, Requests 交给 Scrapy 下载,并通过指定的 回调函数处理 (默认为 parse()).一直进行循环,指导处理结束所有数据
+ 主要**属性**和**方法**
  1. `name` : 定义 spider 名字的字符串 (爬取 mywebsite.com , spider 常命名为 mywebsite)
  2. `allowed_domains` : 包含 spider 允许爬取的域名的列表,可选参数
  3. `start_urls` : 初始 URL 列表.没有特定 URL 时,spider 将从该列表开始爬取
  4. `start_requests(self)` : 返回一个可迭代对象 (iterable) .该对象包含了 spider 用于爬取的第一个 Request
  5. `parse(self, response)` : 当请求 URL 返回网页没有指定回调函数时,默认的 Request 对象回调函数.用来处理网页返回的 response , 以及生成 Item 或者 Request 对象

##### Parse() 方法的工作机制

+ Parse() 使用 **yield** 返回,因此常被用作生成器使用,Scrapy 会逐一获取 parse 方法生成的结果,并判断结果类型
  + 结果类型为 **request** : 加入爬取队列
  + 结果类型为 **item** : 使用 pipeline 处理,其他类型返回错误信息
  + 其他类型 : 返回错误信息
+ Parse() 工作步骤
  + Scrapy 获取到第一部分的 request 不会立刻发送,而是放入队列,继续从生成器获取
  + 取尽第一部分的 request, 在获取第二部分的 item, 取到 item 放入对应 pipeline 里处理
  + parse() 方法作为回调函数 (callback) 赋值给 Request,指定 parse() 方法来处理这些请求 `Scrapy.Request(url, callback=self.parse)`
  + Request 对象经过调度,执行生成 `Scrapy.http.response()` 的响应对象, 并返回给 parse() 方法,直到调度器中没有 Request (递归)
  + 取尽之后 parse() 工作结束, 引擎根据 队列和 pipelines 中的内容执行相应操作

##### Logging

+ Scrapy 提供 **日志(log)** 功能, 可以通过 logging 模块使用。可以修改配置文件 **settings.py** ,任意位置添加 以下两行

  ```python
  LOG_FILE = "text.log"
  LOG_LEVEL = "INFO"
  ```

+ Log levels : Scrapy 提供 5 层 logging 级别

  1. **CRITICAL** : 严重错误 (critical)
  2. **ERROR** : 一般错误 (regular errors)
  3. **WARNING** : 警告信息 (warning messages)
  4. **INFO** : 一般信息 (informational messages)
  5. **DEBUG** : 调试信息 (debugging messages)

+ logging 设置 : 通过 **settings.py** 内进行以下设置可以配置 logging

  + **LOG_ENABLED** : 默认: True, 启动 logging
  + **LOG_ENCODING** : 默认: "utf-8", logging 使用编码
  + **LOG_FILE** : 默认: None, 在当前目录创建 logging 输出文件的文件名
  + **LOG_LEVEL** : 默认: "DEBUG",log 最低级别
  + **LOG_STDOUT** : 默认: False,如果为 True,进程所有的标准输出(包括错误)将被重定向到 log 内

##### Robots 协议 (爬虫协议、机器人协议)

+ Robots 协议 (网络爬虫排除标准 Robots Exclusion Protocal) : 网站通过 robots 协议告诉搜索引擎网页是否可被抓取,以及抓取标准

+ scrapy 默认准守该协议, 将 **settings.py** 进行修改 : ROBOTSTXT_OBER = False

+ 虎扑新闻 robots : [https://www.hupu.com/robots.txt](https://www.hupu.com/robots.txt)

  ```
  User-agent: *
  Allow: /
  
  Sitemap: https://bbs.hupu.com/sitemap_index.xml
  Sitemap: https://bbs.hupu.com/sitemap/sitemap_boards.xml
  Sitemap: https://voice.hupu.com/sitemap_index.xml
  Sitemap: https://nba.hupu.com/players/index.xml
  ```

  

#### Scrapy 创建爬虫项目

##### Scrapy 使用	

1. 实现分页

   ```python
   class HupuSpiderSpider(scrapy.Spider):
       name = 'hupu_spider'
       # 二次请求过滤的域名, 可以注释
       # allowed_domains = ['www']
       start_urls = []
       for i in range(1, 101):
           base_url = f"http://voice.hupu.com/news?category=all&page={i}"
           start_urls.append(base_url)
   ```

2. 更改 **settings.py**

   1. 设置请求头

      ```python
      # Override the default request headers:
      DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36',
      }
      ```

   2. 允许 ROBOTS 协议

      ```python
      # Obey robots.txt rules
      ROBOTSTXT_OBEY = False
      ```

3. 在 **parse** 实现提取逻辑

   1. scrapy 中 response 对象的属性
      1. response.text : 字符串响应内容
      2. response.content : 二进制响应内容
      3. response.xpath() : xpath 提取数据,不需要 lxml 模块解析
         + 返回值为 *[<Selector xpath='' data=''>]* 
         + 提取数据方法
           1. .`.extract()` : 提取 selector 对象的 所有 data, 返回 list
           2. `.extract_first()` : 仅提取第一个数据 
   2. scrapy 发送二次请求
      + `yield scrapy.Request(url, callback=self.parse_detail,encoding='utf-8')`
      + 参数
        + **Request()** : 请求对象
        + **url** : 请求 request 对象对应的 url
        + **callback** : 请求scrapy下载好之后交给哪个方法处理下载好的响应

4. 数据保存

   1. 在 parse 方法内 `yield item`

      ```python
      def parse_detail(self, response):
          news_title = response.xpath('//h1[@class="headline"]/text()').extract_first()
          news_source = response.xpath('//span[@id="source_baidu"]/a/text()').extract_first()
          news_data = response.xpath('//span[@id="pubtime_baidu"]/text()').extract_first()
          news_content = response.xpath('string(//div[@class="artical-main-content"])').extract_first()
          item = HupuNewsItem()
          item['news_url'] = response.url
          item['news_title'] = news_title
          item['news_source'] = news_source
          item['news_data'] = news_data
          item['news_content'] = news_content
          yield item
      ```

   2. 更改 item 定义 : 使用 item.py 内重定义

      ```python
      class HupuNewsItem(scrapy.Item):
          # define the fields for your item here like:
          # name = scrapy.Field()
          news_url = scrapy.Field()
          news_title = scrapy.Field()
          news_source = scrapy.Field()
          news_data = scrapy.Field()
          news_content = scrapy.Field()
      ```

   3. 在 **pipelines.py** 内编写保存

      ```python
      class HupuNewsPipeline:
      
          def __init__(self):
              self.client = pymongo.MongoClient()
              self.db = self.client['hupu_news']
      
          def process_item(self, item, spider):
              self.db['NBA'].update({'news_url': item['news_url']}, {'$set': dict(item)}, True)
              print(item)
              return item
      ```

   4. 在 **setting.py** 内配置 pipelines 管道

      ```python
      # Configure item pipelines
      # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
      ITEM_PIPELINES = {
         'hupu_news.pipelines.HupuNewsPipeline': 300,
      }
      ```

5. 在 spiders 目录下 新建 **main.py** : 方便执行代码,只需要直接执行 main.py 即可执行爬虫

   ```python
   from scrapy import cmdline
   
   cmdline.execute('scrapy crawl company_spider'.split())
   ```

   

##### 创建项目基本命令操作

1. 安装 Scrapy : `pip install scrapy`
2. 创建项目 : `scrapy startproject 项目名称`
3. 新建一个 spider : `scrapy genspider 爬虫名称(name值) www` (www: 二次请求过滤域名默认值)
4. 第一个项目
5. 启动项目 : `scrapy crawl 爬虫名称(name 值)`

