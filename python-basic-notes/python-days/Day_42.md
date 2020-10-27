### Django

#### Django 接口开发

##### 前后端分离

+ 传统开发模式

  + url  ---> 视图函数 (逻辑判断、调用数据库、渲染 HTML)  ---> 向浏览器返回 HTML 页面

    ```python
    # views.py
    def more_goods_list(request):
    	goodstype_id = request.GET.get('goodstype_id')
    	goods_obj_list = Goods.objects.filter(goodstype_id=goodstype_id)
    	return render(request, 'buyer/list.html', {'goods_obj_list': goods_obj_list, 'goodstype_id': goodstype_id})
    ```

    

+ 前后端分离模型

  + 后端只负责返回数据 (一般返回数据类型为 JSON 或 XML),不再负责渲染页面,前端负责渲染数据

    1. Vue.js技术,将后台传递给前端的数据渲染到页面

    2. 使用 JsonResponse 将字典数据转换为 JSON 格式 ，后台返回 JSON 数据给前端 

       ```python
       def more_goods_list_ajax(request):
       	goodstype_id = request.GET.get('goodstype_id')
       
       	goods_obj_list = Goods.objects.filter(goodstype_id=goodstype_id)
       
       	goods_dic_list = []
       	for goods_obj in goods_obj_list:
       		dic = {'name': goods_obj.name, 'img': goods_obj.image.name, 'price': goods_obj.price}
       		goods_dic_list.append(dic)
       
       	return JsonResponse(goods_dic_list, safe=False)
       ```

       

##### JSON 和 XML

+ JSON (JavaScript Object Notation) : 轻量级的数据交换格式, 类似于 python 中的字典

  1. JSON 和 Python 字典数据类型对应

     | Python           | JSON   |
     | ---------------- | ------ |
     | dict             | object |
     | list,tuple       | array  |
     | str, unicode     | string |
     | int, long, float | number |
     | True             | true   |
     | False            | false  |
     | None             | null   |

+ XML (Extensible Markup Language) : 可拓展标记语言,很少使用 XML 数据传输

+ JsonResponse 对象 : 可以将 Python 中的字典或者其他数据类型转换为 JSON 数据

  ```python
  from django.http import JsonResponse
  
  def getdata(request):
      user_list = [
          {'name': '张三', 'age': 18},
          {'name': '李四', 'age': 22},
          {'name': '王五', 'age': 24},
      ]
      return JsonResponse(user_list, safe=False)
  ```

##### AJAX

1. AJAX 介绍

   + AJAX (Asynchronous Javascript And XML) : 异步 JavaScript 和 XML (即 用 JavaScript 语言与服务器进行异步交互, 传输的数据为 XML 和 JSON)
   + AJAX 特点 : 当服务器响应时,不用刷新整个页面,可以实现局部刷新
   + 应用场景 : 注册时信息校验

2. AJAX 格式 (多使用 jQuery 实现 AJAX 请求)

   1. 语法

      ```
      $.ajax({
      	参数1: 值1,
      	参数2: 值2,
      	参数3: 值3,
      	...
      })
      ```

   2. 参数介绍

      | 参数     | 描述                                                         |
      | -------- | ------------------------------------------------------------ |
      | url      | 发送请求的地址                                               |
      | type     | 请求方式('POST'或'GET'),默认为 'GET'.其他 HTTP 请求方法也可以使用,但在部分浏览器可能不支持 |
      | data     | 发送到服务器的数据,格式 : {key: value, key: value}           |
      | error    | 请求失败时调用的函数                                         |
      | success  | 请求成功后的回调函数.参数:由服务器返回数据                   |
      | dataType | 预期服务器返回数据类型,不指定浏览器将自动判断<br/>&emsp;1. "xml" : 返回 XML 文档, 可用 jQuery 处理<br/>&emsp;2. "html" : 返回纯 HTML 信息<br/>&emsp;3. "script" : 返回纯 JavaScript 代码<br/>&emsp;4. "json" : 返回 JSON 数据 |

      

##### Vue 前端渲染

1. Vue 介绍

   + Vue 是一套用于构建用户界面的 JavaScript 框架,前端使用 Vue 的目的就是把 AJAX 里面的数据绑定到前端

