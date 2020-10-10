### Flask 常用技术

#### AJAX 动态数据请求

##### AJAX

+ AJAX (Asynchronous JavaScript And XML) : 异步的 Javascript 和 XML
  + 不属于一种新的编程语言，是一种方法用于使用现有标准,在不重新加载整个页面的情况下,与服务器交换数据并更新部分网页

##### 基于 JQ 的 AJAX 请求

+ 基本语法

  ```
  jQuery.ajax([settings])
  ```

+ 常用配置

  | 配置          | 描述                                                         |
  | ------------- | ------------------------------------------------------------ |
  | `async: true` | 默认值 true.默认值下所有请求均为异步请求.如果需要发送同步请求,设置为 false |
  | `data`        | 发送到服务器的数据.将自动转换为请求字符串格式.GET 请求中附加到 URL 后 |
  | `dataFilter`  | 给 AJAX 返回的原始数据的请求进行预处理的函数                 |
  | `dataType`    | 预处理服务器返回的数据类型,flask 中 jsonify 库将 python 字典中数据转为 json 对象 |
  | `error`       | 自动判断 (xml 或 html).请求失败时调用                        |
  | `success`     | 自动判断 (xml 或 html).请求成功后的回调函数                  |
  | `type`        | 默认值 : "GET", 请求方式 ("POST" 或 "GET"),其他 HTTP 请求方法也可以使用 |
  | `url`         | 发送请求地址                                                 |

+ 例子

  ```
  <script type="text/javascript">
  	$.ajax({
  		type: "post",
  		url: "/kaoqin/",  // 请求发送到的 url 处
  		data: {},
  		dataType: "json",
  		success: function (result) {
  			console.log(result)
  		},
  		error: function (errorMsg) {
  			alert('加载数据失败');
  		}
  	})
  </script>
  ```

#### Flask-SQLAlchemy 分页

+ 基本语法

  ```
  paginate(page=None, per_page=None, error_out=True, max_per_page=None)
  ```
  + 参数

    | 参数         | 描述                                               |
    | ------------ | -------------------------------------------------- |
    | page         | 指定页码,从 1 开始                                 |
    | per_page     | 每一页有几项                                       |
    | error_out    | 是否抛出错误,当其为 True 时,会抛出 404             |
    | max_per_page | 当指定了 max_per_page 时,per_page 受到这个值得限制 |

+ 常用方法

  | 方法名称   | 描述                                  |
  | ---------- | ------------------------------------- |
  | has_next() | 是否还有下一页                        |
  | has_perv() | 是否还有上一页                        |
  | items      | 当前页的元素集合                      |
  | next       | 返回下一页的 Pagination 对象          |
  | next_num   | 下一页页码                            |
  | page       | 当前页页码                            |
  | pages      | 匹配的元素在当前配置一共有多少页      |
  | per_page   | 每一页显示元素个数                    |
  | perv       | 上一页的 Pagination 对象              |
  | perv_num   | 上一页页码                            |
  | query      | 创建 Pagination 对象对应的 query 对象 |
  | total      | 匹配的元素总数                        |

+ 分页使用

  + 视图函数

    ```python
    # 分页测试
    @userbp.route('/fytest/')
    def fytest():
        # 所有的职员
        # person_obj_list = Person.query.all()
        # print(person_obj_list)
        # 第一个参数开始的页码，例如第几页
        # 第二个参数，每一页返回的数据条数
        pagination_obj = Person.query.paginate(2, 1)
        # print(pagination_obj) # <flask_sqlalchemy.Pagination object at 0x0000000004C72488>
        # print(pagination_obj.items)  # 获取具体的对象
        # print(pagination_obj.has_prev)  # 判断是否有上一页,如果有返回True 否则返回False
        # print(pagination_obj.has_next)  # 是否有下一页,如果有返回True 否则返回False
        # print(pagination_obj.prev_num)  # 上一页页码。如果没有返回None
        # print(pagination_obj.next_num)  # 下一页页码。如果没有返回None
        # print(pagination_obj.page) # 当前页码。
        # print(pagination_obj.pages)  # 总页码数
        # print(pagination_obj.iter_pages()) # 可以循环遍历生成页码。
        for page in pagination_obj.iter_pages():
            print(page)
        return '分页...'
    
    
    @userbp.route('/person_list/')
    @login_check
    def person_list():
        # 0.获取前端传递过来的页码
        page = int(request.args.get('page', 1))
        # 1.查询数据库中的数据
        pagination_obj = Person.query.paginate(page, 1)
        person_obj_list = pagination_obj.items
        # 3.判断页码范围
        if page <= 3:
            start = 0
            end = 5
        elif page > pagination_obj.pages - 3:
            start = pagination_obj.pages - 5
            end = pagination_obj.pages
        else:
            start = page - 3
            end = page + 2
    
        # 2.生成页码(使用自带的iter_pages效果不好)
        page_page = range(1, pagination_obj.pages + 1)[start:end]
    
        return render_template('person.html', person_obj_list=person_obj_list, page_page=page_page,
                               pagination_obj=pagination_obj)
    
    ```

    

  + html

    ```html
    <tr>
        <td colspan="4">
            <ul class="pagination">
                <li><a href="/person_list/?page={{ pagination_obj.prev_num }}">上一页</a></li>
                {% for page in page_page %}
                    {% if page == pagination_obj.page %}
                        <li class="active"><a
                                href="/person_list/?page={{ page }}">{{ page }}</a></li>
                    {% else %}
                        <li><a href="/person_list/?page={{ page }}">{{ page }}</a></li>
                    {% endif %}
                {% endfor %}
                <li><a href="/person_list/?page={{ pagination_obj.next_num }}">下一页</a></li>
            </ul>
        </td>
    </tr>
    
    ```

    

