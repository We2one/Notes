### Flak 数据库与请求

#### 1.Flask 数据库

##### 1.1 ORM

+ ORM (Object Relational Mapping 对象映射关系) : 通过使用描述对象和数据库之间映射的元数据,将面向对象语言程序中的对象自动持久化到关系数据库中.
+ 本质 : 将数据从一种形式转换到另一种形式

##### 1.2 Flask-SQLAlchemy 链接

1. 安装 Flask-SQLAlchemy : `pip install flask-sqlalchemy`

2. 使用

   1. 链接 SQLite 数据库 (python自带)

      1. 创建 dbSettings.py 文件 用于设置数据库

         ```python
         import os
         
         
         class Config:
         	# 获取项目所在绝对路径
             # __file__ : 获取现在文件路径
         	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
         	# 配置数据库的 URL
         	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "my_db.sqlite")
         	# 配置-查看映射的 sql 语句
         	# app.config['SQLALCHEMY_CEHO'] = True
         	# 动态追踪修改设置
         	SQLALCHEMY_TRACK_MODIFICATIONS = True
         ```
      
      
      
   2. 在 app.py 内引用 SQLite 设置
   
         ````python
         from flask import Flask
         from flask_sqlalchemy import SQLAlchemy
         from db_setting import Config
         
         app = Flask(__name__)
         # 添加 app 的数据库设置
         app.config.from_object(Config)
         # 创建核心对象
         db = SQLAlchemy(app)
         
         class Student(db.Model):
         	id = db.Column(db.Integer, primary_key=True)
         	name = db.Column(db.String(32))
         
         # 同步表结构
         db.create_all()
         
         if __name__ == '__main__':
         	app.run()
      ````
   
2. 链接 MySQL 数据库
   
   1. 安装 PyMySQL : `pip install pymysql`
   
   2.  `pymysql.install_as_MySQLdb()  # 2.x版本是内置的 MySQLdb 模块,3.x版本,MySQLdb 就不可以使用了`
   
   3. 数据库创建需要存储数据的库 : `CREATE DATABASE db_name charset=utf-8`
   
   4. Flask-SQLAlchemy 链接数据库
   
      + 修改 SQLALCHEMY_DATABASE_URI 配置链接 MySQL 数据库
   
         + 链接内容 : `SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db_name'`
      
           | 参数     | 说明       |
           | -------- | ---------- |
           | mysql    | 协议名     |
           | username | 用户名     |
           | password | 密码       |
         | server   | 主机IP     |
        | db       | 数据库名称 |
   
      + `SQLALCHEMY_TRACK_MODIFICATIONS=True` : 默认为 True ,追踪对象的修改并且发送信号
   
      5. 运行项目 : `db.create_all()`
      
         1. 执行 `.create_all()` 方法将被创建的模型同步生成表结构
         2. 注意 : `.create_all()`方法只能将新创建的模型同步表结构,如果模型修改或删除,`.create_all()`不会同步字段和属性
         
         ````python
         from flask import Flask
         from flask import render_template
         from flask_sqlalchemy import SQLAlchemy
         import pymysql
         
         app = Flask(__name__)
         pymysql.install_as_MySQLdb()  # 2.x版本是内置的 MySQLdb 模块,3.x版本,MySQLdb 就不可以使用了
         # 链接数据库
         app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/test'
         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
         db = SQLAlchemy(app)
         class Student(db.Model):
         	__tablename__ = 'Student'
         	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
         	name = db.Column(db.String(32))
         
         # 创建表
         db.create_all()
         # 删除表
         db.drop_all()
         ````
         
##### 1.3 数据库建模

+ SQLALCHEMY 建模常用字段

  + 常用字段类型

    | 属性     | 描述                   |
    | -------- | ---------------------- |
    | Integer  | 整型                   |
    | Float    | 浮点型                 |
    | Date     | 时间类型(年月日)       |
    | DateTime | 时间类型(年月日时分秒) |
    | Text     | 长文本                 |
    | String   | 变长字符串             |

    

  + 常用字段属性

    | 属性        | 描述       |
    | ----------- | ---------- |
    | primary_key | 主键       |
    | unique      | 键值唯一性 |
    | index       | 索引       |
    | nullable    | 空值       |
    | default     | 默认值     |

