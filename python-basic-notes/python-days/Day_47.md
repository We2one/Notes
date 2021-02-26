### Tornado

#### Elasticsearch 介绍

##### 认识 Elasticsearch

+ Elasticsearch 是 分布式、可拓展、实时的 搜索与数据分析引擎.在项目一开始赋予开发者搜索、分析和探索的能力
+ Elasticsearch 不仅仅只是全文搜索,还可以用于 结构化搜索、数据分析、复杂的人类语言处理、地理位置 和 对象关联关系等.
+ Elasticsearch 是一个开源的搜索引擎,建立在全文搜索引擎库 Apache Lucene 基础之上.
  + Lucene 不仅仅是一个搜索引擎库,非常复杂,需要用 Java 并将 Lucene 直接集成到应用程序中才可以充分发挥其功能
+ Elasticsearch 也是使用 Java 编写的, 内部使用 Lucene 做索引和搜索,目的是使全文搜索变得简单,隐藏 Lucene 的复杂性,提供简单的 RESTful API
+ Elasticsearch 准确形容:
  + 一个分布式的实时文档存储,每个字段可以被索引与搜索
  + 一个分布式实时分析搜索引擎,
  + 能胜任 上百个服务节点的拓展,支持 PB 级的结构化或者非结构化数据
+ Elasticsearch 将所有功能打包成一个单独的服务,开发者可以通过程序连接它提供的简单的 RESTful API 进行通信,使用不同的编程语言充当 Web 客户端

#### Elasticsearch 安装使用

##### Centos7 安装

1. 下载安装包 : `wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.1.tar.gz`

2. 在 home 下解压 : `tar -zxvf elasticsearch-6.3.1.tar.gz`

3. 创建 ES 用户 

   1. `adduser esuser` : 创建新用户
   2. `cd /home` : 进入 home 目录下
   3. `mkdir -p esdata/data` : 创建数据读取目录
   4. `mkdir -p esdata/log` : 创建日志文件
   5. `chown -R esuser elasticsearch-6.3.1` : 赋予 新用户 操作权限
   6. `chown -R esuser esdata` :  : 赋予 新用户 操作权限
   7. 关闭防火墙 : `systemctl stop firewawlld`
   8. 查看防火墙状态 : `systemctl status firewalld`

4. ES 设置

   1. 修改配置文件, 备份配置文件, 进入文件目录

      ```
      cd /home/elaticsearch-6.3.1/config/
      cp elasticsearch.yml elasticsearch.yml.bak
      
      vi elasticsearch.yml
      ```

   2. 配置服务名称

      ```
   # ---------------------------------- Cluster -----------------------------------
      #
      # Use a descriptive name for your cluster:
      #
      #cluster.name: my-application
      cluster.name: my-application  #取消注释
      #
      ```
   
   3. 配置节点名称

      ```
   # ------------------------------------ Node ------------------------------------
      #
   # Use a descriptive name for the node:
      #
      #node.name: node-1
      node.name: node-1
      #
      # Add custom attributes to the node:
      #
      #node.attr.rack: r1
      #
      
      ```
   
   4. 配置 es 数据 和 路径 的存放路径
   
      ```
   # ----------------------------------- Paths ------------------------------------
      #
   # Path to directory where to store the data (separate multiple locations by comma):
      #
   #path.data: /path/to/data
      path.data: /home/esdata/data
      #
      # Path to log files:
      #
      #path.logs: /path/to/logs
      path.logs: /home/esdata/log
      #
      ```
   
   5. 内存锁配置
   
      ```
      # ----------------------------------- Memory -----------------------------------
      #
   # Lock the memory on startup:
      #
   #bootstrap.memory_lock: true
      bootstrap.memory_lock: true
   #
      # Make sure that the heap size is set to about half the memory available
      # on the system and that the owner of the process is allowed to use this
      # limit.
      #
      # Elasticsearch performs poorly when the system is swapping the memory.
      #
      ```
   
   6. 配置服务的 ip 和端口
   
      ```
      # ---------------------------------- Network -----------------------------------
      #
      # Set the bind address to a specific IP (IPv4 or IPv6):
      #
   #network.host: 192.168.0.1
      network.host: 0.0.0.0
   #
      # Set a custom port for HTTP:
   #
      #http.port: 9200
      http.port: 9200
      #
      # For more information, consult the network module documentation.
      #
      ```
   
   7. 多节点配置
   
      ```
      # --------------------------------- Discovery ----------------------------------
      #
      # Pass an initial list of hosts to perform discovery when new node is started:
      # The default list of hosts is ["127.0.0.1", "[::1]"]
      #
      #discovery.zen.ping.unicast.hosts: ["host1", "host2"]
   discovery.zen.ping.unicast.hosts: ["host1", "host2"]
      #
   # Prevent the "split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
      #
   #discovery.zen.minimum_master_nodes:
      #
      # For more information, consult the zen discovery module documentation.
      #
      ```
   
   8. 路由节点个数 和 requires_name 配置
   
      ```
      # ---------------------------------- Gateway -----------------------------------
      #
      # Block initial recovery after a full cluster restart until N nodes are started:
      #
      #gateway.recover_after_nodes: 3
      gateway.recover_after_nodes: 1
      #
      # For more information, consult the gateway module documentation.
   #
      # ---------------------------------- Various -----------------------------------
   #
      # Require explicit names when deleting indices:
   #
      #action.destructive_requires_name: true
      ```
   
      
   
