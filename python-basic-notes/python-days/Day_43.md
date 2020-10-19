### Django

#### Django 高级开发

##### 自定义过滤器

1. 例如: 个人中心页面,手机号隐藏中间部分实现

   1. 视图 (views.py) 修改, 在视图中将用户手机号中部分内容隐藏为 `*`
   2. 视图返回原有数据,使用自定义过滤器方法,将手机号中间部分内容隐藏

2. 自定义过滤器定义

   1. 在 App 中新建一个包 templatetags , 名字固定

   2. 在 `setting.py` 内注册

      ```python
      INSTALLED_APPS = [
      	...
      	'buyer',
      	'buyer.templatetags',
      ]
      ```

      

   3. 在templatetags包中新建一个 py 文件, 名字任意

   4. 创建过滤器,编写函数代码,并注册

      ```python
      from django.template import Library
      
      # 必须使用 register
      register = Library()
      
      # 注册过滤器
      @register.filter
      def filter_phone(phone):
          return phone[:3] + "*"*4 + phone[-4:]
      ```

3. 自定义过滤器使用

   1. 在模版中加载过滤器
      + 在显示手机号的模块首行加载过滤器 : `{% load mytag %}`
   2. 使用过滤器
      + 在使用手机号的地方使用自定义过滤器 : `联系方式: {{ user.phone | filter_phone }}`
   3. 结果

##### 自定义实体类管理器 manager 

1. 导包 : `from django.db.models import Manager`

   + 通常通过模型的 objects 方法调用查询的方法,实际上 objects 是 Django 模型动态生成的查询类,这个查询类继承了 models.Manager

2. 定义类 : 自定义 objects 在 models.py 文件内

   ```python
   from django.db.models import Manager
   
   class MyUser(Manager):
       # 查询
       def getusername(self, id):
           # 根据用户 id 查询邮箱
           user = Seller.objects.filter(id = id).first()
           if user:
               return user.email
           else:
               return user
   ```

   

3. 将定义的类复制到 objects

   ```python
   class Seller(models.Model):
       ...
       objects = MyUser()
   ```

4. 使用 

   ```python
   from Seller.models import Seller
   data = Seller.objects.getusername(4)
   # <===> 等同于
   data = Seller.objects.filter(id=4).first()
   ```

   

##### 中间件

1. 中间件介绍

   + 中间件介绍 : 中间件是处理 Django 请求和相应的框架级别 钩子, 是一个轻量、低级别的插件系统,用于全局范围改变 Django 的输入输出,每个中间件都有固定的功能,使用需要谨慎.解决了项目代码的冗余和一致性问问题
   + 中间件包含的方法 (中间件开发过程中,一次请求分为5 个部分)
     1. process_request : 视图之前,请求开始
     2. process_views : 视图中,请求开始
     3. process_exception : 错误
     4. process_template_response : 模板开始渲染,试图结束
     5. process_response : 响应结束

2. 中间件使用

   1. 创建文件

      + 在项目的主目录 (与项目同名目录) 下创建 middleware.py 文件, 用来编写中间件

   2. 中间件的方法

      1. 在 middleware.py 文件内编写中间件的五个方法

         ```python
         from django.utils.deprecation import MiddlewareMixin
         
         class MiddleWareTest(MiddlewareMixin):
             
             def process_request(self, request): ...
                 
             def process_view(self, request, callback, callbackargs, callbackkwargs): ...
                 
             def process_exception(self, request, exception): ...
                 
             def process_template_response(self, request, response): ...
                 
             def process_response(self, request, response): ...
         ```

      2. 在 setting.py 注册中间件

         ```python
         MIDDLEWARE = [
             ...
             'buyer.middlewawre.MiddleWareTest'
         ]
         ```

         

3. 中间件方法

   1. process_request : 视图之前,请求开始

      ```python
      def process_request(self, request):
          """
          在视图函数之前执行
          :param request:
          :return: 如果返回响应对象则不再执行视图函数。
          不写返回值和 返回None 表示不拦截 （放行），
          """
      
          print('process request')
      ```

      

   2. process_views : 视图中,请求开始

      ```python
      def process_view(self, request, view_func, view_args, view_kwawrwgs):
          """
          在 process_request 之后，在 视图函数之前执行。
      
          :param request:
          :param view_func: 表示视图函数的内存地址
          :param view_args: 接受视图函数位置参数
          :param view_kwargs:接受视图函数的关键字参数
          :return: 如果返回响应对象则不再执行视图函数。
          不写返回值和 返回None 表示不拦截 （放行）。
          """
      
          print('process view ...')
      ```

      

   3. process_exception : 错误

      ```python
      def process_exception(self,request, exception):
          """
          在视图函数抛出异常之后执行
          :param request:
          :param execption:
          :return:
          """
      
          print('process_exception')
          print(exception)
          return HttpResponse('操作出现错误')
      ```

      

   4. process_template_response : 模板开始渲染,试图结束

      ```python
      def process_template_response(self, request, response):
          """
          响应对象中必须包含 render 方法。
          在视图函数之后执行。
          :param reqeust:
          :param response:
          :return: 必须要有返回值
          """
      
          print('process_template_response')
      ```

      

   5. process_response : 响应结束

      ```python
      def process_response(self, request, response):
          """
          在视图函数之后执行。
          :param request:
          :param response:
          :return: 必须要有返回值
          """
      
          print('process_response')
          return response
      ```

      