#### 项目部署

##### 安装 Flask 环境

1. 导出虚拟环境中的 Flask 开发环境: `pip freeze > package.txt`
2. 将包目录上传至服务器,并进行安装
   1. 将 package.txt 放在 /opt 目录下
   2. 安装 `pip3 install -r package.txt`
   3. 可以换源下载 `pip3 install -r package.txt -i 源地址`

##### 启动 Flask 项目

1. 上传 Flask 项目 至 /opt 目录下

   1. 修改项目中 main.py 开放端口为 0.0.0.0

   2. 启动项目,可能涉及关闭防护墙

      ```
      python3 main.py run
      systemctl stop firewalld
      ```

   3. 访问项目测试

##### uWSGI 转接 Nginx 服务器

1. 安装 uWSGI : `pip3 install uwsgi`
2. 创建软链接 : `ln /usr/local/python3/bin/uwsgi /usr/bin/wsgi`

##### Nginx

1. 下载 Nginx : `wget -c https://nginx.org/download/nginx-1.12.2.tar.gz`
2. 安装 Nginx : 
   1. 解压 : `tar -zxvf nginx-1.12.2.tar.gz`
   2. 在解压目录下的编译安装 : `./configure`然后  `make && make install`
3. 创建软链接 : `ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx`
4. 启动 Nginx 并查看 : `nginx`
5. Nginx 常用命令
   1. `nginx -s stop` : 停止 nginx
   2. `nginx -s reload` : 重启 nginx
   3. `nginx -t` : 检测是否正确

##### Flask + uWSGI + Nginx 部署

1. wWSGI 配置文件

   + 在 /opt 下创建 scripts 目录,编写 uWSGI 配置文件

     ```
     [uwsgi]
     
     socket=127.0.0.1:5000
     // uWSGI 启动地址及端口
     pythonpath=/opt/FlaskOAPro
     // 项目木目录
     module=main
     // 项目控制文件名,不加 .py
     wsgi-file=/opt/FlaskOAPro/main.py
     // 项目控制文件目录
     callable=app
     // 控制文件当中 app 的名称
     processes=4
     threading=2
     daemonize=/opt/scripts/uwsgi.log
     ```

2. Nginx 配置文件

   1. 进入配置文件目录 : `/usr/local/nginx/conf/`

   2. 进行 `nginx.conf` 备份 : `cp nginx.conf nginx.conf.bak`

   3. Nginx 配置文件修改

      ```
      server {
      	listen		80;
      	server_name FlaskOAPro;
      	
      	# charset koi8-r;
      	
      	# access_log	logs/host.access.log main;
      	access_log	logs/host.access.log;
      	error_log	logs/host.error.log;
      	
      	loation / {
      		include uwsgi_params;
      		uwsgi_pass 127.0.0.1:5000;
      		uwsgi_param UWSGI_CHDIR /opt/FlaskOAPro;
      		uwsgi_param UWSGI_SCRIPT main:app;
      	}
      }
      ```

3. 启动项目

   1. 在 `/opt/scripts` 下启动 uWSGI : `uwsgi --ini uwsgi.ini`
   2. 启动 Nginx 

4. 访问项目