5. 配置系统参数

   1. `vim /etc/security/limits.conf` : 在文件最后添加

      ```
      # End of file
      esuser hard nofile 65536
      esuser soft nofile 65536
      esuser soft memlock unlimited
      esuser hard memlock unlimited
      
      ```

   2. `vi /etc/sysctl.conf`

      ```
   # sysctl settings are defined through files in
      # /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
      #
      # Vendors settings live in /usr/lib/sysctl.d/.
      # To override a whole file, create a new file with the same in
      # /etc/sysctl.d/ and put new settings there. To override
      # only specific settings, add a file with a lexically later
      # name in /etc/sysctl.d/ and put new settings there.
      #
      # For more information, see sysctl.conf(5) and sysctl.d(5).
      vm.max_map_count=262144
      ```
   
   3. 执行命令 : 

      1. `sysctl -p`

      2. `visudo` : 添加允许 esuser 在任何地方执行命令

         ```
      ## The COMMANDS section may have other options added to it.
         ##
         ## Allow root to run any commands anywhere
         root    ALL=(ALL)       ALL
         esuser  ALL=(ALL)       ALL
         
         ```
   
   4. `vim /etc/security/limits.d/20-nproc.conf`

      ```
   # Default limit for number of user's processes to prevent
      # accidental fork bombs.
   # See rhbz #432903 for reasoning.
      
      *          soft    nproc     4096
      root       soft    nproc     unlimited
      
      * soft nproc 204800
      * hard nproc 204800
      ```
   
   5. `vim /etc/security/limits.d/def.conf` : 创建并编写,文件尾部编写
   
      ```
   * soft nofile 204800
      * hard nofile 204800
   ~
      ~
   ```
   
      
   
6. 安装 1.8 以上版本的 java (`yum install java -y`) 并启动 

   + 进入 elasticsearch-6.3.1 的目录下 : `cd /home/elasticsearch-6.3.1/bin/`
   + 切换为 esuser 用户 : `su esuser`
   + 启动 : `./elasticsearch`

   + 启动后访问 本机 ip 的 9200 端口 查看效果

##### Postman 使用

1. Postman 介绍

   + Postman 是一款强大的网页调试与发送网页 HTTP 请求的 Chrome 插件
   + 在开发或调试网络程序程序或者是网页 B/S 模式的程序的时候需要一些方法来跟踪网页请求,用户可以使用一些网络的监视工具 (比如Firebug) 等页面调试工具
   + Postman 不仅可以调试简单的 CSS、HTML、脚本等网页简单信息,还可以发送几乎所有类型的 HTTP 请求

2. [Postman 简易版 (Google 插件)](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop/related?hl=zh-CN)

   <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Postman.png" style="zoom:50%;" />

3. 区域划分

   1. 文档区: 可以查看请求的历史,可以进行请求保存,对于接口开发较为方便
   2. 请求方式和地址 : 发送需要的请求
   3. 请求参数 : 设置请求携带的参数,请求头部参数和请求数据都可以

##### ES 基本使用

1. 介绍

   1. Es 和数据库可以进行类比学习

      | 数据库        | database | table | rows     | Columns |
      | ------------- | -------- | ----- | -------- | ------- |
      | Elasticsearch | index    | type  | document | fields  |

   2. 传统数据库只能存储基本的数据类型 (字符串、数字、小数、邮箱、时间),复杂的数据类型只能通过多表关系表述 (一对一、一对多、多对多)

   3. Es 可以保存更为复杂的数据类型

