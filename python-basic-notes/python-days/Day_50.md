### 模拟登陆与代理设置

#### 登录页面信息爬取

##### cookie 与 session

1. 什么是 cookie 和 session
   + cookie : 网站用来辨别身份,进行会话跟踪,存储在本地终端上的数据
   + session : 主要用于在服务器端存储特定用户对象会话所需要的信息 (会话 : 本意是有始有终的一系列动作和消息)
2. cookie 和 session 产生的原因
   + http 协议是一个无状态协议,在特定的操作下需要保存信息,因此使用 cookie 和 session 保存信息
3. cookie 原理
   + cookie 是由服务器产生,浏览器第一次请求,服务器发送给客户端保存.浏览器继续访问时,就会在请求头的 cookie 字段附加上 cookie 信息,使服务器可以识别访问对象
   + cookie 的缺陷:
     1. 用户本地保存,容易被修改,安全性低
     2. 大小受限,最大 4kb
4. session 原理
   + session 在服务器保存,解决了 cookie 的安全问题
   + 为了使服务器可以识别访问用户,在用户 本地 cookie 中保存 sessionid 字段,在服务器中方便查找
   + session 登录步骤
     1. 导入 requests 库
     2. 使用 requests 生成一个 session 对象 : `session = requests.session()`
     3. session 对象发起请求,接收响应 `response = session.post()`
        + session 请求的 url 来自于登录页面 form 表单 action 登录信息的 URL
        + session 请求时的 data 数据都来自于登录界面的 form 表单
5. 禁用 cookie
   + 禁用 cookie 一般情况下 session 也无法使用
   + url 重写技术 : 禁用 cookie 情况下, 使用 session,将 sessionid 拼接在url内
6. session 的生命周期 : 服务武器创建开始,有效期结束 (一般网站为 30 分钟) 就删除

##### 案例

1. cookie 登录

   ```python
   import requests
   
   	cookie 登录
   headers = {
   	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
   	'Cookie': 'Cookie值'
   }
   
   url = "http://xue.ujiuye.com/user/index/"
   	
   response = requests.get(url, headers=headers)
   
   print(response.status_code, response.encoding)
   print(response.url)
   with open("./test.html", "w", encoding="utf-8") as f:
   	f.write(response.text)
   ```

2. session 登录

   ```python
   import requests
   
   session = requests.session()
   
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
   }
   
   login_url = "https://security.kaixin001.com/login/login_post.php"
   
   data = {
       "loginemail": "用户名",
       "password": "密码",
   }
   response = session.post(login_url, data=data, headers=headers)
   
   print(response.text)
   
   ```

   

#### 代理设置

+ 如果一直使用同一个 ip 爬取一个网页, 由于采集网站信息强度和收集速度太大,会给服务器带来巨大压力,容易被封杀 IP

##### 代理基本原理

+ 代理 (proxy server 实际上指代理服务器)

  + 功能 : 代理网络用户去取得网络信息
  + 是网络信息中转站
  + 基本原理 : 本机向代理服务器发出请求,代理服务器再向 web 服务器 发出请求, 代理服务器收到响应后,将响应发送回本机,此时 web 服务器识别的将是代理服务器 IP

+ 代理实例

  ```python
  import requests
  
  proxies = {
      "http": "http://121.31.12.12:5212",
      "https": "https://222.22.11.21:3131",
  }
  
  response = requests.request("get", "http://www.baidu.com/", proxies=proxies)
  print(response.text)
  ```

  

#### 页面响应类型

##### 数据的结构化分类

+ 爬取网页和应用有用内容一般分为三部分:
  1. **结构化数据**
     + 可以使用统一结构加以表示的数据。可以使用关系型数据库进行表示和存储,表现为二维形式的数据
     + 特点 : 一行数据表示一个实体的信息,每一行数据属性都相同
  2. **半结构化数据** (自描述的结构)
     + 结构化数据的一种形式,不符合关系型数据库或其他数据表的形式关联起来的数据模型结构,但包含相关标记,用来分隔语义元素及其对记录和字段进行分层
     + 常见类型有 : **JSON**、**XML**、**HTML**
     + 实际存储结构 : **树**、**图**
  3. **非结构化数据**
     + 没有固定结构的数据,一般整体进行存储,存储为二进制格式
     + 常见类型 : 文档、图片、视频、音频

##### json 数据

+ JSON (JavaScript Object Notation, JS 对象标记) : 是一种轻量级的数据交换格式，json 是 js 对象的字符串表达式, 使用文本形式表示一个 js 对象的信息,本质是一个字符串
+ Js 中对象和数组是比较特殊并且比较常用的两种类型
  1. 对象表示为键值对
  2. 数据用逗号分隔
  3. 花括号保存对象
  4. 方括号保存数组
+ json 优势
  + Json 作为数据包格式传输时有更高的效率, Json 不像 XML 一样有严格的闭合标签
  + 大大减少网络的传输压力
  + 易于阅读
  + 有效提升网络速度

##### 处理 JSON 数据的两种方式

1. 使用 **json** 模块

   1. 将 Python 类型转换为 json 字符串类型: `json.dumps()`

      ```python
      json_data = json.dumps(dic)
      ```

      

   2. 将 json 字符串类型转换为 Python 类型 (字典或列表): `json.loads()`

      ```python
      dic_data = json.loads(json_data)
      ```

      

2. Requests 方法

   + `requests.json()` : 直接获取json 数据对应的 python 数据类型

