### Tornado

#### Tornado + ES 检索

##### Python 中使用 ES 检索

+ 实例

  ```python
  from elasticsearch import Elasticsearch
  
  es = Elasticsearch(hosts="10.10.123.131", timeout=360)
  
  body = {
  	# 精确查询
  	"query": {
  		"term": {
  			"c_name": "宾利"
  		}
  	}
  }
  
  result = es.search(index="carlist", doc_type="car", body=body)
  print(result)
  print(result["hits"]["hits"]) # 获取更好格式的数据
  ```

  

##### Tornado + ES

+ 实例 

  ```python
  import tornado.web
  from elasticsearch import Elasticsearch
  
  
  class MyHeadler(tornado.wewb.RequestHandler):
      
      def get(self):
          result = locals()
          result.pop("self")
          self.render("index.html", **result)
          
  class CarHeadler(tornado.web.RequestHandler):
      
      def initialize(self):
          self.es = Elasticsearch("10.10.123.131")
          self.body = {
              "query": {
                  "match": {
                      "c_name": ""
                  }
              }
          }
          
      def get(self):
          # 获取请求数据
          c_name = self.get_arguments("search_key")[0]
          # 进行请求的 es 个数构建
          self.body["query"]["match"]["c_name"] = c_name
          self.body["from"] = 0
          self.body["size"] = 12
          # 进行 es 请求
          result = self.es.search(
          	body = self.body,
              index = "carlist",
              doc_type = "car",
          )
          # 数据过滤
          cars = result["hits"]["hits"]
          car_list = [i["_source"] for i in cars]
          
          self.render("car_list.html", car_list=car_list)
  ```

#### Tornado 部署

##### 检查 Linux

1. 检查自己的 IP 地址 : `ifconfig`
2. 关闭防火墙 : `systemctl stop firewalld`

##### 安装 Python3.7 环境

1. 下载 Python 3.7 依赖包 : `yum install zlib-devel libffi-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc* make -y`
2. 下载 Python 3.7 tar 包 : `wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz`
3. 解压 tar 包 : `tar -Jxvf Python-3.7.2.tar.xz`
4. 编译安装
   + 进入目录下 : `./configure prefix=/usr/local/python3`
   + 安装 : `make && make install`
5. 创建软链接 : 
   + Python 软链接 : `ln -s /usr/local/python3/bin/python3 /usr/bin/python3`
   + Pip 软链接 : `ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3`

#### 启动项目

1. 安装项目依赖包 
   1. 导出 虚拟环境下的项目依赖包 : `pip freeze > a.txt`
   2. 在 Linux 系统下下载 依赖包 : `pip3 install -r a.txt`
2. 启动项目 : `python manage.py` (不需要使用 uWSGI 与 Nginx 服务器)