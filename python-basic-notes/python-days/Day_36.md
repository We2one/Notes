### Flask 蓝图

#### Flask 中的配置文件

##### 直接编写

+ 简单直观的将一些常见的固定不变的配置写入 config.py , 以类似于操作字典的形式操作

##### 配置文件

1. 通过 `app.config.from_object()`方法引入配置

   ```python
   from flask import Flask, request, render_template
   from flask_sqlalchemy import SQLAlchemy
   from demo01.config import Config
   
   app = Flask(__name__)
   # Config 为配置文件内的配置类
   app.config.from_object(Config)
   db = SQLAlchemy(app)
   ```

2. 通过 `app.config.from_pyfile("config.py")`, 直接引用配置

##### 目录结构化

+ `项目名` : 项目目录

  + `static` : 静态文件目录

  + `templates` : 模板文件目录

  + `__init__.py` : 项目初始化文件

    ```python
    from flask import Flask, request, render_template
    from flask_sqlalchemy import SQLAlchemy
    from demo01.config import Config
    
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    ```

    

  + `config.py` : 项目配置文件

    ```python
    import os
    
    class Config:
    	path = os.path.abspath(os.path.dirname(__file__))
    	SQLALCHEMY_DATABASE_PATH = 'sqlite:///' + os.path.join(path, 'mysqlite.sqlite')
    	SQLALCHEMY_TRACK_MODIFICATIONS = True
    ```

    

  + `models.py` : 模型文件

    ```python
    from demo01.views import db
    
    class Base(db.Model):
    	__abstract__ = True
    	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    	def update(self):
    		db.session.commit()
    
    	def save(self):
    		db.session.add(self)
    		db.session.commit()
    
    	def delete(self):
    		db.session.delete(self)
    		db.session.commit()
    ```

  + `views.py` : 视图文件

    ```python
    from demo01.app import *
    from demo01.models import *
    
    @app.route('/add_info/')
    def add_info():
        pass
    ```

    

+ `manage.py` : 项目控制文件

  ```python
  from demo01.views import db, app
  
  if __name__ == '__main__':
  	# db.drop_all()
  	db.create_all()
  	app.run()
  ```

#### 蓝图

+ Web 开发时,用模块化管理将功能模块化区分,方便后续开发维护.
+ Flask 蓝图 (Blueprint) : 方便的将一个应用分解为一套蓝图 (子应用),极大地简化大型应用并为拓展的子应用提供集中的注册入口

##### 蓝图的基本使用

+ 直接使用

  ```python
  # 导入蓝图
  from flask import Blueprint
  
  app = Flask(__name__)
  
  # 创建蓝图对象
  bp = Blueprint('bp', __name__)
  
  # 使用蓝图
  @bp.route('/index/')
  def index():
      return 'index'
  
  if __name__ == '__main__':
  	# 注册蓝图
  	app.register_blueprint(bp)
  
  	app.run(debug=True)
  ```

  