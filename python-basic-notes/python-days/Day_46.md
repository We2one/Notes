### Tornado

#### Tornado 介绍与安装

##### Tornado 介绍

+ Tornado 是 Python 编写的一个强大的可拓展 Web 服务器,在处理**高网络流量**的时候足够强大,创建的时候和 Flask 一样足够轻量,可以应用大量的工具
+ Tornado 与其他框架对比
  1.  完整的 Web 开发框架,与 Django、Flask 一样提供了路由映射,request 上下文,基于模板的页面渲染功能
  2. 高效的网络库,性能可以和 Python 的 Twisted、Gevent 等底层框架媲美,同时提供了 **异步IO**、**超时事件处理**、等功能,
  3. 提供了高效的 HTTPClient, 除了服务器端框架,还提供了基于 异步框架的HTTP 客户端
  4. 提供了高效的内部服务器,Tornado 的内部服务器可直接用于生产环境
  5. 完备的 WebSocket 支持

##### Tornado 安装

1. 创建沙箱环境 : `conda create -n TornadoPath python=3.7`

2. 安装 Tornado : `pip install tornado==6.0.4`

3. 测试安装

   ```python
   import tornado
   tornado.version
   ```

   

#### Tornado Web 路由

##### Tornado 入门

1. 基本 GET 请求案例

   ```python
   import tornado.ioloop
   import tornado.web
   
   class MainHadler(tornado.web.RequestHandler):
       
       def get(self):
           self.write("hello world")
           
   def make_app():
       app = tornado.web.Application(
       	[
               (r"/", MainHadler)
           ]
       )
       return app
   
   def main():
       app = make_app()
       app.listen(8000)
       tornado.ioloop.IOLoop.current().start()
       
   if __name__ == "__main__":
       main()
   ```

   1. tornado.ioloop 类 : 负责 Tornado 进行 io 交互的基础类, 需要让 ioloop 让脚本保持持续的监听
   2. tornado.web 类 : 负责 Tornado Web 开发的基础类
   3. tornado.web.RequestHandler 类 : 负责处理请求的基础类, 在类当中可以重写 get、post、put、delete 等方法,实现对不同类型的请求响应
   4. write 方法 : tornado.web.RequestHandler 类 的一个输出方法
   5. tornado.web.Application 类 : Tornado Web 应用的基础类, 上面编写了处理请求的类, tornado.web.Application 目的是 Tornado 内置服务器的类,用来运行项目, 第一参数 : 可以接收一个 列表类型的路由表,这个路由表当中 都是两元素元组,前面的元素是匹配,后面的元素是处理请求类
   6. app.listen() : 设置访问监听的端口
   7. tornado.ioloop.IOLoop.current().start() : 启动 io 监听

2. RequestHandler 内三个重写方法

   1. Initialize() : 被子类重写, 用于请求类初始化,如果有参数需要在路由中传递

      ```python
      import tornado.ioloop
      import tornado.web
      
      class MainHadler(tornado.web.RequestHandler):
          
          def initialize(self):  # 初始化类
              self.database = database
          
          def get(self):
              self.write("hello world")
              
      def make_app():
          app = tornado.web.Application(
          	[
                  (r"/", MainHadler)
              ]
          )
          return app
      
      def main():
          app = make_app()
          app.listen(8000)
          tornado.ioloop.IOLoop.current().start()
          
      if __name__ == "__main__":
          main()
      ```

      

   2. Prepare() : 请求之前执行的操作

      ```python
      import tornado.ioloop
      import tornado.web
      
      class MainHadler(tornado.web.RequestHandler):
          
          def prepare(self):
              print("请求前执行")
          
          def get(self):
              self.write("hello world")
              
      def make_app():
          app = tornado.web.Application(
          	[
                  (r"/", MainHadler)
              ]
          )
          return app
      
      def main():
          app = make_app()
          app.listen(8000)
          tornado.ioloop.IOLoop.current().start()
          
      if __name__ == "__main__":
          main()
      ```

      

   3. On_finish() : 请求之后执行的操作

      ```python
      import tornado.ioloop
      import tornado.web
      
      class MainHadler(tornado.web.RequestHandler):
          
          def get(self):
              self.write("hello world")
              
          def on_finish(self):
              print(请求之后执行)
              
      def make_app():
          app = tornado.web.Application(
          	[
                  (r"/", MainHadler)
              ]
          )
          return app
      
      def main():
          app = make_app()
          app.listen(8000)
          tornado.ioloop.IOLoop.current().start()
          
      if __name__ == "__main__":
          main()
      ```

      

##### Tornado 路由解析

+ 匹配规则

  1. 路由可以用**字符串**匹配
  2. 路由可以用**正则**匹配
  3. 路由当中**正则组**匹配到的内容作为参数传递给视图函数
  4. 路由当中**正则命名组**匹配到的内容作为参数传递给视图函数对应名称参数

