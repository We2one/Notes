### Flask 插件

#### Flask-Script

+ 完成项目在 Linux 下的管理、使用、添加命令

##### 安装插件

+ `pip install flask-script`

##### 使用插件

+ 引用

  ```python
  from flask import Flask
  from flask_script import Manager
  
  app = Flask(__name__)
  
  # 管理 app
  manager = Manager(app)
  
  """
  Linux 运行时 可以直接  python xxx.py runserver
  """
  ```

##### 配置 pycharm 启动项目

##### 安装运行命令

+ 实例

  ````python
  from flask import Flask
  from flask_script import Manager, Command
  
  app = Flask(__name__)
  
  manager = Manager(app)
  
  # 增加命令 hello
  class Hello(Command):
      def run(self):
          print('hello, world')
  
  class Runserver(Command):
      def run(self):
          app.run(port=8000)
  
  # 添加命令, 执行 python xxx.py hello 输出 hello world
  manager.add_command('hello', Hello)
  # 添加命令, 执行 python xxx.py runserver8000 项目开始监听 8000 端口
  manager.add_command('runserver8000', Runserver)
  
  @app.route('/index/')
  def index():
      return "你看"
  
  if __name__ == '__main__':
      manager.run()
  ````

#### Flask-Migrate

+ Flask-Migrate : 实现数据迁移 替代 `db.create_all()`,使用命令行生成表格

##### 安装

+ `pip install flask-migrate`

##### 使用

+ `__init__.py` : 项目初始化

  ```python
  from flask import Flask
  from flask_sqlalchemy import SQLAlchemy
  from flask_migrate import Migrate
  
  db = SQLAlchemy()
  # 实例化
  migrate = Migrate()
  
  def creeateApp(obj):
      app = Flask(__name__)
      app.config.from_object(obj)
      # 惰性加载
      db.init_app(app)
      migrate.init_app(app, db)
      
      from blueprintproject.app import bp
      
      from blueprintproject.user import user_bp
      app.register_blueprint('bp', url_prefix='/app')
      app.register_blueprint('user_bp', url_prefix='/user')
      return app
  ```

+ `main.py` 

  ````python
  from blueprintproject import creatApp
  from config import Config
  from flask_script import Manager, Command
  from flask_migrate import MigrateCommand
  
  app = createApp(Config)
  
  # 管理 app
  manager = Manger(app)
  # 增加命令 hello
  class Hello(Command):
      def run(self):
          print('hello, world')
  
  class Runserver(Command):
      def run(self):
          app.run(port=8000)
  
  # 添加命令, 执行 python xxx.py hello 输出 hello world
  manager.add_command('hello', Hello)
  # 添加命令, 执行 python xxx.py runserver8000 项目开始监听 8000 端口
  manager.add_command('runserver8000', Runserver)
  # 安装命令
  manager.add_command('db', MigrateCommand)
  
  @app.route('/index/')
  def index():
      return "你看"
  
  if __name__ == '__main__':
      manager.run()
  ````

##### 执行数据迁移

+ 初始化 : `python xxx.py db init`
+ 生成迁移文件,将模型中的变更生成对应迁移文件 : `python xxx.py db migrate`
+ upgrade 执行迁移文件,将生成的迁移文件执行,达到同步表结构的目的 : `python xxx.py db upgrade`

#### Flask-WTF

##### 介绍

1. 功能一
   1. 前端校验
      1. 使用前端的技术完成数据是否为空、长度、类型的判断
      2. 可以使用 Flask-WTF 表单类完成前端校验
      3. 可以通过 Form 表单类中增加属性，返回 Form 表单类的实例,前端使用实例创建的样式,进行前端校验
   2. 后端校验
      1. 校验数据是否为空、长度、类型、是否有敏感字、数据是否合法、是否已经存在
      2. 通过 Form 中的属性进行后端校验
      3. 可以通过自定义校验完成后端校验
2. 功能二
   1. 下发 csrftoken，并完成 CSRF 校验

##### 安装

+ `pip install flask-wtf`



##### 使用 Flask-WTF 插件

1. 创建 forms.py

   ```python
   from flask_wtf import FlaskForm
   import wtforms
   # 校验器
   from wtforms import validators
   from wtforms import ValidationError
   
   
   class UserForm(FlaskForm):
   	# 对填写的数据进行校验
   	name = wtforms.StringField(
   		label="账号",
   		# 校验规则
   		validators=[
   			validators.Email(message="必须是邮箱"),
   		]
   	)
   	password = wtforms.PasswordField(label="密码")
   ```

2. 视图 : 实例化 Form 类, 将 Form 类对象渲染到模板中

   + 模板页面可以使用 Form 类提供的样式,可以完成部分的前端校验

   + 注意 : 下发 csftoken

     + 除了对应 Form 类的后端校验进行 csrftoken 之外，其他的 post 请求不进行校验

     ```python
     from flask import render_template, request
     from .forms import UserForm
     
     
     @user_bl.route('/register/', method=['GET', 'POST'])
     def register():
     	userform = UserForm()
     	if request.method == 'POST':
     		data = request.form
     		print(data)
     	return render_template('register.html', **locals())
     ```

3. 后端校验

   1. 使用 WTF 提供的方法进行后端校验

   2. 页面中使用 Form 提供样式

   3. 将数据提交到视图,进行后端校验

   4. 常用的表单字段

      | 字段          | 说明                                |
      | ------------- | ----------------------------------- |
      | StringField   | 字符串                              |
      | IntergerField | 整型                                |
      | TextAreaField | 文本                                |
      | PasswordField | 密码                                |
      | HiddenField   | 隐藏域                              |
      | DateField     | Datatime.data 格式 年月日           |
      | DateTimeField | Datatime.datatime 格式 年月日时分秒 |
      | FloatField    | 小数                                |
      | RadioField    | 单选                                |
      | SelectField   | 下拉                                |
      | FileField     | 文件                                |
      | SubmiField    | 提交                                |

   5. 校验规则

      | 方法         | 说明                            |
      | ------------ | ------------------------------- |
      | Email        | 邮件校验                        |
      | EqualTo      | 比较两个字段的值,常用于密码比较 |
      | IPAddress    | Ipv4 格式的 IP 地址             |
      | length       | 长度                            |
      | NumnerRange  | 数字范围                        |
      | DataRequired | 空值检查                        |
      | Url          | 检查是否符合 url 格式           |
      | AnyOf        | 确保输入值在指定范围            |
      | NoneOf       | 确保输入值不在指定范围          |

      



