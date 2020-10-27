### Django

#### Django 异步开发

##### 发送邮件

+ Smtp : 轻量级邮件发送协议, 邮件的发送和接收人

+ Smtp 服务器地址以及端口

  + SSL : smtp.163.com: 465
  + 非 SSL : smtp.163.com: 25

+ 实例

  ```python
  import smtplib  # smtp 服务器
  from email.mime.text import MIMENText # 邮件文本
  
  # 构建邮件
  
  subject = "邮件主题"
  content = "邮件内容"
  sender = "发件人邮箱"
  recver = "收件人邮箱"
  password = "发送人邮箱密码"
  message = MIMEText(content, "html", "utf-8")
  
  message["Subject"] = subject  # 邮箱主题
  message["From"] = sender  # 发件人
  message["To"] = recver  # 收件人
  
  # 发送邮件, 实例化 smtp 服务器
  smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
  # 登录发送者账号
  smtp.login(sender, password)
  smtp.sendmail(sender, [recver], message.as_string())
  smtp.close()
  ```

  

##### 发送短信

1. 使用第三方发送短信平台实现,以 第三方平台为例 [容联云](https://www.yuntongxun.com)

2. [短信业务接口介绍](http://doc.yuntongxun.com/p/5a533de33b8496dd00dce07c)

3. 发送短信
   + Demo 下载

     ```python
     编码说明：coding=utf-8或gbk
     from CCPRestSDK import REST
     import ConfigParser
      
     accountSid= '您的主账号'; 
     #说明：主账号，登陆云通讯网站后，可在控制台首页中看到开发者主账号ACCOUNT SID。
      
     accountToken= '您的主账号Token'; 
     #说明：主账号Token，登陆云通讯网站后，可在控制台首页中看到开发者主账号AUTH TOKEN。
      
     appId='您的应用ID'; 
     #请使用管理控制台中已创建应用的APPID。
      
     serverIP='app.cloopen.com';
     #说明：请求地址，生产环境配置成app.cloopen.com。
      
     serverPort='8883'; 
     #说明：请求端口 ，生产环境为8883.
      
     softVersion='2013-12-26'; #说明：REST API版本号保持不变。 
      
     def sendTemplateSMS(to,datas,tempId): 
        #初始化REST SDK
     	rest = REST(serverIP,serverPort,softVersion) 
         rest.setAccount(accountSid,accountToken) 
        	rest.setAppId(appId)
      	result = rest.sendTemplateSMS(to,datas,tempId) 
         for k,v in result.iteritems():
             if k=='templateSMS' : 
             	for k,s in v.iteritems():
                 	print '%s:%s' % (k, s) 
             else: 
                 print '%s:%s' % (k, v) 
     ```

4. Python SDK 操作发送短信: `pip install ronglian_sms_sdk`

   ```python
   from ronglian_sms_sdk import SmsSDK
    
   accId = '容联云通讯分配的主账号ID'
   accToken = '容联云通讯分配的主账号TOKEN'
   appId = '容联云通讯分配的应用ID'
    
   def send_message():
       sdk = SmsSDK(accId, accToken, appId)
       tid = '容联云通讯创建的模板ID'
       mobile = '手机号1,手机号2'
       datas = ('变量1', '变量2')
       resp = sdk.sendMessage(tid, mobile, datas)
       print(resp)
   ```

   

##### 基于 Django 的短信和邮箱注册

1. 邮件注册
   1. 步骤
      1. 提交邮箱 (`settings.py` 设置)

         ```python
         # 配置发送邮件信息
         # 邮箱配置
         EMAIL_HOST_USER = 'xxx' # 登录服务器的用户名
         EMAIL_HOST_PASSWORD = 'xxxx' # 授权码
         EMAIL_USE_SSL = True # SSL 表示更加安全
         EMAIL_HOST = 'smtp.163.com' # 主机
         EMAIL_PORT = 994 # 端口号
         ```

         

      2. 发送验证邮件 (验证码、链接)

         ```python
         def email_test(request):
         	email = EmailMultiAlternatives(subject='主题',
         	                               body='欢迎收到我自己的邮件',
         	                               from_email='163邮箱号',
         	                               to=['接收邮箱号'],
         	                               )
         	email.send()
         	return HttpResponse('发送成功')
         ```

         

      3. 跳回网站、完成注册
2. 短信注册
   1. 步骤
      1. 发送验证码
         1. 前端 ajax get 请求获取验证码
         2. 视图函数发送验证码
         3. 视图保存验证码至数据库
      2. 验证码入库
      3. 提交验证码
      4. 比对验证码,确认
         1. 注册视图,获取验证码
         2. 校验验证码
            1. 检验验证按是否存在
            2. 校验验证码是否在有效期内

##### 异步通信框架 Celery

1. Celery 框架介绍

   + Celery 框架 : Python 中专门用来处理异步任务的框架
     + 异步任务 : 当任务发起时,不会阻塞主线程,会到另外的线程或进程运行,直到结束,返回结果
   + 工作案例 : 
     + 验证码的发送 : 用户点击发送验证码后,显示发送验证码,此时后台启用另一个进程进行验证码的发送流程
   + Celery 执行任务流程 (除了异步任务,还可以执行定时任务)
     1. 在发送任务之前, worker 启动
     2. 用户发起任务,任务通常以函数形式存在
     3. 执行完的结果放回 store 中
     4. 任务执行过程中涉及的对象
        1. user : 任务发起人
        2. broker : 任务列表
        3. workers : 执行任务的对象,可以是一个线程、一个进程或一个服务器
        4. store : 接过容器
   + Celery 最常用的两种**任务容器** 和 **结果容器**
     + Redis, NoSQL数据库 : Redis 被频繁的使用在并发,分布式当中,Redis 可以将数据存储在内存中,运算快
     + RabbitMQ 消息队列 : 成熟的用于任务存储 和 转发的消息队列

2. Celery 框架安装

   1. 下载 Redis 数据库 以及 Python 需要 Celery 以及 redis 操作需要组件

      ```python
      pip install django-celery==3.2.2
      pip install django-redis
      pip install redis==2.10.6
      ```

   2. 安装 Redis

      1. 解压 Redis 压缩包
      2. 进入压缩包目录,执行 `redis-server.exe redis.windows.conf` 启动数据库
      3. 关闭 Redis 数据库,先执行 `redis-cli.exe` 客户端连接上数据库再执行 `shutdown` 关闭数据库

3. Celery 异步任务

   1. 配置 `settings.py`, 安装 djcelery App

      ```python
      INSTALLED_APPS = [
          ...
          'Buyer',
          'Seller',
          'djcelery',
      ]
      ```

   2. 创建子应用(app) CeleryTask, 并创建 `tasks.py` 文件  `python manage.py startapp CeleryTask`

   3. `settings.py` 内编写配置

      ```python
      import djcelery
      djcelery.setup_loader()  # 加载模块
      BROKER_URL = 'redis://127.0.0.1:6379/1'  # 指定 broken 的存储位置, 消息中间件 redis 中间人
      CELERY_IMPORTS = ('CeleryTask.tasks')  # 指定任务文件
      ## 时区
      CELERY_TIMEZONE = 'Asia/Shanghai'
      # celery 调度器, 固定写法
      CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
      ```

   4. 项目主目录中 (项目同名目录) 创建 `celery.py` 文件 (控制文件)

      ```python
      import os
      from celery import Celery
      from django.conf import settings
      
      # 设置 celery 的环境变量和 Django-celery 的工作目录
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cmdb.settings')
      
      # 实例化 celery 应用, celery 服务器的名称
      app = Celery('art_project')
      
      # 加载 celery 配置
      app.config_from_object('django.conf:settings')
      
      # 如果在项目中,创建了 task.py ,那么 celery 就会顺着 app 查找 task.py 生成任务
      app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
      ```

   5. `tasks.py` 编写任务 (celery 任务 : 通常是一个函数,但是在功能上添加了 `@app.task` 装饰器)

      ```python
      from __future__ import absolute_import
      from Qshop.celery import app
      
      @app.task
      def Test():
      	import time
      	time.sleep(20)
      	print('休眠结束')
      ```

   6. 启动 celery

      1. 第一次启动需要 数据迁移 `python manage.py migrate`
      2. 启动 celery : `python manage.py celery worker --loglevel=INFO`
      3. 启动报错 `from kombu.async.timer import Entry ...` (Python3 当中 async 为关键词,不可做微模块名称需要修改源码)
         1. 将 kombu 模块的 async 部分改为其他名字 `asynchronous`
         2. 修改保存时, 将文件中所有的 async 改为 asynchronous
      4. 再次启动 worler

   7.  `tasks.py` 发布任务

      ```python
      from CeleryTask.tasks import Test
      
      def index(request):
      	Test.delay()
      ```

   8. 发布带有参数的任务

      ```python
      from CeleryTask import test.myprint
      
      @LoginValid
      def index(request):
          myprint.delay(10)
          return render(request, 'store/index.html')
      ```

4. Celery 定时任务

   1. `settings.py` 增加配置

      ```python
      from celery.schedules import timedelta, crontab
      
      CELERYBEAT_SCHEDULE = {
          u"测试": {
              "task": "CeleryTask.tasks.Test",  # 定时要执行的任务为
              "schedule": timedelta(seconds=2),  # 每两秒执行一次
          }
      }
      ```

   2. 启动 worker : `python manage.py celery worker --loglevel=INFO`

   3. 启动定时任务 : `python manage.py celerybeat --loglevel=INFO` 

   