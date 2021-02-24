### Django

#### Django 特性

1. 优点
   1. 重量级框架,框架本身封装了丰富的功能组件
   2. 完善的开发文档
   3. 开发效率快
2. 缺点
   1. 开发不够灵活、自由,不能够完成高度定制化开发
   2. 执行速度慢

#### Django 安装

##### Django 安装 (使用 2.2.1 最稳定)

1. anaconda 虚拟环境操作
   1. 创建虚拟环境 : `conda create -n  虚拟环境名 python=3.7`
   2. 激活虚拟环境 : `activate 虚拟环境名`
   3. 退出虚拟环境 : `deactivate`
   4. 查看虚拟环境 : `conda env list`
2. 安装 Django : `pip install django==2.2.1 -i 国内源地址`

##### 创建项目

1. 创建工程

   1. 创建一个目录
   2. 进入目录打开终端
   3. 激活虚拟环境 : `activate DjangoPath`
   4. 创建工程 : `django-admin startproject 工程名`

2. Django 项目启动

   1. 进入 Django 项目 manage.py 同级目录

   2. 激活虚拟环境

   3. 启动项目

      + `python manage.py runserver`

      + `python manage.py runserver 9000` : 修改端口
      + `python manage.py runserver 0.0.0.0:9000` : 局域网开放并修改端口
      + 设置 setting.py 中的 `ALLOWED_HOST =['*']`

3. 目录结构

   + 目录名
     + 主目录
       + `__init__.py`  : 主目录初始化文件
       + `settings.py` : 项目配置文件
       + `urls.py` : 项目的主路由文件
       + `wsgi.py` : 项目的部署文件
     + `db.sqlit3` : 启动项目后出现 sqlite3 数据库文件
     + `manage.py` : 项目的管理文件,负责项目的管理、启动

##### Django 第一个项目

+ 在主目录下创建 `views.py`

  ```python
  from django.shortcuts import HttpResponse
  
  def hello(request):
      return HttpResponse('hello word')
  ```

+ 请求流程

  1. 请求 /hello/
  2. Django 查看 `setting.py` 中的 ROOT_URLCONF 设置, 找到根 URL 配置
  3. Django 比较 URL 配置中各个 URL 模式,找到与 /hello/ 匹配的那个
  4. 找到匹配模式就调用对应视图函数
  5. 视图函数返回一个 HttpResponse 对象

##### Django 路由

+ 基本格式

  ```python
  from django.contrib import admin
  from django.urls import path
  from .views import *
  
  urlpatterns = {
      path('admin/', admin.site.urls),
      path('hello/', hello)
  }
  ```

+ 两种格式

  1. `path("字符串", 要执行任务的视图)`
  2. `re_path("正则表达式", 要执行的任务视图)`

+ Django 中 路由正则匹配

  + `re_path(r'^\w/$', views.zf)` : \w匹配任意一个字母数字下划线
  + `re_path(r'^\w+/$', views.zf)` : + 匹配前面表达式以次或多次
  + `re_path(r'^\d/$', views.blog)` : 匹配任意数字

+ 分组匹配

  + 通过分组匹配将 url 路径部分内容,传递到视图函数
  + 通过 () 方式,将匹配到的内容传递给视图函数的形参

+ 分组命名匹配

  + 更直观的分组匹配
  + (?P<名称>正则表达式)

#### Django 模板

##### 模板加载

+ 在 manage.py 同级下创建 文件夹 templates 存放 HTML 模板

+ 在 setting.py 下进行读取模板配置

  ```python
  TEMPLATES = [
      {
          ...
          'DIRS' : [os.path.join(BASE_DIR, 'templates')],
          ...
      }
  ]
  ```

+ 建立 HTML 文件

+ 在 views.py 中 返回页面

  ```python
  from django.shortcuts import HttpResponse, render_to_response
  
  def hello(request):
      # return HttpResponse('hello word')
      return render_to_response('hello.html')
  ```

  

##### 模板语法

+ 变量

  + 语法 : `{{ 变量名 }}`

  + 变量传参

    1. 以 字典形式传参

       ```python
       def index(request):
           uer_info = {'name': "张三", 'age': 12}
           hobbies = ['篮球', '足球']
           return render(request, 'index.html', {
               'user_info': user_info,
               'hobbies': hobbies,
           })
       ```

    2. 以 locals() 集体传参

       ```python
   def index(request):
           uer_info = {'name': "张三", 'age': 12}
           hobbies = ['篮球', '足球']
           return render(request, 'index.html', locals())
       ```
    
  + 支持类型为 : 字符串、整型、列表、字典、元组

  + 变量为字典可以通过键取值

  + 变量为可迭代对象可以使用索引取值