+ 建模需要描述的内容

  + 业务主体 : 网站中对象
  + 主体关系 : 对象之间联系

+ 员工表模型

  ```python
  class Person(db.Model):
  	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  	username = db.Column(db.String(32), unique=True)
  	password = db.Column(db.String(32))
  	nickname = db.Column(db.String(32), default="")
  	age = db.Column(db.Integer, default=18)
  	gender = db.Column(db.String(16), default="男")
  	score = db.Column(db.Float, nullable=True)
  ```

##### 1.4 目录结构化

1. app.py : 项目初始化,配置文件

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from db_setting import Config
   
   app = Flask(__name__)
   app.config.from_object(Config)
   db = SQLAlchemy(app)
   ```

   

2. main.py : 项目控制文件

   ```python
   from __init__ import app
   
   if __name__ == '__main__':
   	app.run()
   
   ```

   

3. models.py : 模型文件 (存放数据库模型)

   ````python
   from __init__ import db
   
   class Student(db.Model):
   	id = db.Column(db.Integer, primary_key=True)
   	name = db.Column(db.String(32))
   
   # 同步表结构
   db.create_all()
   ````
4. views.py : 视图文件 (存放引用视图)

   ```python
   from __init__ import app
   from flask import render_template
   
   
   @app.route('/')
   def hello_world():
   	return 'Hello World!'
   ```

##### 1.5 Flask-SQLAlchemy 操作

1. 单表操作

   1. 增加数据

      1. 增加单条数据

         ```python
         person = Person(
         	username = "小孙",
             password = "123456",
             nickname = "老孙",
             age = 12,
             score = 45.5
         )
         ```

         

      2. 增加多条数据

         ```python
         person1 = Person(
         	username = "小孙",
             password = "123456",
             nickname = "老孙",
             age = 12,
             score = 45.5
         )
         person2 = Person(
         	username = "小张",
             password = "123456",
             nickname = "老张",
             age = 22,
             score = 45.5
         )
         ```

   2. 查询

      | 方法                                                         | 说明                                                         | 例子                                                         |
      | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
      | `.query.all()`                                               | 查询符合条件的所有内容,返回值为列表,没有值就返回空列表       | 查询当前所有员工<br>`person_list = Person.query.all()`       |
      | `.query.get()`                                               | 通过 id 进行查找,返回值为对象,没有值返回 None                | 查 id 为 255 的员工<br>``person_list = Person.query.get(255)`` |
      | `.query.filter()`<br><hr><br>`.query.filter_by()`            | 过滤筛选                                                     | 查所有年龄大于21的男生<br>`persion_list=Person.query.filter(Person.age>21,Person.gender=="男")`<br/>查所有男生<br/>`persion_list=Person.query.filter_by(gender=="男")` |
      | `like()`                                                     | 模糊查询<br>*%* : 匹配0个或多个<br>*_* : 匹配一个            | 查所有年龄大于21的吴姓男生<br/>`persion_list=Person.query.filter(Person.age>21,Person.gender=="男",Person.nickname.like('吴%'))` |
      | `.query.filter().limit()`<br>`.query.filter_by().limit()`    | 返回的数据条数                                               | 查10位年龄大于21的男生<br>`persion_list=Person.query.filter(Person.age>21,Person.gender=="男").limit(10)` |
      | `.query.filter().limit().offset()`<br/>`.query.filter_by().limit().offset()` | 查询起始位置,以下标进行偏移                                  | 从第二十个开始,查10位年龄大于21的男生<br>`persion_list=Person.query.filter(Person.age>21,Person.gender=="男").limit(10).offset(20)` |
      | `.query.filter().limit().order_by()`<br/>`.query.filter_by().limit().order_by()` | 排序<br/>顺序: `.order_by(db_name.条件)`<br/>逆序: `.order_by(db_name.条件.desc())` | 按照年龄排序,查询所有吴姓男同事,逆序<br>`persion_list=Person.query.filter(Person.gender=="男",Person.nickname.like('吴%')).order_by(Person.age.desc())` |
      | `max()`、`min()`、`count()`、`sum`、`avg`                    | 聚合查询                                                     | 需要先引入 func 函数 `from sqlalchemy import func`<br>查询所有物姓男生个数<br>`result = db.session.query(func.count(Person.id)).filter(Person.gender=="男",Person.nickname.like('吴%')).all()` |
      | `group_by(db_name.分组条件)`                                 | 分组查询                                                     | 需要先引入 func 函数 `from sqlalchemy import func`<br/>查询男女个数<br/>`result = db.session.query(Person.gender, func.count(Persion.id)).group_by(Persion.gender).all()` |
      | `and_()`、`or_()`、`not_()`                                  | 逻辑查询                                                     | 需要先引入 函数 `from sqlalchemy import and_,or_,not_`<br>查询所有吴姓同事或男同事<br>`person_list = Person.query.filter(or_(Person.gender=="男",Person.nickname.like("吴%")))` |

   3. 修改

      ```python
      # 修改 id 为 5 的用户性别为男
      person = Person.query.get(5)
      person.gender = "男"
      db.session.commit()
      ```

   4. 删除

      ```python
      # 删除 id 为 25 的用户
      person = Person.query.get(25)
      db.session.delete(person)
      db.session.commit()
      ```

      

2. 封装

   1. 每一个模型都需要创建一个 id 字段,可以将冗余的代码封装成一个基类

   2. 所有数据都需要增加删改方案

      1. 增加

         ```python
         def update(self):
             db.session.add()
             db.session.commit()
         ```

         

         

      2. 修改

         ```python
         def update(self):
             db.session.commit()
         ```

         

      3. 删除

         ```python
         def update(self):
             db.session.delete()
             db.session.commit()
         ```

         

      4. 查询

##### 1.6 Flask-SQLAlchemy 关系

1. 一对多关系,采用外键 (foreign-key) 进行一对多约束

   1. 例如: 员工与职位关系

   2. 模型搭建

      ```python
      ## 职位
      class Position(Base):
          __tablename__ = "position"
          p_name = db.Column(db.String(32))
          p_level = db.Column(db.Integer)
          p_person = db.relationship(
          	"Person" # 映射的类对象
              backref="our_position" # 反向映射,给person 表使用
          )
      ## 员工
      class Person(Base):
          # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
          username = db.Column(db.String(32), unique=True)
          password = db.Column(db.String(32))
          nickname = db.Column(db.String(32), default="")
          age = db.Column(db.Integer, default=18)
          gender = db.Column(db.String(16), default=18)
          score = db.Column(db.Float, nullable=True)
          
          # 声明p_position 是一个外键整型字段,对应 position 表的 id
          p_position = db.Column(db.Integer, db.ForeignKey("position.id"))
      ```

      + `__tablename__=""` : 表格名
      + `p_position = db.Column(db.Integer, db.ForeignKey("position.id"))` : 声明p_position 是一个外键整型字段,对应 position 表的 id
      + `p_person = db.relationship("Person", backref="our_position")` : 创建字段反向映射多表,backref 多表中操作一表数据的字段
      + relationship : 单纯表象两个模型间关系,不体现在数据库的表结构中,只为实现一对多查询更加方便
      + 一对一关系 : 增加列表项 `uselist=False`

   3. 一对多操作增加

      1. 使用外键字段增加数据

         ```python
         # 1. 增加职位,然后增加员工
         pos = Position(p_name="员工", p_level=1)
         pos.save()
         # 增加员工李四
         per = Person(username='李四', password="123456", nickname="小四", p_position=1)
         per.save()
         # 增加员工王五
         position = Position.query.filter_by(p_name="员工").first()
         per = Person(username='王五', password="123456", nickname="老五", p_position=position_id)
         per.save()
         ```

      2. 使用 relationship 正向操作 (relationship 所在模型到另一个模型) 增加数据

         ```python
         # 2. 增加员工小王 为小组长
         per = Person()
         per.username = "小王"
         per.password="12212"
         per.nickname = "王组长"
         # 不需要给外键字段赋值
         per.save()
         # 此操作将会删除之前的关系,重新建立关系
         pos = Position.query.filter(Position.p_name="小组长").first()
         pos.p_person = [per]
         pos.save()
         ```

      3. 使用 relationship 反向操作 (另一个模型到relationship 所在模型) 增加数据

         ```python
         # 3. 增加小二为主任
         per = Person()
         per.username = "小二"
         per.password="12212"
         per.nickname = "二主任"
         # 使用 backref 反向映射,值为职位对象
         # 此操作将会删除之前的关系,重新建立关系
         per.our_position = Position.query.filter_by(p_name="主任").first()
         per.save()
         ```

         

   4. 一对多查询

      ```python
      # 查询 id = 1 的员工的职位
      ## 反向操作
      person = Person.query.get(1)
      pos = person.our_position.p_name
      print(pos)
      # 查询员工职位的员工
      ## 正向操作
      pos = Position.query.get(1)
      person_list = pos.p_person
      print(person_list)
      ```

      

2. 多对多关系

   1. OA项目中的权限管理

      1. 主任 : 查看部门考勤、组织部门会议
      2. 经理 : 查看部门考勤、组织部门会议、招聘员工、开除员工
      3. 表一 : 描述职位 (职位名称、职位等级)
      4. 表二 : 描述权限 (权限名称)
      5. 多对多 : 同一职位可以有多个权限,一个权限可以给多个人

   2. 创建模型

      1. 中间表创建 (必须如此创建)

         ```python
         # 创建中间表
         pos_per = db.Table(
         	'pos_per',  # 表名
         	db.Column('pos_id', db.Integer, db.ForeignKey("position_id")),
         	db.Column('per_id', db.Integer, db.ForeignKey('permission.id')),
         )
         ```

      2. 创建职位表 (反向映射员工表与权限表)

         ```python
         # 创建职位表
         class Position(Base):
         	p_name = db.Column(db.String(32))
         	p_level = db.Column(db.Integer)
         	p_person = db.relationship(
         		"Person",
         		backref='our_position',
         	)
         	p_permission = db.relationship(
         		"Permission",
         		secondary=pos_per,
         		backref="p_position",
         	)
         ```

      3. 创建员工表 (外键连接职位表)

         ```python
         # 创建员工表
         class Person(Base):
         	username = db.Column(db.String(32), unique=True)
         	password = db.Column(db.String(64))
         	nickname = db.Column(db.String(32))
         	age = db.Column(db.Integer)
         	gender = db.Column(db.String(16))
         	score = db.Column(db.Float)
         
         	p_position = db.Column(db.Integer, db.ForeignKey("position.id"))
         ```

      4. 创建权限表

         ```python
         # 创建权限表
         class Permission(Base):
         	per_name = db.Column(db.String(256))
         ```

   3. 多对多操作增加数据

      1. 表中增加数据

         ```python
         # 插入权限
         p_list = [
             "查看部门考勤",
             "组织部门会议",
             "招聘员工",
             "开除员工",
         ]
         for per in p_list:
             p = Permission()
             p.per_name = per
             p.save()
             # 插入职位
             pos1 = Position(p_name="主任", p_level=1)
             pos2 = Position(p_name="经理", p_level=2)
             pos1.save()
             pos2.save()
         ```

      2. 正向操作增加关系

         ```python
         # 正向操作增加关系  Position -> Permission
         # 主任职位增加查看部门考勤权限
         pos = Position.query.filter(Position.p_name=="主任").first()
         per = Permission.query.filter(Permission.per_name=="查看部门考勤").first()
         pos.p_permission = [per]
         pos.save()
         ```

      3. 反向操作增加关系

         ```python
         # 反向操作,招聘员工权限中增加经理的角色
         per = Permission.query.filter(Permission.per_name=="招聘员工").first()
         pos = Position.query.filter(Position.p_name=="经理").first()
         per.p_position = [pos]
         per.save()
         ```

   4. 多对多操作查询

      ```python
      # 正向查询经理权限
      pos = Position.query.filter(Position.p_name=="经理").first()
      per = pos.p_permission
      print(per)
      # 反向查询拥有招聘员工的所有职位
      per = Permission.query.filter(Permission.per_name=="招聘员工").first()
      pos = per.p_position
      print(pos)
      ```

      