##### 缓存

1. 缓存介绍

   + Django 做动态网站时,每次请求页面都需要做许多运算,从数据库中进行多次读取,然后渲染
   + 缓存 : 对常用的数据存放到独立的容器内,当用户请求,先在容器内查找
   + 缓存容器 : 内存、文件、数据库 或 专业缓存服务器 (Memcache)
     + 内存 : 缓存最快,但是有内存溢出漏洞
     + 文件 : 缓存中性价比较高,安全有漏洞
     + 数据库缓存 : 在创建一个表存放常查询的数据,设计难度高
   + 缓存常用配置 : 在 `setting.py` 中,默认没有缓存配置,可以到 `global_settings.py` (缓存配置在 Python 目录下 `Lib\site-packages\django\conf`) 中查找缓存配置

2. 缓存基本格式 : `global_settings.py`

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
           'LOCATION': '', # 变量,缓存名称,文件缓存: 文件名,数据库缓存: 数据库名
           'TIMEOUT': 300, # 缓存时间,默认300s 如果为 None 表示永不过期
           'OPTIONS': {
               'MAX_ENTRIES': 300, # 最大缓存个数,默认 300 个
               'CULL_FRQUENCY': 3, # 达到最大缓存个数后,删除缓存比例,默认是3
           }
       }
   }
   ```

   

3. 内存缓存: `LocMemCache`

4. 文件缓存 : `FileBaseCache`

   ```python
   'BACKEND': 'django.core.cache.backends.filebased.FileBaseCache',
       # cache_name 文件名
   'LOCATION': os.path.join(BASE_DIR, 'cache_name') , # 变量,缓存名称,文件缓存: 文件名,数据库缓存: 数据库名
   ```

   

5. 数据库缓存: `DatabaseCache`

   ```python
   'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
       # cache_table 缓存表名
   'LOCATION': 'cache_table' , # 变量,缓存名称,文件缓存: 文件名,数据库缓存: 数据库名
   ```

   

6. Memcache 服务器 使用

   1. 安装 Memcache 服务器 : 下载 Memcache 安装文件 , 命令行运行 安装命令 `memcached.exe -d install`

   2. 启动 Memcache 服务器 : 在 服务中启动 Memcache 服务

   3. 安装 Memcache 包 : `pip install python-memcached`

   4. 配置 cache 缓存 : (缓存配置在 Python 目录下 `Lib\site-packages\django\conf`)

      ```python
      CACHES = {
          'default': {
              'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
              'LOCATION': '127.0.0.1:11211', # 变量,缓存名称,文件缓存: 文件名,数据库缓存: 数据库名
              'TIMEOUT': 300, # 缓存时间,默认300s 如果为 None 表示永不过期
              'OPTIONS': {
                  'MAX_ENTRIES': 300, # 最大缓存个数,默认 300 个
                  'CULL_FRQUENCY': 3, # 达到最大缓存个数后,删除缓存比例,默认是3
              }
          }
      }
      ```

      

   5. 缓存的使用

      1. 在视图中使用

         ```python
         from django.views.decorators import cache_page
         
         @cache_page(60*15)  # 设置 15 分钟 缓存
         def index(request):
             pass
         ```

         

      2. 在路由中使用

         ```python
         from django.views.decorators.cache import cache_page
         
         urlpatterns = [
             path('index/', cache_page[15 * 60](index))  # 仅对当前路由缓存
         ]
         ```

         

      3. 在 HTML 中使用 缓存

         ```HTML
         {% load cache %}
         {% cache 500 hsqcache %}  // 缓存时间 和 名称
         <img src="" class="">
         {% endcache %}
         ```

         

      4. 全局使用 : 在 setting.py 内注册 中间件

         ```python
         MIDDLEWARE = [
             'django.middleware.cache.FetchFromCacheMiddleware',
         ]
         ```

         

      5. 底层 cache 使用

         1. 导包 : `from django.core.cache import cache`
         2. cache 方法
            + `cache.get(key)` : 获取缓存
            + `cache.set(key, value, timeout)` : 设置缓存
            + `cache.delete(key)` : 删除缓存
         3. 设置缓存流程
            + 请求数据
              + 判断缓存中是否存在数据
            + 存在数据
              + 返回数据
            + 不存在数据
              + 在数据库中查询数据
              + 设置数据在缓存中
              + 返回结果