2. Vue 基本语法

   1. 下载引入

   2. 第一个应用

      + Django 中 使用 Vue 是会发生语法冲突,需要增加标签 verbatim 处理

        ```
        {% verbatim %}
        	<div id='app'>
        		{{ message }}
        	</div>
        {% endverbatim %}
        ```

      + Vue.js 的应用可以分为 2 个重要部分 : 视图(HTML 代码)、脚本

        + 视图

          ```
          {% verbatim %}
          	<div id='app'>
          		{{ message }}
          	</div>
          {% endverbatim %}
          ```

        + 脚本

          ```
          <script>
          	new Vue({
          		el: "#app",  // id 选择器
          		data: {
          			message: "hello world",
          		}
          	})
          </script>
          ```

          

      + 注意事项

        1. 引入 Vue.js 脚本文件
        2. 创建视图部分
        3. 创建脚本 Vue 对象
        4. 注意 : 变量仅可以在选择器范围内使用

   3. 常用的基本语法

      1. 插值操作 : 将 Vue 对象中的数据显示到页面上. "Mustache" 语法 (双大括号语法) 的文本插值,将数据显示到 HTML 页面中

      2. v-bind : "Mustache" 不能作用在 HTML attribute 上,遇到此情况应该使用 v-bind 指令

         ```
         <body>
         	<div id="app">
         		<a v-bind:href="url">点击<a>
         	</div>
         </body>
         <script>
         	new Vue({
         		el: "#app",
         		data: {
         			url: "http://www.baidu.com",
         	})
         </script>
         ```

         

      3. v-if : 用于条件性的渲染一块内容.此内容只在指令的表达式返回 true 值是被渲染

         ```
         <body>
         	<div id="app">
         		<p v-if="true">{{ msg }}</p>
         		<p v-if="false">{{ msg }}</p>
         		<p v-if="0">{{ msg }}</p>
         		<p v-if="10">{{ msg }}</p>
         		<p v-if="aa">{{ msg }}</p>
         	</div>
         </body>
         ```

         

      4. v-for : 类似于确定是数值否在一定范围内,为 True 显示数据

         ```
         <body>
         	<div id="app">
         		<ul>
         			<li v-for="game in games">{{ game }}</li>
         		</ul>
         		<ul>
         			<li v-for="(game, index) in games">{{ index }} -- {{ game }}</li>
         		</ul>
         	</div>
         </body>
         <script>
         	new Vue({
         		el: "#app",
         		data: {
         			games: ['lol', 'DNF', 'CF'],
         	})
         </script>
         ```

         

      5. v-on : 监听 DOM 事件,并在触发时运行一些 JavaScript 代码

         ```
         <body>
         	<div id="app">
         		<ul>
         			<li v-on=click="onLoad">{{ message }}</li>
         		</ul>
         	</div>
         </body>
         <script>
         	new Vue({
         		el: "#app",
         		data: {
         			message: "hello world",
         			methods: {
         				onLoad:function(){
         					alter('hello world');
         				}
         			}
         	})
         </script>
         ```

         

##### REST

+ REST (Representational State Transfer , 变现层状态转移) 与技术无关, 是一种软件架构风格、设计风格,不是标准,只是一组设计原则和约束条件

+ 使用 REST 风格设计的软件可以更加简洁、更有层次感、更易于实现存储

+ RESTful : 满足约束条件和原则的应用程序或设计

