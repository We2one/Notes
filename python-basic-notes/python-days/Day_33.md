#### Flask 框架

+ 框架: 框架是一个半成品，已经对基础的代码进行了封装并提供相应的 API ，开发者在使用框架是直接调用封装好的 API 可以省去很多代码编写, 从而提高工作效率和开发速度

#### Flask 的模板系统

+ Flask 默认采用 Jinja2 模块进行模板渲染,Jinja2 通常用于 Flask、Tornado 框架中
+ static : 静态文件,Flask 默认加载当前目录下的 static 目录下的静态文件
+ templates : 模板文件,Flask 默认加载当前目录下的 templates 目录下模板文件

##### Flask 程序内部

1. 路由

   + 路由使用装饰器的形式定义,必须以`/`开头,否则报错 `ValueError: urls must start with a leading slash`
   + `@app.route('/index/')`

2. 视图函数

   + 路由之下定义的函数 : 处理用户请求,返回响应的函数代码块
   + 视图函数名不能重复,否则报错 `AssertionError: View function mapping is overwriting an existing endpoint function: index`

3. 启动服务器 run

   | run 参数            | 说明                                                         |
   | ------------------- | ------------------------------------------------------------ |
   | `host="0.0.0.0"`    | 主机地址,默认是 127.0.0.1<br/>允许外部可访问: 0.0.0.0        |
   | `port=端口号`       | 默认为 5000                                                  |
   | `debug=True`        | 调式模式,默认为False<br/>开发的时候一般设置为 True 如果视图有错,可以在浏览器报错,并且会定时更新页面<br/>设置时不用设置 use_reloader |
   | `use_reloader=True` | 是否自动重启代码,默认为 False                                |

   

4. URL 路径参数,多用于二级路径,动态加载路由

   + 可以通过请求的 URL 中获取需要的参数

     ```
     @app.route('/index/<id>')
     ```

   + `<>` : 转换器语法,默认为字符串类型 (匹配到的内容类型始终为字符串类型)

   + 转换器语法

     | 转换器类型        | 使用            |
     | ----------------- | --------------- |
     | string 字符串类型 | `<string:name>` |
     | int 整数类型      | `<int:data>`    |
     | float 浮点类型    | `<float:data>`  |
     | path 路径类型     | `<path:data>`   |

     

##### 调用静态页面 

1. 新建 templates 目录 --> 存放 HTML 文件

2. 调用静态页面

   + 使用模块 `from flask import render_template`

     ```python
     @app.route('/')
     def hello_world():
     	return render_template("xxx.html")
     ```

     

##### 视图传递参数到模板

1. 单独传递

   ```
   @app.route('/')
   def hello_world():
   	name = "张三"
   	age = 18
   	return render_template("xxx.html", name=name, age=age)
   ```

   ```
   <!--xxx.html-->
   <body>
   	<p>姓名: {{ name }}</p>
   	<p>年龄: {{ age }}</p>
   </body>
   ```

2. 序列解包，传递所有参数

   ```
   @app.route('/')
   def hello_world():
   	name = "张三"
   	age = 18
   	return render_template("xxx.html", **locals())
   ```

   ```
   <!--xxx.html-->
   <body>
   	<p>姓名: {{ name }}</p>
   	<p>年龄: {{ age }}</p>
   </body>
   ```

##### 模板语法

1. 变量的使用

   + 语法 : `{{ 变量 }}`

     ```
     hobby = ["sing", "writing", "reading"]
     score = {"python": 100, "java": 120, "c++": 150}
     
     class Persion:
     	def __init__(self, name, age):
     		self.name = name
     		self.age = age
         def show():
         	return f"name={self.name}, age={self.age}"
         	
     persion = Persion("张三", 15)
     ```

     + `{{ 变量名, 索引 }}` 或 `{{ 变量名[索引] }}` : 索引获取可迭代元素

       ```
       {{ hobby, 2 }} // "reading"
       {{ hobby[2] }} // "reading"
       ```

     + `{{ 变量名["key值"] }}` : key 获取 字典内的值

       ```
  {{ score["java"] }}
       ```
     
     + `{{ 初始化类名.参数名 }}` : 获取类内参数 (类变量)

       ```
  {{ persion.name }}
       ```

     + `{{ 初始化类名.类方法名() }}` : 获取类方法返回值 (类方法使用)
     
       ```
  {{ persion.show() }}
       ```

   + 使用 python 内置方法 --> upper, replace, lower 等

2. 控制语句

   1. if 控制语句

      + 语法结构
        + `{% if 条件 %} {% endif %}`
        + `{% if 条件 %} {% else %} {% endif %}`
        + `{% if 条件 %} {% elif 条件 %} {% else %} {% endif %}`

   2. for 循环 --> 迭代 Python 中数据类型,包括列表、元组和字典

      1. 迭代列表

         ```
         {% for i in list %}
         	{{ i }}
         {% endfor %}
         ```

      2. 迭代字典

         ```
         {% for key,value in dict.items() %}
         	{{ key }}: {{ value }}
         {% endfor %}
         ```

      3. loop 获取 for 循环遍历状态

          

         | 方法           | 说明                            |
         | -------------- | ------------------------------- |
         | `loop.index`   | 当前迭代的索引(从1开始)         |
         | `loop.index()` | 当前迭代的索引(从0开始)         |
         | `loop.first`   | 是否是第一次迭代,返回 bool 值   |
         | `loop.last`    | 是否是最后一次迭代,返回 bool 值 |
         | `loop.length`  | 序列中项目数                    |

3. 过滤器 -- (本质是函数,可以通过过滤器将视图传递的值进行修改显示的效果)

   + 常用过滤器

     | 方法                                                    | 说明                    |
     | ------------------------------------------------------- | ----------------------- |
     | `{{ "abc" | capitalize }}`                              | 首字母大写,其他字母小写 |
     | `{{ "abc" | lower }}`                                   | 全转换为小写字母        |
     | `{{ "abc" | upper }}`                                   | 全转换为大写字母        |
     | `{{ "abc" | title }}`                                   | 每个单词的首字母都大写  |
     | `{{ "hello world" | replace("hello", "run") | upper }}` | 替换字符串              |
     | `{{ 18.18 | round | int }}`                             | 数字四舍五入            |
     | `{{ "<p>你好</p>" | safe }}`                            | 渲染时值不转义          |

   + 自定义过滤器

     + python 编写函数

       ```
       def add(num1, num2, num3):
       	return num1+num2+num3
       app.add_template_filter(add, "Add")
       ```

     + HTML 页面引用

       ```
       {{ value | add(1, 2, 3) }}
       ```

##### 模板继承和加载

1. 继承

   + 对一个网站中重复部分单独写一个 HTML 文件,为了防止冗余,直接继承父网页大部分样式,然后添加新的功能
   + 定义父模板, 在父模板中用 block 定义 可继承部分
     1. block 定义可修改部分 : `{% block block_name %} 定义内容 {% endblock %}`
   + 定义子模板,继承父模板,根据需要在字模板中修改父模板中的 block
     1. 继承父模板 : `{% extends "xxx.html" %}`
     2. 修改父模板中 block : `{% block block_name %} 修改内容 {% endblock %}`

2. include 包含

   + 将常用页面的常用内容 (eg: 导航栏,页尾信息等) 不变的组件保存在单独的 HTML 文件中,然后在需要的地方引用
   + 引用 : `{% include 'xxx.html' %}`

   