2. 索引 (index)

   1. 创建索引, 采用的请求方式为 put

      1. 创建步骤

         <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_index01.png" style="zoom:50%;" />

         <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_index02.png" style="zoom:50%;" />

      2. 创建索引和类型,需要在路由上描述索引,然后搭建请求的数据结构

         | 参数       | 描述              |
         | ---------- | ----------------- |
         | carlist    | 索引,名称必须小写 |
         | mappings   | 映射,创建的开始   |
         | car        | 表名,自定义       |
         | properties | 属性              |
         | c_name     | 字段名称,自定义   |
         | type       | 字段类型的键      |
         | text       | 文本类型          |

         

      3. Es 常用字段类型

         | 类型    | 描述                                                         |
         | ------- | ------------------------------------------------------------ |
         | string  | 字符串类型                                                   |
         | long    | 64 位存储,数字类型                                           |
         | integer | 32 位存储,数字类型                                           |
         | short   | 16 位存储,数字类型                                           |
         | byte    | 8 位存储,数字类型                                            |
         | double  | 64 位双精度存储,数字类型                                     |
         | float   | 32 位双精度存储,数字类型                                     |
         | date    | 日期类型,必须指定格式                                        |
         | Boolean | 布尔类型                                                     |
         | Binary  | 二进制类型                                                   |
         | Array   | 数组类型                                                     |
         | Object  | 单个 json (字典) 对象                                        |
         | nested  | 嵌套的 json 对象                                             |
         | text    | 文本类型,用于全文本字段,文本不会被 Analyzer 分词<br>默认不支持聚合和排序,需要将 fielddata 设置为 true |
         | Keyword | 用于 ID,枚举及不需要分词的文本<br>适用于 Filter 精确匹配,Sorting 和 Aggregations |

   2. 查看所有索引 : `ip地址/_表名/indices/`

      + 实例

        <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_getindex01.png" style="zoom:50%;" />

      + `yellow open hello rs7mwZXPQL6d-bKUy_DKng 5 1 0 0 1.2kb 1.2kb`
        + yellow : 当前索引当中索引的状态, 绿色代表健康,黄色代表警告,红色代表有误
        + open : 代表索引开启, close 关闭
        + index_name : 定义索引时的索引名称

   3. 查看当前索引 : `ip地址:9200/索引名/`

      + 实例

        <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_getindex02.png" style="zoom:50%;" />

   4. 查看单条索引数据 : `ip地址:9200/索引名/_search`

      + 实例

        <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_getindex03.png" style="zoom:50%;" />

   5. 删除索引: 发送 DELETE 请求

      + 实例

        <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_delete.png" style="zoom:50%;" />

3. 插入文档 (document 使用 post 请求) : `ip地址/索引名/表名`

   + 实例

     <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_post01.png" style="zoom:50%;" />

4. 查询文档 (document 使用 get 请求) : `ip地址/索引名/表名/_search`

   + 实例

     <img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_post02.png" style="zoom:50%;" />

#### ES 模型及数据创建

##### 创建 ES 模型

<img src="https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/postman_esmodel.png" style="zoom:50%;" />

##### Python 操作 ES

1. 安装模块 elasticsearch : `pip install elasticsearch -i http://pypi.tuna.tsinghua.edu.cn/simple`

2. 插入数据脚本

   ```python
   import random
   from elasticsearch import Elasticsearch
   
   es = Elasticsearch("10.10.123.131", timeout=360)  # 链接服务器,设置超时时间
   
   # 尝试保存10000条数据
   
   c_names = """奥迪
   宾利
   宝马
   华晨
   比亚迪
   别克
   凯迪知拉克
   雪佛兰
   克莱斯道勒
   一汽
   法拉利
   菲亚特
   福特
   本田
   捍马回
   现代
   捷豹
   吉普
   起亚
   兰博基尼
   路虎
   雷克撒斯
   林肯
   莲花
   玛莎拉蒂
   迈巴赫
   马自达
   奔驰答
   迷你
   三菱
   日产
   欧宝
   标志
   保时捷
   雷诺
   劳斯莱斯
   萨博
   斯科达
   世爵
   斯巴鲁
   铃木
   丰田
   大众""".split("\n")
   
   c_citys = "郑州市、洛阳市、焦作市、商丘市、信阳市、周口市、鹤壁市、安阳市、濮阳市、驻马店市、\
   南阳市、开封市、漯河市、许昌市、新乡市、济源市、灵宝市、偃师市、邓州市、登封市、三门峡市、\
   新郑市、禹州市、巩义市、永城市、长葛市、义马市、林州市、项城市、汝州市、荥阳市、\
   平顶山市、卫辉市、辉县市、舞钢市、新密市、孟州市、沁阳市、郏县".split("、")
   
   for i in range(10000):
       data = {
           "c_name": random.choice(c_names),
           "c_date": "%s-%s-%s" % (
               random.randint(1983, 2020),
               random.randint(1, 12),
               random.randint(1, 28)
           ),
           "c_mileage": random.randint(1, 10000),
           "c_city": random.choice(c_citys),
           "c_price": random.randint(8, 100),
           "c_sale": random.randint(1, 3),
           "c_service": random.randint(30, 100)
       }  # 构建插入数据的结构
   
       res = es.index(index="carlist", doc_type="car", body=data)  # 开始执行
       print(res)
   
   print('插入完成了....')
   
   ```

   