+ 10 条规则

  1. 协议 : API 与用户的通信协议,总是使用 HTTPS 协议

  2. 域名 : 在域名上区分不同文件

     + 子域名方式区分
       1. 'www.xxx.com' : 访问网站
       2. 'api.xxx.com' : 返回 接口数据 (JSON 或 XML)
     + Url 区分
       1. 'www.xxx.com' : 访问网站
       2. 'www.xxx.com/api/' : 添加一个 api 目录, 返回接口数据

  3. 版本 : 在 URL 上添加版本以区别不同版本程序 'www.xxx.com/app/v1.0'

  4. 路径 : 网络上任何东西都是资源,均使用名词表示 ,减少使用 类似 'getuser' 之类的动词使用

  5. HTTP 动词 : 对资源的具体操作类型

     + 常用 HTTP 动词 <=对应=> SQL 命令
       1. GET <==> SELECT : 从服务器取出资源 (一项或多项)
       2. POST <==> CREATE : 在服务器新建一个资源
       3. PUT <==> UPDATE : 在服务器更新资源 (客户端提供改变后的完整资源)
       4. DELETE <==> DELETE : 从服务器删除数据
     + 3 个不太常用的 HTTP 动词
       1. PATCH <==> UPDATE : 在服务器更新资源 (客户端提供改变的属性)
       2. HEAD : 获取资源的元数据
       3. OPTIONS : 获取信息,关于资源的那些属性是客户端可以改变的

  6. 过滤信息 : 如果记录很多,服务器不会全部返回数据给用户,API 应该提供参数,过滤返回结果

     + 常见参数

       | 参数                     | 描述                                                     |
       | ------------------------ | -------------------------------------------------------- |
       | `?limit=10`              | 指定返回记录数量                                         |
       | `?offset=10`             | 指定返回记录的开始位置                                   |
       | `?page=2&per_page=10`    | 指定第几页以及每页的记录数                               |
       | `?sortby=name&order=asc` | 指定返回结果按照那个属性进行排序,以及排序规则 (顺序倒序) |
       | `?animal_type_id=1`      | 指定筛选条件                                             |

  7. 状态码 : 服务器向用户返回状态码和提示信息

     ​	

     | 状态码                                       | 描述                                                         |
     | -------------------------------------------- | ------------------------------------------------------------ |
     | `200 OK - [GET]`                             | 服务器成功返回用户请求的数据                                 |
     | `201 CREATED - [POST/PUT/PATCH]`             | 用户新建或修改数据成功                                       |
     | `202 Accepted - [*]`                         | 表示一个请求已进入后台排序 (异步任务)                        |
     | `204 NO CONTENT - [DELETE]`                  | 用户删除数据成功                                             |
     | `400 INVALID REQUEST - [POST/PUT/PATCH]`     | 用户发出请求有误,服务器没有进行新建或修改数据操作            |
     | `401 Unauthorized - [*]`                     | 表示用户没有权限 (令牌、用户名、密码错误)                    |
     | `403 Forbidden - [*]`                        | 表示用户得到授权 (与 401 错误相对),但是禁止访问              |
     | `404 NOT FOUND - [*]`                        | 用户发出的请求针对的是不存在的记录,服务器没有进行操作,该操作是幂等的 |
     | `406 NOT Acceptable - [GET]`                 | 用户请求的格式不可得 (如用户请求 XML 格式 只有 JSON 格式)    |
     | `410 Gone - [GET]`                           | 用户请求的资源被永久删除,且不会再得到                        |
     | `422 Unprocesable entity - [POST/PUT/PATCH]` | 当创建一个对象时,发生一个验证错误                            |
     | `500 INTERNAL SERVER ERROR - [*]`            | 服务器发生错误,用户将无法判断发出的请求是否成功              |

     

  8. 错误处理 : 如果状态码是 4xx, 服务器就应该向用户返回出错信息.一般来说,返回的信息中 error 作为键名,出错信息作为键值即可 `{error: 'Invalid API key'}`

  9. 返回结果 : 针对不同操作,服务器向用户返回的结果应符合以下规范

     1. GET	/collection	: 返回资源对象列表 (数组)
     2. GET    /collection/resource    : 返回单个资源对象
     3. POST    /collection    : 返回新生成的资源对象
     4. PUT    /collection/resource    : 返回完整的资源对象
     5. PATCH    /collection/resource    : 返回完整的资源对象
     6. DELETE    /collection/resource    : 返回一个空文档

  10.  超媒体 : 即 返回结果中提供链接,连向其他 API 方法, 是用户不查文档也可以找到下一步 API

  11.  其他 : 服务器返回的数据格式, 尽量使用 JSON 数据, 避免使用 XML

##### FBV (基于函数的视图) 和 CBV (基于类的视图)

1. FBV : 函数至少有一个参数 request, 表示当前请求对象

2. CBV : 视图类必须直接或间接继承 django.views.View 类, 定义方法表示接受对应的请求 (方法中 request 表示请求对象, *args 与 *kwargs 用来接收)

   ```python
   from django.views import View
   
   class GoodsView(View):
   	def get(self, request, *args, *kwargs):
   		pass
       
   # 视图类
   urlpatterns = [
       path('xxxx/xxx/', GoodsView.view.View)
   ]
   ```

   

3. SCRF 拦截 : Django 的 CSRF 不回拦截 GET 请求, POST、PUT、DELETE都会拦截,可以使用 postman 工具测试拦截情况

   + 使用 csrf_exempt 装饰器,去掉 CSRF 拦截, 先调用 dispatch 方法,然后根据不同的请求,调用对应的方法,再次使用 postman 测试

     ```python
     from django.views.decorators.scrf import csrf_exempt
     from django.utils.decorators import method_decorator
     
     @csrf_exempt
     def goods(request):
         pass
     
     from django.views import View
     
     @method_decorator(csrf_exempt, 'dispatch')
     class GoodsView(View):
         def get(self, request, *args, **kwargs):
             return HttpResponse("get 请求")
     ```

     

##### Django REST Framework 框架

1. 安装 DRF 框架

   1. 安装 : `pip install djangorestframework`

   2. 在 `setting.py` 内注册 app

      ```python
      INSTALLED_APP = [
          ...
          'rest_framework',
      ]
      ```