+ 标签

  + 语法 : **{%  %}**

  + 结构

    1. if 结构

       ```jinja2
       {% if 条件 %}
       	执行语句
       {% elif 条件 %}
       	执行语句
       {% endif %}
       ```

    2. ifequal 结构

       ```jinja2
   {% ifequal age 19 %}
       	<p>成年</p>
   {% endifequal %}
       ```
    
    3. for 循环结构
    
       + forloop : 记录循环次数, 常与 if 一起使用

    4. for ... empty 循环

       ```jinja2
   {% for i in arr %}
       	{{ i }}
   {% empty %}
       	列表内没有 i
   {% endfor %}
       ```
    
       
    
    5. autoescape off 关闭自动转义
    
       ```jinja2
   {% autoescape on %}
       	{{ url }}
   {% endautoescape %}
       {% autoescape off %}
   	{{ url }}
       {% endautoescape %}
       ```
    
       
  
+ 过滤器

  + 语法 : `{{ name|过滤器方法: 传值 }}`  用于对传入视图函数值二次处理

##### 静态文件处理

1. 方法一

   1. 在 manage.py 同级目录下创建 static 文件夹, 用来存放静态 JS、CSS、图片等文件

   2. 在 setting.py 内配置

      ```python
      STATIC_URL = '/static/'
      
      STATICFILES_DIRS = [
      	os.path.join(BASE_DIR, 'static'),
      ]
      ```

   3. 在 html 文件内加载静态资源

      ```html
      <img src="/static/xxx.png" alt=">"
      ```

2. 方法二

   1. 在网页头部加上 `{% load static %}`
   2. 访问静态资源 `{% static 'xxx.png' %}`

##### 模板继承和包含

1. 继承 `extends`

   + 对于重复的网页去除冗余代码,或者AJAX方便加载

   + 定义父 base 模板后调用

     ```jinja2
     {% extends 'base.html' %}
     {% block main %}
     
     {% endblock %}
     ```

     

2. 包含 `include`

   + 将常用的页面内容,导航栏、页尾信息等不变组件单独存储,使用时在使用地方导入

   + 语法

     ```jinja2
     {% include 'navbar.html' %}
     ```

#### Django 中的 App

+ 一个 Project (项目) 是一系列 App (应用) 的实例, 以及配置
+ 一个 App (应用) 是一系列便携的 Django 功能, 通常包含模型和视图

##### 创建 App

1. `python manage.py startapp app_name`