+ 匹配实例

  ````python
  import tornado.web
  import tornado.ioloop

  class MainHandler(tornado.web.RequestHandler):
  
  	def get(self):
  		self.write('hello world')
  
  class ReMainHandler(tornado.web.RequestHandler):
  
  	def get(self):
  		self.write('hello world I am re')
  
  class ReGroupMainHandler(tornado.web.RequestHandler):
  
  	def get(self, args):
  		self.write('I am %s' %args)
  
  class ReNameGroupMainHandler(tornado.web.RequestHandler):
  
  	def get(self, name):
  		self.write('my name is %s' %name)
  
  if __name__ == '__main__':
  
  	app = tornado.web.Application(
  		[
  			(r"/", MainHandler),
  			(r"/re/\w{3}", ReMainHandler),
  			(r'/re_group/(\w{3})/', ReGroupMainHandler),
  			(r'/re_name_group/(?P<name>\w{3})/', ReNameGroupMainHandler),
  		],
  		debug=True,
  		autoreload=True,
  	)

  	app.listen(8000)
  	tornado.ioloop.IOLoop.current().start()
  ````
  
  

#### Tornado 模板系统

##### Tornado 模板加载

+ Tornado 默认加载服务器的根目录 (启动文件目录) 的 HTML 文件 和静态文件,但是需要对静态文件与 HTML 文件进行规范化整理，所以在 application 中可以直接配置文件路径

  | 配置                   | 描述         |
  | ---------------------- | ------------ |
  | `template_path=""`     | 模板文件目录 |
  | `static_path=""`       | 静态文件目录 |
  | `static_url_prefix=""` | 静态文件路由 |

  

+ 实例

  ```python
  if __name__ == '__main__':
  
  	app = tornado.web.Application(
  		[
  			(r"/", MainHandler),
  			(r"/re/\w{3}", ReMainHandler),
  			(r'/re_group/(\w{3})/', ReGroupMainHandler),
  			(r'/re_name_group/(?P<name>\w{3})/', ReNameGroupMainHandler),
  		],
  		debug=True,
  		autoreload=True,
  		static_path='static',
  		static_url_prefix='/static/',
  		template_path='templates',
  	)
  
  	app.listen(8000)
  	tornado.ioloop.IOLoop.current().start()
  ```

  

##### Tornado 模板语法

1. 变量

   | 调用方式                       | 描述             |
   | ------------------------------ | ---------------- |
   | `{{ name }}`                   | 变量调用         |
   | `{{ name[1] }}`                | 变量索引取值     |
   | `{{ name[1:3] }}`              | 变量索引截取     |
   | `{{ name.upper() }}`           | 变量方法调用     |
   | `{{ name.replace("i", "L") }}` | 变量方法传参调用 |

   + 视图函数传参之 HTML

     ```python
     class Index2Handler(tornado.web.RequestHandler):
     
     	def get(self):
     		name = 'zs'
     		self.render('index2.html', name=name)
     ```

2. 标签

   1. if 标签 ,结束标识符是 end 

      ```python
      def get(self):
          name = 'zs'
          result = dict(
              arg_true=True,
              arg_false=False,
              arg_string="字符串",
              arg_number=5,
          )
      		
      ```

      

      | 调用方式                                                     | 描述         |
      | ------------------------------------------------------------ | ------------ |
      | `{% if result[" arg_true"] %}`<br>`{% end %}`                | 布尔值判断   |
      | `{% if result[" arg_string"] == "字符串" %}`<br/>`{% end %}` | 字符串判断   |
      | `{% if result[" arg_number"] == 5 %}`<br/>`{% end %}`        | 数字比较判断 |

      

   2. for 标签, 结束符也是 end ( 可以使用enumerate 函数遍历列表 )

   3. 模板继承与加载 `{% block 继承名 %} 模板页 {% end %}`、`{% extends "xxx.html" %}`、`{% include "xxx.html" %}`

##### Tornado 请求响应

+ 请求响应方法

  | 方法       | 描述               |
  | ---------- | ------------------ |
  | render     | 加载页面           |
  | redirect   | 跳转 (重定向) 页面 |
  | write      | 返回数据           |
  | set_header | 设定响应头部       |

+ 返回 JSON

  ````python
  import json
  
  class JsonHandler(tornado.web.RequestHandler):
  
  	def get(self):
  		self.set_header('Content-Type', 'application/json; charset=UTF-8')
  		self.write(json.dumps({'message': 'ok'}))
  		self.finish()
  ````

#### Tornado 数据库操作

##### Torndb 数据库操作工具

1. 安装 Torndb : `pip install torndb`

2. 安装 pymysql : `pip install pymysql`