2. 基本使用 : DRF 框架中的 序列化类 可以进行数据格式转换,将 Python 中字典转换为 JSON 格式

   1. 创建 Serializer 类 (`serializers.py`) : 在应用中创建 serializers 文件用于编写序列化类, 需要继承 ModelSerializer 或 HyperlinkedModelSerializer (生成 url 路由)

      ```python
      from rest_framework import serializers
      from Store.models import Goods
      
      class MoreListlizers(serializers.ModelSerializer):
          class Meta:
              model = Goods
              fields = "__all__"
      ```

      + Serializer 内部类 Meta 属性解释
        1. model : 对应的 model 类
        2. fields : model 类要序列化的属性 `__all__` 表示所有属性
        3. depth : 关联对象序列化的深度,默认只序列化关联对象的 id, 设置为 1 后序列化关联对象所有 filelds 属性

   2. 创建视图

      ```python
      from rest_framework import viewsets
      from .serializers import MoreListlizers
      
      class GoodsView(viewsets.ModelViewSet):
          queryset = Goods.objects.all()
          serializer_class = MoreListlizers
      ```

      

   3. 路由指出

      ```python
      from rest_framework.routers import DefaultRouter
      
      router = DefaultRouter()
      router.register("goods", GoodsView)
      
      urlpatterns = [
          ...
      ]
      
      urlpatterns += router.urls
      ```

      

   4. 访问测试

   5. 简单的分页 : 解决 接口直接返回所有数据 的问题,通过DRF快速分页解决问题 (在 `setting.py` 中配置)

      ```python
      REST_FRAMWORK = {
          'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 分页器
          'PAGE_SIZE' = 10,
      }
      ```

3. 视图类

   1. 继承 APIView 类 : APIView 对 Django 的 django.views.View 类进一步封装

      ```python
      from rest_framework.views import APIView
      from rest_framework.response import Response
      
      class MoreListView(APIView):
          def get(self, request, format=None):
              goodstype_id = request.GET.get('goodstype_id')
      
      		goods_obj_list = Goods.objects.filter(goodstype_id=goodstype_id)
              serializer = MoreListSerializer(goods_obj_list, many=True)
              return Response(serializer.data	)
          
      # 路由设置 urls.py
      path('xxx/', MoreListView.as_view())
      ```

      

   2. 使用 mixins 类 : 对 views 进一步封装 ,  提高代码重用率

      ```python
      from rest_framework import generics
      from rest_framework import mixins
      
      class MoreListView(mixins.ListModelMixin, generices.GenericAPIView):
          def get_queryset(self):
              goodstype_id = self.request.GET.get('goodstype_id')
              goods_obj_list = Goods.objectsfilter(goodstype_id=goodstype_id).order_by('-id')
              return goods_obj_list
          
          serializer_class = MoreListSerializer
          
          def get(self, request, *args, **kwargs):
              return self.list(request, *args, **kwargs)
          
          def get_serializer_context(self):
              return {
                  'view': self  # 返回本身数据,否则 DRF 框架会自动给图片添加绝对路径
              }
          
      # 路由
      	path('xxx/', MoreListView.as_view())
      ```

      

   3. 通用视图类 : mixins 类的使用 使代码量减少,但是 使用 REST 框架的 通用混合视图 仍可以进一步减少 视图 的代码量

      ```python
      class MoreListView(generics.ListAPIView):
          def get_queryset(self):
              goodstype_id = self.request.GET.get('goodstype_id')
              goods_obj_list = Goods.objectsfilter(goodstype_id=goodstype_id).order_by('-id')
              return goods_obj_list
          
          serializer_class = MoreListSerializer
          
          def get_serializer_context(self):
              return {
                  'view': self  # 返回本身数据,否则 DRF 框架会自动给图片添加绝对路径
              }
          
      # 路由
      	path('xxx/', MoreListView.as_view())
      ```

      

   4. viewSet 视图和路由器

      1. viewSet 视图类 是对通用视图的进一步封装

         ````python
         from rest_framework import viewsets
         
         class MoreListViewSet(viewsets.ReadOnlyModelViewSet):
             def get_queryset(self):
                 goodstype_id = self.request.GET.get('goodstype_id')
                 goods_obj_list = Goods.objectsfilter(goodstype_id=goodstype_id).order_by('-id')
                 return goods_obj_list
             
             serializer_class = MoreListSerializer
             
             def get_serializer_context(self):
                 return {
                     'view': self  # 返回本身数据,否则 DRF 框架会自动给图片添加绝对路径
                 }
             
         # 路由
         from django.urls import path, include
         from buyer import views
         from rest_framework.router import DefaultRouter
         
         more_list = views.MoreListViewSet.as_view({
             'get': 'list',
         })
         
         urlpatterns = [
             ...
             path('more_list_view/', more_list)
         ]
         
         ````

      2. 使用 DRF 路由器替代 Django 路由

         ```python
         from django.urls import path, include
         from buyer import views
         from rest_framework.router import DefaultRouter
         
         # 创建路由
         router = DefaultRouter()
         # 注册视图
         router.register('more_list_view', views.MoreListViewSet, basename='')
         
         urlpatterns = [
             ...
             path('', include(router.urls))
         ]
         ```

         