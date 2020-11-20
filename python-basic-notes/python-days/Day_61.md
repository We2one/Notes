### Scrapy-redis 分布式

#### Python 邮件监控

##### SMTP 简介

+ **SMTP** (Simple Mail Transfer Protocol : 简单邮件传输协议) : 一组用于由原地址到目的地址传送邮件的规则,由它来控制新建的中转方式

+ python 的 smtplib 提供了一种很方便的途径发送电子邮件,对 smtp 进行了简单的封装

  ```python
  import smtplib
  smtpObj = smtplib.SMTP([host [, port [, local_hostname]]])
  ```

  + 参数说明
    1. **host** : SMTP 服务器主机,可以指定主机的 ip 地址或者域名 (可选参数)
    2. **port** : 如果提供了 host 需要指定 SMTP 服务使用的端口号, 一般端口号为 25
    3. **local_hostname** : 如果 SMTP 在本机上,可以指定服务器地址为 localhost

+ Python SMTP 使用 **sendmail** 方法发送邮件,语法格式:

  ```python
  SMTP.sendmail(from_addr, to_addrs, msg [, mail_options, rcpt_options])
  ```

  + 参数说明
    1. **from_addr** : 邮件发送者地址
    2. **to_addrs** : 字符串列表,邮件发送地址
    3. **msg** : 发送消息,字符串 (表示邮件)
       + msg 格式 为 smtp 定义固定格式
         1. 标题
         2. 发信人
         3. 收件人
         4. 邮件内容
         5. 附件

##### 邮件监控五个步骤

+ 五个步骤

  ```python
  # 导入邮件包
  import smtplib
  # 创建邮件对象
  smtpobj = smtplib.SMTP()
  # 连接服务器
  smtpobj.connect()
  # 登录操作
  smtpobj.login()
  # 发送邮件
  smtpobj.sendmail()
  # 退出操作
  smtpobj.quit()
  ```

  1. 连接服务器 : `smtp.connect(self, host='localhost', port=0, source_address=None)`
  2. 登录操作 : `smtplib.login(self, user, password, *, initial_response_ok=True)`
  3. 发送邮件 : `smtplib.sendmail(self, from_addr, to_addrs, msg, mail_options=(), rcpt_options=())`

#### Redis 安装

1. 安装步骤
   1. 将下载好的 redis 安装包解压到指定目录
   2. 将 redis 安装目录配置到环境变量的 path 中
   3. 在 cmd 中运行命令 `redis-server` ,查看是否可以启动 redis 数据库

2. redis 重要文件

   + **redis.windows.conf** : redis 的配置文件
   + **redis-cli.exe** : 客户端命令程序
   + **redis-server.exe** : 服务端命令程序
   + 默认端口 : **6379**

3. 一个 reids 配置文件就是一个 redis 数据库

4. 开启多个 redis 服务

   1. 复制配置文件,名称后添加需要开启的端口号

   2. 打开配置文文件更改端口号

      ```
      # Accept connections on the specified port, default is 6379 (IANA #815344).
      # If port 0 is specified Redis will not listen on a TCP socket.
      port 6379
      ```

   3. 开启多个命令端口,使用 `redis-server [配置文件]` 启动 redis 服务

   4. 链接 redis 数据库 `redis-cli -p 端口号`

5. redis 优点

   1. redis 有丰富的数据结构
   2. redis 身为内存化数据库,可以持久化保存数据