3. 修改代码 (torndb 对 python3 支持存在问题) : 将所有的 **MySQLdb** 修改为 **pymysql**, 设置连接超时为 10

   ```python
   def __init__(self, host, database, user=None, password=None, max_idle_time=7 * 3600,
               connect_timeout=10,
               time_zone="+0:00", charset="utf8", sql_mode="TRADITIONAL"):
       self.host = host
       self.database = database
       self.max_idle_time = float(max_idle_time)
       
   def query(self, query, *parameters, **kwparameters):
       ...
       try:
           ...
           return [Row(itertools,zip_longest(column_names, row)) for row in cursor]
       finally:
           cursor.close()
   ```

4. 使用时

   ```python
   import torndb
   
   db = torndb.Connection(
   	host="127.0.0.1",
       database="",
       user="",
       password="",
   )
   
   result = db.get("select * from car where id = 1")
   ```

##### Tornado SQLAlchemy (Tornado ORM)

1. 安装 SQLAlchemy : `pip install sqlachemy`

2. 安装 pymysql : `pip install pymysql`

3. 创建数据库测试

   ```python
   import os
   from sqlachemy import create_engine  # 创建数据库链接核心,负责连接数据库
   from sqlachemy import Column, String, Integer, Float  # 定义数据表需要字段
   from sqlachemy.ext.declarative import declarative_base  # 进行表和核心关联的方法
   import pymysql
   
   pymysql.install_as_MySQLdb()
   
   base_dir = os.path.abspath(os.path.dirname(__file__))
   db_path = "sqlite:///" + os.path.join(base_dir, 'mysqlite,sqlite3')
   
   engine = create_engine(
   	db_path,
       encoding="utf-8",
       echo=True,
   )
   
   Base = declarative_base(bind=engine)  # 创建关联核心的数据库表基类
   
   class Car(Base):
       id = Column(Integer, primary_key=True, autoincrement=True)
       ...
       
   if __name__ == "__main__":
       Base.metadata.create_all()  # 同步数据库
   ```

   

4. 封装模型

   ```python
   class BaseModel(Base):
       id = Column(Integer, primary_key=True, autoincrement=True)
       
       def save(self):
           session = Session()
           session.add(self)
           session.commit()
       
       def delete(self):
           session = Session()
           session.delete(self)
           session.commit()
           
       def update(self):
           session = Session()
           session.commit()
           
   class Car(BaseModel):
       pass
   ```

   

5. SQLAlchemy 操作 : 基本的数据库操作与 Flask-SQLAlchemy 类似，在创建查询对象有所不同

   + 查询数据 : `from sqlachemy import func`

     ```python
     from sqlachemy import func
     
     # 查询总和
     car_number = self.session.query(
     	Car,
         func.sum(Car.c_price)
     )
     ```

     

##### 基于 ORM 的结构修改

1. `app.py` : 创建数据库引擎和服务

   ````python
   import tornado.web
   from urls import urlpatters
   from settings import debug_config
   
   def make_app():
       app = tornado.web.Application(
   	    urlpatters,
   	    **debug_config,
       )
       return app
   ````

   

2. `manage.py` : 控制文件

   ```python
   import torndo.ioloop
   from models import base
   from app import make_app
   
   if __name__ == "__main__":
       base.metadata.create_all()
       app = make_app()
       app.listen(8000)
       tornado.ioloop.IOLoop.current().start()
   ```

   

3. `models.py` : 数据库文件

   ```python
   class BaseModel(Base):
       id = Column(Integer, primary_key=True, autoincrement=True)
       
       def save(self):
           session = Session()
           session.add(self)
           session.commit()
       
       def delete(self):
           session = Session()
           session.delete(self)
           session.commit()
           
       def update(self):
           session = Session()
           session.commit()
           
   class Car(BaseModel):
       pass
   ```

   

4. `settings.py` : 配置文件

   ```python
   import os
   base_dir = os.path.dirname(os.path.abspath(__file__))
   db_path = "sqlite:///" + os.path.join(base_dir, 'mysqlite,sqlite3')
   
   debug_config = dict(
   	debug=True,
       autoreload=True,
       static_path='static',
       static_url_prefix='/static/',
       template_path='templates',
   )
   ```

   

5. `urls.py` : 路由文件

   ```python
   from views import *
   
   urlpatters = [
       ('/', MyHeadler),
    	...
   ]
   ```

   

6. `views.py` : 视图文件

#### Tornado 请求管理

| 属性名    | 描述                      |
| --------- | ------------------------- |
| method    | http 请求方法             |
| uri       | 客户端请求的完整 uri 地址 |
| path      | Uri 当中的路径            |
| version   | http 版本                 |
| headers   | http headers 字典格式     |
| body      | http 请求内容,字符串格式  |
| remote_ip | 客户端 ip                 |
| protocol  | 请求的协议 http/https     |
| host      | 请求的主机                |
| arguments | 客户端提交的参数          |
| files     | 客户端上传的文件          |

