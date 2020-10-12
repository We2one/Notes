### Django

#### Django 数据库操作

##### Django ORM 单表操作

+ Django 可以通过开启命令行模式对模型 (models) 进行操作  : `python manage.py shell`

+ 操作方法

  1. 增加操作

     1. `类名.objects.create(属性名称=xxx)` : create 方法增加数据

     2. `save()` : save 方法上传修改

     3. 实例

        ```
        obj = models.类()
        obj.属性名 = "xxx"
        ...
        obj.save()
        ```

  2. 删除操作

     1. 使用 delate 方法
        1. 方法一 : `类名.objects.get("xxx").delete()`
        2. 方法二 : `类名.objects.filter("xxx").delete()`

  3. 修改操作

     1. 使用 update 方法 (不能用 get 方法) : `类名.objects.filter("xxx").update(name="xxx")`

     2. 使用 save 方法

     3. 实例

        ```
        obj = 类名.objects.get("xxx")
        obj.name = "xxx"
        ...
        obj.save()
        ```

  4. 查询操作

     1. get 方法 : 返回一个与给定筛选条件相匹配的对象

        + 返回结果有且只有一个,如果有多个符合筛选条件的对象或者没有符合筛选条件的 **报错**
        + 返回的是具体某个模型类的**对象**，而不是 QuerySet 列表对象

     2. filter 方法 : 返回包含了与所给筛选条件相匹配的对象

        + 返回 QuerySet 列表对象.获取每个对象时,通过索引或便利
        + 可以传入多个关键字,底层的 sql 使用 and 来连接多个条件

     3. all 方法 : 返回 所有 QuerySet 列表对象.获取具体每个对象时 通过索引或者遍历

     4. order_by 方法 : 对查询结果排序

        1. 正向排序

           ```python
           StoreUser.objects.order_by("id")
           ```

           

        2. 反向排序,在字段前添加 "-"

           ```python
           StoreUser.objects.order_by("-id")
           ```

     5. first 方法 : 返回第一条记录,返回具体的某个模型类对象 (object),而不是 QuerySet 列表对象

     6. last 方法 : 返回最后一条记录,返回具体的某个模型类对象 (object),而不是 QuerySet 列表对象

  5. 双下划线查询

     | 条件           | 描述                                         | 举例                                                 |
     | -------------- | -------------------------------------------- | ---------------------------------------------------- |
     | `__gt`         | 大于                                         | `StoreUser.objects.filter(id__gt=4)` <==> `id > 4`   |
     | `__lt`         | 小于                                         | `StoreUser.objects.filter(id__lt=4)` <==> `id < 4`   |
     | `__gte`        | 大于等于                                     | `StoreUser.objects.filter(id__gte=4)` <==> `id >= 4` |
     | `__lte`        | 小于等于                                     | `StoreUser.objects.filter(id__lte=4)` <==> `id <= 4` |
     | `__contains`   | 模糊查询,相当于 SQL 语句中的 like(%keyword%) | `StoreUser.objects.filter(phone__contains="135")`    |
     | `__in`         | 判断在范围                                   | `StoreUser.objects.filter(id__in=[1, 2, 3])`         |
     | `__isnull`     | 判断为空                                     | `StoreUser.objects.filter(phone__isnull=Flase)`      |
     | `__startswith` | 获取指定内容开头的记录                       | `StoreUser.objects.filter(phone__startswith="13")`   |

  6. 聚合查询 : MySQL 中的 max、min、sum、avg、count

     + 导包 : `from django.db.models import Sun, Avg, Max, Min, Count`
     + 依赖 : aggregate 是 Django ORM 中的终止语句

  7. 分组查询 (annotate()) 

     + 按照年龄和性别统计用户个数

       ```
       StoreUser.objects.all().values('age').annotate(count('age'))
       StoreUser.objects.all().values('gender').annotate(count('gender'))
       ```

  8. F 查询 : 在查询中, F() 的实例引用一个模型字段.在查询过滤器中也可以这样引用,以便比较同一个模型实例中的两个字段 **用于同一用户的不同信息查询、比较**

     + 引入 F 查询 : `from django.db.models import F`

     + F 查询 年龄 大于 会员等级的用户

       ```
       from django.db.models import F
       
       result = StoreUser.objects.filter(age__gt = F('level')).all()
       ```

       

  9. Q 查询 : filter() 查询是 并联查询,如果需要使用 or、and、not 需要使用 Q 对象

     + 引入 Q 查询 : `from django.db.models import Q`

     + `|` : 或 or

     + `&` : 且 and

     + `~` : 非 not

     + 案例

       1. 查询所有 19 岁的男生

          ```
          StoreUser.objects.filter(age = 19, gender='男')
          ```

       2. 查询所有 19 岁的用户 或男用户

          ```
          StoreUser.object.filter(Q(age=19) | Q(gender='男')).all()
          ```

       3. 查询所有不是 19 岁的员工

          ```
          StoreUser.objects.filter(~Q(age=19)).all()
          ```

          

  10.  Djamgo 分页 : Django 本身携带分页函数,可以自动分页,但是也有限制查的方法,使用索引

      ```
      StoreUser.objects.filter(~Q(age=19))[10]
      ```

      

##### Django 关系操作