2. 在 `setting.py` 文件 INSTALLD_APPS 列表中注册 App

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',
   ]
   ```

   

3. 使用 pycharm 在 **New Project** --> **more setting** 内 创建 App

#### Django 数据库

##### ORM 介绍

1. Object Relational Mapping (ORM 对象关系映射) : 将面向对象语言程序中的对象自动持久化到关系数据库中.本质是将数据从一种形式 (对象) 转换到另一种形式 (数据库表格)
2. ORM 转换对应关系
   1. Python 中一个类 <----> 数据库中一张表格
   2. Python 中一个对象 <----> 数据库表格中一条记录
   3. Python 中类的属性 <----> 数据库表格中的字段
3. ORM 优势
   + ORM 提供数据库的映射, 不直接编写 SQL 代码, 操作数据库只需要像操作对象一样.提高了开发效率.
4. ORM 劣势
   + 一定程度上牺牲程序效率

##### DjangoOrm 建模

+ Django 数据库模型必须在 App 当中的 models 中创建

##### 数据库配置

1. 配置 MySQL 数据库

   1. 设置数据库配置信息

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'db_name',
              'USER': 'user_name',
              'PASSWORD': 'user_password',
              'HOST': 'HOST_IP',
              'PORT': 'mysql_port',  # 默认 3306
          }
      }
      ```

      

   2. 下载 PyMySQL 模块,在 项目包的 `__init__.py` 下

      ```python
      import pymysql
      pymysql.install_as_PyMySQLdb()
      ```

      

   3. 排错 : Django 2.2.1 与 PyMySQL 不兼容需要修改源码

      1. 生成数据库映射时报错

         ```
         Traceback (most recent call last):
           File "manage.py", line 21, in <module>
             main()
           File "manage.py", line 17, in main
             execute_from_command_line(sys.argv)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\__init__.py", line 381, in execute_from_command_line
             utility.execute()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\__init__.py", line 375, in execute
             self.fetch_command(subcommand).run_from_argv(self.argv)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\base.py", line 323, in run_from_argv
             self.execute(*args, **cmd_options)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\base.py", line 364, in execute
             output = self.handle(*args, **options)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\base.py", line 83, in wrapped
             res = handle_func(*args, **kwargs)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\core\management\commands\makemigrations.py", line 101, in handle
             loader.check_consistent_history(connection)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\migrations\loader.py", line 283, in check_consistent_history
             applied = recorder.applied_migrations()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\migrations\recorder.py", line 73, in applied_migrations
             if self.has_table():
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\migrations\recorder.py", line 56, in has_table
             return self.Migration._meta.db_table in self.connection.introspection.table_names(self.connection.cursor())
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\base\base.py", line 256, in cursor
             return self._cursor()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\base\base.py", line 233, in _cursor
             self.ensure_connection()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\base\base.py", line 217, in ensure_connection
             self.connect()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\base\base.py", line 197, in connect
             self.init_connection_state()
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\mysql\base.py", line 231, in init_connection_state
             if self.features.is_sql_auto_is_null_enabled:
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\utils\functional.py", line 80, in __get__
             res = instance.__dict__[self.name] = self.func(instance)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\mysql\features.py", line 82, in is_sql_auto_is_null_enabled
             cursor.execute('SELECT @@SQL_AUTO_IS_NULL')
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\utils.py", line 103, in execute
             sql = self.db.ops.last_executed_query(self.cursor, sql, params)
           File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query
             query = query.decode(errors='replace')
         AttributeError: 'str' object has no attribute 'decode'
         ```

      2. 修改源码: `File "E:\Anaconda\envs\mydjango\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_queryquery = query.decode(errors='replace')`原为 decode ,python3 无此方法,改为 encode

         ```python
         def last_executed_query(self, cursor, sql, params):
             # With MySQLdb, cursor objects have an (undocumented) "_executed"
             # attribute where the exact query sent to the database is saved.
             # See MySQLdb/cursors.py in the source distribution.
             query = getattr(cursor, '_executed', None)
             if query is not None:
             query = query.encode(errors='replace')  # 原为 decode ,python3 无此方法,改为 encode
             return query
         ```

      3. 继续进行数据库检查、生成映射、同步至数据库

         

2. 配置 sqlite3 数据库

   + 配置

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
     }
     ```

     

3. 数据迁移 (添加新的数据库表时)

   1. `python manage.py check` : 检测数据库配置是否有错误
   2. `python manage.py makemigrations app_name` : 生成数据库映射文件
   3. `python manage.py migrate` : 同步数据库

4. Django 模型常用字段

   | 字段名称                               | 字段描述                                                     |
   | -------------------------------------- | ------------------------------------------------------------ |
   | `models.CharField(max_length=32)`      | 字符串类型,必须设置 max_length                               |
   | `models.IntergerField()`               | 整数类型                                                     |
   | `models.FloatField()`                  | 小数类型                                                     |
   | `models.TextField()`                   | 文本类型                                                     |
   | `models.EmailField()`                  | 邮件格式的字符串                                             |
   | `models.DateField()`                   | 日期格式 (年月日)                                            |
   | `models.DateTimeField()`               | 时间格式 (年月日时分秒)                                      |
   | `models.FileField(upload_to=file_dir)` | 文件类型, 特殊类型,可以保存文件路径同时自动上传文件,必须设置 upload_to 上传到媒体路径下的位置 |
   | `models.ImageField(upload_to=img_dir)` | 图片类型, 特殊类型 (需要提前配置),可以保存文件路径同时自动上传文件,必须设置 upload_to 上传到媒体路径下的位置 |
   | `电话类型`                             | 必须是美国座机格式的电话号                                   |

   + 配置 ImageField 保存图片

     1. 安装 pillow 模块 : `pip install pillow`

     2. `setting.py` 配置媒体文件

        ```python
        MEDIA_URL = "/media/"
        MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
        ```

5. Django 数据库常用的字段参数

   | 参数名称       | 参数描述                     |
   | -------------- | ---------------------------- |
   | `verbose_name` | 别名,在后台可以使用          |
   | `default`      | 默认值                       |
   | `unique`       | 不可重复                     |
   | `blank`        | 可以为空,常用于字符串        |
   | `null`         | 可以为 null 常用于数字和时间 |
   | `max_length`   | 字符串长度范围               |
   | `upload_to`    | 文件上传地址                 |
   | `Auto_now`     | 默认当前时间                 |

6. Django ORM 总结

   1. Django ORM 默认自带 id 主键
   2. Django ORM 默认字段不为空,为了方便,通常可以设置 blank 和 null



