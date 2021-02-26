### Django

#### Django Form 请求

##### Django 请求

1. 常见的请求方式

   1. get : 默认请求方式,请求数据以明文形式存储在路由,get的格式是以 ? 开头,键值对形式,以&分隔每个键值对,常用于向服务器获取资源
   2. post : 请求数据隐藏发送,常用于向服务器提交资源

2. 请求对象

   + 视图函数中 request 是传递导视图的请求对象,包含请求的所有信息

   + request 对象类型是 "django.http.HttpRequest"

   + 常用属性

     | 常用属性及常用位置             | 描述                                |
     | ------------------------------ | ----------------------------------- |
     | `request.GET`(前端搜索功能)    | 获取 get 请求数据的方法             |
     | `request.POST`(后台注册)       | 获取 post 请求数据方法              |
     | `request.FILES`(后台注册)      | 获取文件上传请求数据的方法          |
     | `request.method`(后台注册)     | 获取请求的方法                      |
     | `request.META`                 | 获取请求的详细参数                  |
     | `request.META.OS`              | 获取请求端系统                      |
     | `request.META.HTTP_USER_AGENT` | 获取用户请求头,返回请求的浏览器版本 |
     | `request.META.HTTP_HOST`       | 获取请求的主机                      |
     | `request.META.HTTP_REFERER`    | 获取请求的来源                      |

##### Django 表单

1. HTML 表单 form

   | 属性          | 说明                             |
   | ------------- | -------------------------------- |
   | `action=""`   | 提交的地址,默认为当前路由        |
   | `method=""`   | 提交的方法,默认是 get            |
   | `name=""`     | 用来做传参的标识                 |
   | `type=submit` | 会自动提交当前表单数据到指定路由 |

   

2. 后端处理

   + CSRF 中间件 : 在 Django 1.4 版本之后 CSRF 在 setting 中默认开启,如果不开启会发生 CSRF 错误

     ```python
     MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'django.contrib.sessions.middleware.SessionMiddleware',
         'django.middleware.common.CommonMiddleware',
         
         'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 校验
         
         'django.contrib.auth.middleware.AuthenticationMiddleware',
         'django.contrib.messages.middleware.MessageMiddleware',
         'django.middleware.clickjacking.XFrameOptionsMiddleware',
     ]
     
     ```

     

   + CSRF 跨站请求伪造 : 利用当前浏览器还在生效的 cookie 对指定网站进行操作

   + **Django 的 CSRF 验证使用**

     1. 在 form 表单内部第一行, 插入 CSRF 校验, 使用 

        ```html
	// {% csrf_token %}
        <form action="" method='post'>
            {% csrf_token %}
            姓名: <input type='text' name='name'>
        </form>
        ```

     2. 返回 post 页面时一定要使用 **render** 方法,render 方法 与 render_response 方法功能类似,但是 render 会在第一个参数返回 request, 如果不返回 request, 前端无法使用 `{% csrf_token %}`

     3. `{% csrf_token %}` 标签实际是在前端 form 表单生成一个 hidden 隐藏域, name 为 csrf-middlewaretoken, value 值是 CSRF 校验值

##### Django 表单类

1. 表单类介绍

   1. Django 框架内部自带 Form 对象, Form 表单功能:

      1. 自动生成 HTML 表单元素
      2. 检查表单数据合法性
      3. 如果验证错误, 重新显示表单 (数据不重置)
      4. 数据类型转换 (字符串类型的数据转换成相应的 Python 类型)

   2. 前后端验证

      1. 前端验证 : Django 表单类对象渲染到模板后,会生成 附带属性标签的 HTML 对象,可以交互

      2. 后端验证 : 通过将 request 的参数传给 Form, 得到一个 Form 对象,调用这个对象的 is_valid 方法,如果返回为 True 表示通过验证,否则未通过验证

         ```python
         def reg_form(request):
             if request.method == 'POST':
                 # 校验请求
                 user_form = forms.UserForm(request.POST)
                 if user_form.is_valid():
                     # 获取校验过的数据
                     data = user_form.cleaned_data
                     name = data.get('name')
                     ...
                 else:
                     return render(request, 'register_form.html', {'user_form': user_form})
             return render(request, 'register_form.html')
         ```

