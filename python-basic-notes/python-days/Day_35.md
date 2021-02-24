### Flask 数据库与请求

#### Flask 请求

##### 常见的请求方式

1. get : 默认是 get 请求,请求数据以明文形式放到路由上,get 的格式是以 "?" 开头,键等于值的键值对形式用 "&" 分隔不同键值对,

   + 常用于向服务器获取资源

     ```
     https://127.0.0.1/s?wd=张三&rsv_spt=1
     ```

2. post : 请求数据隐藏发送,安全系数更高.

   + 常用于向服务器提交资源

##### 请求对象

+ 导入 flask 的 request 模块,通过request 的属性,获取请求的信息 `from flask import request`
+ 重定向 : `from flask import redirect`
+ 常用属性

  | Request 参数 | 定义                                                       |
  | ------------ | ---------------------------------------------------------- |
  | args         | 接收 get 请求参数                                          |
  | data         | 接收所有请求参数,是请求体的原始数据                        |
  | files        | 接收文件数据                                               |
  | form         | 接收 post 请求数据                                         |
  | method       | 请求方式                                                   |
  | referrer     | 请求来源                                                   |
  | url          | 统一资源定位符 `http://127.0.0.1:8000/get_test/?name=张三` |
  | host         | `127.0.0.1:8000`                                           |
  | host_url     | `http://127.0.0.1:8000`                                    |

##### Form 表单

+ 表单属性

  + action : 提交的地址,默认是当前路由
  + method : 提交的方法,默认是 get
  + input : 表单的元素
  + name : 参数,用来做传参的值
  + submit : 自动提交当前表单数据

+ form 表单 get 请求

  ```python
  @app.route('/index/')
  def index():
      get_arg = request.args  # 接收 get 请求参数
      keywords = get_arg.get("keywords")
      # 模糊查询
      r = f"{keywords}%"
      persion_list = Person.query.filter(Person.nickname.like(r))
      # persion_list = Person.query.filter(Person.nickname.like("王"))
      
      return render_template("index.html", **local())
  ```

+ form 表单 post 请求 (完善 OA 的人员添加)

  ```python
  @app.route('/add_permission/', methods=['GET', 'POST'])
  def add_permission():
      if request.method == 'POST':
          print(request.form)
          print(request.form.get('name'))
          print(request.method)
          # 提交后再次访问此页面
          return redirect('/add_permission/')
      return render_template("add_permission.html")
  ```

+ 图片上传

  + 前端添加上传图片的表单

  + 后端视图保存图片
    + 通过 request.files 获取上传文件
    + 将文件保存至服务器
    + 数据库中保存文件路径

##### 会话机制

+ 会话 : 数据交互的一次过程.从浏览器发起请求到浏览器关闭,这样的一次交互叫会话.当交互过程中有很多状态和数据需要记录,而且 HTTP 请求都是无状态的,与前后请求都无关,请求者身份默认都是匿名的,这样使得访问缺乏连续性,同一个网站无法识别访问者身份,局限了 Web 开发。

+ Web 开发的会话技术

  1. cookie : 在浏览器请求的时候,服务器下发的保存在浏览器本地的用于识别用户身份的小文本;让浏览器的访问有很好的连续性,可以有身份的访问

     1. cookie 的安全隐患 : cookie 存放在用户本地,很容易被修改和盗用

     2. 创建 cookie: `.set_cookie(键, 值, 有效期)`

        | 参数    | 介绍                                                         |
        | ------- | ------------------------------------------------------------ |
        | key     | 设置 cookie 的 key                                           |
        | value   | 设置 cookie 的 value                                         |
        | max_age | 改 cookie 的过期时间,默认为浏览器关闭则自动过期,有效期单位是 s |
        | expires | 过期时间,是一个 datetime 类型                                |
        | domain  | 该cookie 有效的域名,一般设置子域名                           |
        | path    | cookie 的有效路径                                            |

        ```python
        from flask import make_response
        @app.route("/setcookie/")
        def setcookie():
            # Django 在 响应对象中设置 cookie
            response = make_reponse("hello")
            response.set_cookie("name", "张三", max_age=1000)
            return response
        ```

     3. 删除 cookie : `.delete_cookie("name")`

        ```python
        from flask import redirect
        @app.route("/deletecookie/")
        def deletecookie():
            # 删除 cookie
            response = redirect('/index/')
            response.delete_cookie("name")
            return response
        ```

     4. 获取 cookie : `request.cookies.get("name")`

        ```python
        @app.route("/getcookie/")
        def getcookie():
        	# 导入 request
        	# 获取 cookie
        	data = request.cookies
        	print(data)
        	name = data.get("name")
        	# name = request.cookies.get("name")
        	print(name)
        	return "获取cookie"
        ```

  2. session