1. 一对一 (OneToOneField)

   1. `models.OneToField()` 参数

      | 字段参数              | 描述                                                         |
      | --------------------- | ------------------------------------------------------------ |
      | `to=关联表`           | 设置要关联的表                                               |
      | `to_field=关联字段名` | 设置要关联的字段                                             |
      | `on_delete=处理办法`  | 如果删除关联表之后的处理办法<br>1. `models.CASCADE` : 级联删除,删除关联表后删除此表<br>2. `models.DO_NOTGING` : 不做处理 |

   2. 卖家与店铺一对一

      1. 实例

         ```python
         class StoreUser(models.Model):
             ...
         
             
         class Store(models.Model):
             ...
             store_user = models.OneToOneField(to=StoreUser, on_delete=models.CASCADE)
         ```

      2. 增加店铺

         ```python
         from Store.models import Store
         
         store = Store()
         store.store_name = "早餐店"
         store.store_description = "包子"
         store.store_logo = "img/1.png"
         store.store_address = "北京"
         store.store_user = StoreUser.objects.get(id=1)
         ```

      3. 映射查询

         1. 查询张三的店铺, 从 StoreUser 查 Store 

            ```python
            zhangsan = StoreUser.objects.filter(username="张三")
            print(zhangsan.store.store_name)
            ```

         2. 查询早餐店主人, 从 Store 查 StoreUser

            ```python
            store = Store.objects.get(id=1)
            print(store.store_name.nick_name)
            ```

            

2. 一对多 (ForeignKey)

   1. `models.ForeignKey()`

   2. 商品和店铺一对多

      1. 实例

         ```python
         class GoodsType(models.Model):
             t_name = models.CharField(max_length=32)
             
         class Goods(models.Model):
             g_name = models.CharField(max_length=32)
             g_price = models.FloatField()
             goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)
         ```

      2. 添加商品并关联商品类型

         ```python
         goods = Goods()
         goods.g_name = "苹果"
         goods.g_price = 12.3
         goods.goods_type = GoodsType.objects.get(id=1)
         goods.save()
         ```

      3. 映射查询

         1. 查询物品类型, 从 Goods 表查 GoodsType 表

            ```python
            goods = goods.objects.get(id=1)
            print(goods.goods_type.t_name)
            ```

         2. 查询商品类型对应商品,从 GoodsType 表查 Goods 表 (先获取类型,在获取 `类型名.小写关联表名_set.all()`)

            ```python
            goods_type = GoodsType.objects.get(id=1)
            # 获取该类型所有对应商品
            print(goods_type.goods_set.all())
            ```

            

3. 多对多 (ManyToManyField)

   1. `models.ManyToManyField()`

   2. 商品类型和店铺多对多 (一个店铺有多种类型的商品,一个商品类型在多个店铺售卖)

      1. 实例

         ```python
         class Store(models.Model):
             ...
             store_user = models.OneToOneField(to=StoreUser, on_delete=models.CASCADE)
             
         class GoodsType(models.Model):
             t_name = models.CharField(max_length=32)
             
             t_store = models.ManyToManyField(to=Store)
         ```

      2. 添加类型

         ```python
         goods_type = GoodsType()
         goods_type.t_name = "烧烤"
         goods_type.save()
         ```

      3. 类型关联店铺

         ```python
         goods_type = GoodsType.object.get(id=1)
         goods_type.t_store.add(Store.object.get(id=1))
         goods_type.save()
         ```

      4. 映射查询

         1. 查询店铺对应类型, 从 Store 表 查 GoodsType 表

            ```python
            store = Store.objects.get(id=1)
            print(store.goodstype_set.all()) # 获取的是可迭代数据
            for one in store.goodstype_set.all():
                print(one.t_name)
            ```

            

         2. 查询类型对应店铺, 从 Goods.Type 表 查 Store 表

            ```python
            goods_type = GoodsType.objects.get(id=2)
            store = goods_type.t_store.all()
            for one in store:
                print(one.store_name)
            ```

            

         

#### MVC 和 MVT 架构模式

##### MVC 架构模式

+ MVC (Model View Controller) : 分为三个基本部分 : 物理 Model、视图 View 和 控制器 Controller
  + M : Model (模型),代表数据存储层,和数据库进行交互
  + V : View (视图),产生 HTML 页面,代表系统中选择显示什么和怎么显示
  + C : Controller (控制器),接受请求,进行处理,与 M、V 进行交互,返回响应

##### MVT 架构模式

+ MVT (Model View Templates) : Django 框架分为三部分 : Model 模型、Template 模板、View 视图
  + Model (模型) : 负责业务对象与数据库的对象 (ORM)
  + View (视图) : 负责业务逻辑,并在适当的时候调用 Model 和 Templates
  + Templates (模板) : 负责把页面展示给用户

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

     1. 在 form 表单内部第一行, 插入 CSRF 校验, 使用 `{% csrf_token %}`

        ```html
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

      ```python
      class SellerForm(forms.Form):
          username = forms.CharFiled(required=True, error_messages={'required': '必填'})
          password = forms.CharFiled(required=True, min_length=6, error_messages={'required': '必填', 'min_length': '长度至少为 6 位'})
      
          
      	def clean_username(self):
              username = self.cleaned_data.get('username')
              if 'sb' in username:
                  raise ValidationError('包含敏感词汇')
      ```

      

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

      