2. 表单类使用

   1. 创建表单类 : forms.py

      ````python
      class SellerForm(forms.Form):
          username = forms.CharFiled(required=True, error_messages={'required': '必填'})
          password = forms.CharFiled(required=True, min_length=6, error_messages={'required': '必填', 'min_length': '长度至少为 6 位'})
      
      	def clean_username(self):
              username = self.cleaned_data.get('username')
              if 'sb' in username:
                  raise ValidationError('包含敏感词汇')
      ````

   2. 视图

   3. 模板 显示错误信息

      ```html
      <div class="form-group row">
          <div class="col-sm-11 mb-3 mb-sm-0">
              <input type="text" class="form-control form-control-user" name="username" id="exampleFirstName" placeholder="用户名" value="{{ seller_form.username.value }}">
              <span style="color: red">{{ seller_form.username.errors.0 }}</span>
          </div>
      </div>
      ```

      

##### Django 表单校验

1. 常用验证器

   1. 在验证某个字段时,除了直接使用不同的 Field 或者传递参数外,还可以通过传递一个 validators 参数用于指定验证器,进一步对数据进行过滤

   2. 实例

      ```python
      class SellerForm(forms.Form):
          username = forms.CharFiled(required=True, error_messages={'required': '必填'})
          password = forms.CharFiled(required=True, min_length=6, error_messages={'required': '必填', 'min_length': '长度至少为 6 位'})
          
          email = forms.CharField(
          	required=True,
              validators=[RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', '邮箱格式不正确')],
              error_messages={'required', '必填!'}
          )
      ```

   3. 常用验证器

      | 验证器                 | 描述                |
      | ---------------------- | ------------------- |
      | `MaxValueValidator()`  | 验证最大值          |
      | `MinValueValidator()`  | 验证最小值          |
      | `MinLengthValidator()` | 验证最小长度        |
      | `MaxLengthValidator()` | 验证最大长度        |
      | `EmailValidator()`     | 验证是否是邮箱格式  |
      | `URLValidator()`       | 验证是否是 URL 格式 |
      | `RegexValidator()`     | 正则表达式的验证    |

      

2. 自定义验证

   1. 自定义验证器 (类验证器: 调用时采用 `类验证器名()`,函数验证器: 调用时直接调用 `函数验证器名`)

      ```python
      # 定义类验证器
      class OurValid:
          def __call__(self, value):
              if 'sb' in username:
              raise ValidationError('不能包含敏感词汇')
      # 定义函数验证器
      def nextValid(value):
          if 'sb' in username:
              raise ValidationError('不能包含敏感词汇')
              
      class OurForm(forms.Form):
          name = form.CharField(
          	max_length=32,
              validators=[OurValid(), nextValid]
          )
      ```

      

   2. Django 表单类也提供了对特定字段的自定义验证,在 Form 类中定义实例方法,方法名是 `clearn_验证的字段名`, 如果验证失败,抛出 ValidationError 异常,否则正常返回值,在前端返回显示异常信息

      + views.py 自定义验证

        ```python
        def clean_username(self):
            username = self.cleaned_data.get('username')
            if 'sb' in username:
                raise ValidationError('不能包含敏感词汇')
        ```

        

      

##### Django 会话机制

1. cookie

   1. 设置时间 : 默认时间为 UTC ,与当前本地时间错了 8 小时

      ```
      TIME_ZONE = 'Asia/Shanghai'
      USE_TZ = False
      ```

   2. cookie 操作

      1. 创建 cookie (有效期单位为 秒): `response.set_cookie(键,值,有效期)`
      2. 删除 cookie : `response.delete_cookie(键)`
      3. 获取 cookie : `request.COOKIES.get(键)`

2. session

   1. session 在 Django 中默认配置存储在数据库
   2. session 操作
      1. 创建 session : `request.session[键]=值`
         + 有效期默认为两周,可以修改有效时间,单位为 秒 : `request.session.set_expiry(时间)`
      2. 获取 session : `request.session.get(键)`
      3. 删除 session 
         1. 删除一个键值对 : `del request.session[键]`
         2. 删除所有键值对 : `request.session.clear()`
   3. 服务器获取不到 session 的几种情况
      1. 客户端没有发送 sessionid
      2. 客户端发来 sessionid , 但未在数据库中找到
      3. 客户端发来 sessionid , 从数据库中找到了, 但是过期了

3. 案例: 权限设置,如果未登录则不能访问任何后台的路由

   1. 登陆成功后保存 session
   2. 在首页 view 验证 session
   3. 编写装饰器代码
   4. 使用装饰器
   5. 退出登录成功

##### 设置后台访问权限

1. 方式一 : 对每一个页面进行判断,十分繁琐

2. 方式二 : 使用装饰器判断

   ```python
   def check_login(func):
   	def inner(request):
   		seller_name = request.COOKIES.get('seller_name')
   		if seller_name:
   			return func(request)
   		else:
   			return redirect('seller/login/')
   	return inner
   ```

3. 方式三 : 使用中间件