#### ES 检索

##### 查询 (在Python 中运行 postman 内GET 请求)

1. 查询基本格式

   ```json
   {
       "query": {
           "查询的类型": {
               "查询条件": "条件的值"
           }
       }
   }
   ```

2. 精准查询 **term**
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

   

3. 多条件查询 **terms**

   ```python
   from elasticsearch import Elasticsearch
   
   es = Elasticsearch(hosts="10.10.123.131", timeout=360)
   
   body = {
   	# 精确查询
   	"query": {
   		"terms": {
   			"c_name": ["宾利", "大众"]
   		}
   	}
   }
   
   result = es.search(index="carlist", doc_type="car", body=body)
   print(result)
   print(result["hits"]["hits"]) # 获取更好格式的数据
   ```

   

4. 查询所有 **match_all**

   ```python
   from elasticsearch import Elasticsearch
   
   es = Elasticsearch(hosts="10.10.123.131", timeout=360)
   
   body = {
   	# 精确查询
   	"query": {
   		"match_all":{
   
   		}
   	}
   }
   
   result = es.search(index="carlist", doc_type="car", body=body)
   print(result)
   print(len(result["hits"]["hits"]))  # 10 默认查询 10 条
   ```

   

5. 分页查询: **from**: 分页起始位置, **size**: 分页条数 (可以通过循环增加 from 值实现多次查询)

   ```python
   from elasticsearch import Elasticsearch
   
   es = Elasticsearch(hosts="10.10.123.131", timeout=360)
   
   body = {
   	# 精确查询
   	"query": {
   		"match_all":{
   
   		}
   	},
   	"from": 0,
   	"size": 100
   }
   
   result = es.search(index="carlist", doc_type="car", body=body)
   # print(result)
   print(len(result["hits"]["hits"]))  # 100
   print(result["hits"]["hits"])
   ```

   

6. 排序查询 **sort**

   1. 顺序查找 `"sort: [ '排序条件' ]"`

      ```python
      from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
      	# 精确查询
      	"query": {
      		"match_all":{
      	},
      	"sort": [
      		"c_date"  # 按时间顺序顺序查找
      	],
      	"from": 0,
      	"size": 100
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```

   2. 倒序查询 : ``"sort: { '排序条件': { 'order': 'desc' } }"``

      ```python
      from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
      	# 精确查询
      	"query": {
      		"match_all":{
      
      		},
      	},
      	"sort": {
      		"c_date": {
      			"order": "desc"
      		}
      	},
      	"from": 0,
      	"size": 100
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```

      

7. 模糊查询: **match** 匹配含有指定关键字的数据,采用**分词**进行建模,会有效果

   ```python
   from elasticsearch import Elasticsearch
   
   es = Elasticsearch(hosts="10.10.123.131", timeout=360)
   
   body = {
   	"query": {
   		"match": {
   			"c_name": "宝马"
   		}
   	}
   }
   
   result = es.search(index="carlist", doc_type="car", body=body)
   # print(result)
   print(len(result["hits"]["hits"]))
   print(result["hits"]["hits"])
   ```

   