6. [redis 文档](https://note.youdao.com/ynoteshare1/index.html?id=b25d0db9b99d173ad016f8d84184bd99&type=note)

#### Scrapy-Redis 分布式

##### 分布式爬虫简介

1. 使用分布式的原因

   + 分布式爬虫就是多台计算机上都安装爬虫程序,重点是**联合采集** (例如: 三台服务器上三个爬虫同时爬取一个网页,需要一个 **状态管理器**集中分配,**去重**已爬过的url)
   + **状态管理器** : 也是一个服务,需要部署在某一台服务器上,通过状态管理器集中分配需要抓取的URL 以及去重
   + 分布式爬虫的优点
     1. 充分利用多机器的带宽进行加速爬取,一台服务器上带宽有限
     2. 充分利用多机器的 IP 加速爬取的速度,一台服务器如果爬取过快容易被封 IP
   + 分布式爬虫 : 多台服务器**有序**的爬取任务为队列的 URL

2. Scrapy 和 Scrapy-Redis 的区别

   1. Scrapy 是一个通用爬虫框架,不支持分布式.分布式爬取需要 Scrapy-redis.
   2. Scrapy-redis **提供以下四种组件 (components) **,使用分布式爬取时需要对四种组件进行修改
      1. Scheduler
      2. Duplication Filter
      3. Item Pipeline
      4. Base Spider
   3. 安装 Scrapy-redis : `pip intsall scrapy-redis`

3. Scrapy-redis 架构

   1. **Scheduler 调度器** : 负责对新的 request 进行入队操作 (加入 Scrapy queue), 取出下一个要爬取的 request (从 Scrapy queue 中取出)等操作

      + Scrapy 改造了 python 本来的 **collection.deque (双向队列) ** 形成自己的 **Scrapy queue** 

      + Scrapy 多个 spider 不能共享待爬取队列 Scrapy queue, 即 Scrapy 本身不支持爬虫分布式,Scrapy-redis 解决就是吧 Scrapy queue 换为 **redis 数据库** (也是指 redis 队列),在同一个 redis-server 存放要爬取的 request,便可以让多个 spider 在一个 redis 数据库读取

      + Scrapy-redis 把待爬取的队列按照优先级建立了一个字典结构,然后根据优先级,决定队列顺序,出列时优先级较小的优先出列.

        ```
        {
        	优先级0 : 队列0,
        	优先级1 : 队列1,
        	优先级2 : 队列2,
        	...
        }
        ```

        

   2. **Duplication Filter (DupeFilter)** : 负责 Scrapy-redis 的去重功能,通过redis 的 **set 不重复** 的特性,实现去重.

      + **Scrapy 去重** : 用集合实现 request 去重,Scrapy 将已将发送的 request 指纹放入一个集合中,把下一个 request 指纹拿到集合中对比,如果指纹存在于集合资,说明 request 发送过了,没有则继续操作

        ```python
        def request_seen(self, request):
            # self.request_fingerprints(request) 一个指纹集合
            fp = self.request_fingerprints(request)
            # 核心操作
            if fp in self.fingerprints:
                return True
            self.fingerprints.add(fp)
            if self.file:
                self.file.write(fp + os.linesep)
        ```

        

      + **Scrapy-redis 去重** : 调度器从引擎接受 **request** , 将 request 的指纹存入 redis 的 set 检查是否出现了重复,并将不重复的 request push 写入 redis 的 request queue
      + **Scrapy-redis 请求过程** : 引擎请求 request (Spider 发送出的) 时,调度器从 redis 的 request queue 队列里根据优先级 pop 出一个 request 给引擎,引擎将此 request 发送给 spider 处理

   3. Item Pipeline

      + **Scrapy-redis 存储过程** : 引擎将 (spider 返回的) 爬取到的 Item 发送给 spider 处理; Item Pipeline  将爬取到的 Item 存入 redis 的 Items queue
      + 修改过后的 Item Pipeline 可以很方便的 根据 key 从 item queue 提取 item,从而实现 **items processes 集群**

   4. Base Spider : 重写后的 RedisSpider 继承了 **Spider** 和 **RedisMixin (从 redis 中读取 url) ** 两个类

      + 当生成一个 Spider 继承 RedisSpider 时, **调用 setup_redis 函数**，这个函数**连接 redis 数据库**,然后会**设置 signals** (信号):
        1. 当 **spider 空闲**的时候的 signals : 会调用 spider_idle 函数,这个函数调用 schedule_next_request 函数,保证 spider 一直存活,并且抛出 **DontCloseSpider 异常**
        2. **抓取到 item** 时的 signals : 调用 item-scraped 函数,这个函数会调用 schedule_next_request 函数,获取下一个 request

4. **总结**

   1. 重写 **schedule (调度器)** 和 **spider 类** : 实现**调度**、**spider 启动**、**redis 的交互**
   2. 实现新的 **dupefilter 类** 和 **queue 类** : 达到 **判重**、**调度容器**、**redis 交互**,由于每个主机上的爬虫都会访问同一个 redis 数据库，所以调度和判重都统一管理,达到分布式的目的
   3. spider 初始化时会同时初始化一个对应的 scheduler 对象, 这个调度器对象通过读取 settings,配置好自己的**调度容器 queue** 和**判重工具 dupefilter**
   4. **Scrapy-redis 开始爬取** : 每当一个 spider 产出一个 request 的时候,Scrapy 引擎会把这个 request 递交给这个 spider 对应的 scheduler 对象进行调度, scheduler 对象通过访问 redis 对 request 进行判重,如果不重复就把其添加到 redis 中的调度器队列里. 当调度条件满足时, scheduler 对象就从 redis 的调度器队列取出一个 request 发送给 spider ,让它爬取
   5. **Scrapy-redis 爬取结束之后 ** : spider 爬取了所有暂时可用的 url 之后, scheduler 发现这个 spider 对应的 redis 的调度器队列空了,于是触发信号 **spider_idle**, spider 收到这个信号之后,直接连接 redis 读取 start_urls 池，拿到新一批 url， 重复 工作

#### 增量爬虫

##### 增量爬虫

+ 增量爬虫 : 通过爬虫程序监控某网站的数据更新情况,以便可以爬取到该网站更新出的新数据
+ 增量爬取步骤 (核心 : **去重**, 可以在1、2步随机一个去重)
  1. 在发送请求前判断该 URL 是否爬取过 (去重 : 适合不断有新网页出现的网站: 小说网、每日新闻)
  2. 解析内容后判断这部分内容是否爬取过 (去重 : 适合页面内容会更新的网站)
  3. 写入存储介质时判断内容是否在介质中
+ **去重方法** :
  + 将爬取过程中产生的 url 进行存储,存储在 redis 的 set 中,当下次进行数据爬取时,首先判断即将发起请求的 url 是否存储在 url 的 set 中存在,如果不存在则请求
  + 对爬取到的网页进行唯一标识限定,然后将该唯一标识限定存储至 redis 的 set 中,当下次爬取到网页数据时,在持久化存储时,首先判断该数据唯一标识符在 redis 中的 set 中是否存在，进一步决定是否进行持久化存储