8. 逻辑查询 **bool**

   1. 基本格式

      ```json
      {
          "query": {
          	"bool": {
                  "逻辑类型": [
                      {
                          "查询类型1": {
                              "查询条件1": "查询条件1的值"
                          }
                      },
                      {
                          "查询类型2": {
                              "查询条件2": "查询条件2的值"
                          }
                      },
                      {
                          "查询类型3": {
                              "查询条件3": "查询条件3的值"
                          }
                      },
                  ]
              }
      	}
      }
      ```

      

   2. **must** : 且, 多条件同时成立

      ```python
      from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
      	"query": {
      		"bool": {
      			"must": [
      				{
      					"term": {
      						"c_name": "大众"
      					}
      				},
      				{
      					"term": {
      						"c_price": 18
      					}
      				}
      			]
      		}
      	}
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```

      

   3. **should** : 或, 多条件任一个成立

      ```python
      from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
      	"query": {
      		"bool": {
      			"should": [
      				{
      					"term": {
      						"c_name": "大众"
      					}
      				},
      				{
      					"term": {
      						"c_price": 18
      					}
      				}
      			]
      		}
      	}
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```

   4. **must_not** : 非, 查询条件不成立

      ```python
   from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
      	"query": {
      		"bool": {
      			"must_not": [
      				{
      					"term": {
      						"c_name": "大众"
      					}
      				},
      			]
      		}
      	}
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```
      
   
      
5. must 和 should 同时使用需要特殊语法 : 在 must 和 shoud 同时存在时,should 部分需要重写一个 bool 类型嵌套在 must 条件中
   
   ```python
      from elasticsearch import Elasticsearch
   
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      # 查询 18 万的宝马或大众
      body = {
      	"query": {
      		"bool": {
      			"must": [
      				{
      					"term": {
      						"c_price": 18
      					}
      				},
      				{
      					"bool": {
      						"should": [
      							{
      								"term": {
      									"c_name": "宝马"
      								}
      							},
      							{
      								"term": {
      									"c_name": "大众"
      								}
      							}
      						]
      					}
      				}
      			]
      		}
      	}
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```
      
   
9. 范围查询 **range**

   1. 符号属性

      | 符号 | 描述     |
      | ---- | -------- |
      | lt   | 小于     |
      | lte  | 小于等于 |
      | gt   | 大于     |
      | gte  | 大于等于 |

      

   2. 实例

      ```python
      from elasticsearch import Elasticsearch
      
      es = Elasticsearch(hosts="10.10.123.131", timeout=360)
      
      body = {
          # 查询价格在 10 -15 万之间的所有车
      	"query": {
      		"range": {
      			"c_price": {
      				"lt": 15,
      				"gt": 10
      			}
      		}
      	},
      	"from": 0,
      	"size": 100,
      }
      
      result = es.search(index="carlist", doc_type="car", body=body)
      # print(result)
      print(len(result["hits"]["hits"]))
      print(result["hits"]["hits"])
      ```

10.  聚合查询 **aggs**

    1. 聚合函数

       | 聚合函数名称 | 描述     |
       | ------------ | -------- |
       | avg          | 平均数   |
       | sum          | 求和     |
       | max          | 求最大值 |
       | min          | 求最小值 |

    2. 基本格式

       ```
       {
       	"query": {
       		"查询类型": {
       			"查询条件": "查询条件的值"
       		}
       	},
       	"aggs": {
       		"自定义名称": {
       			"聚合函数": {
       				"field": "查询条件"
       			}
       		}
       	}
       }
       ```

    3. 实例

       ```python
   from elasticsearch import Elasticsearch
       
       es = Elasticsearch(hosts="10.10.123.131", timeout=360)
       
       body = {
       	# 求宝马均价
       	"query": {
       		"term": {
       			"c_name": "宝马"
       		}
       	},
       	"aggs": {
       		"price_avg": {
       			"avg": {
       				"field": "c_price"
       			}
       		}
       	}
       }
       
       result = es.search(index="carlist", doc_type="car", body=body)
       print(result)
       print(len(result["hits"]["hits"]))
       print(result["aggregations"]["price_avg"]["value"])  # 均价
       ```
    
11.  分组查询

    ```python
    from elasticsearch import Elasticsearch
    
    es = Elasticsearch(hosts="10.10.123.131", timeout=360)
    
    # 查询各种车辆数量以及平均价格
    body = {
    	"query": {
    		"match_all": {
    
    		}
    	},
    	"aggs": {
    		"case_sum": {
    			"terms": {
    				"field": "c_name"
    			},
    			"aggs": {
    				"price_avg": {
    					"avg": {
    						"field": "c_price"
    					}
    				}
    			}
    		}
    	}
    }
    
    result = es.search(index="carlist", doc_type="car", body=body)
    # print(result)
    print(len(result["hits"]["hits"]))
    print(result["aggregations"]["case_sum"])
    print(result["aggregations"]["case_sum"]["buckets"])
    ```

    

