### 爬虫和数据

#### 获取数据途径

1. 企业产生的用户数据
2. 数据平台购买数据
3. 政府/机构公开的数据
4. 数据管理咨询公司
5. 爬取网络数据

#### 爬虫是什么

##### 爬虫定义

+ **网络爬虫** : 按照一定的规则,自动的抓取万维网信息的**程序**或**脚本** 

##### 爬虫分类

1. 通用爬虫 ----  搜索引擎
   1. 抓取网页
   2. 数据存储
   3. 预处理
   4. 提供检索服务,网站排名
2. 聚焦爬虫
   + **面向特定主题需求** 的一种网络爬虫程序
   + 与通用爬虫区别
     + 在实施网页抓取时会对内容进行处理筛选,尽量保证只抓取与需求相关的网页信息

#### requests 模块 get 请求

##### 网络请求

+ 客户端发送请求主要有两种请求方法
  1. get 请求 : 从服务器去获取内容
  2. post 请求 : 向服务器提交内容

##### 使用 requests 发送 get 请求

1. 导入 requests 模块 : `import requests`

2. 发送请求获取响应

   ```python
   response = requests.get(
   	url = "",
       headers = 请求头字典,
       params = 请求参数字典,
   )
   ```

   

##### response 对象的属性

1. **字符串响应**内容 : `response.text`
   + Requsets 会自动解码来自服务器的内容
   + response.text 获取的是页面字符内容
2. **二进制响应**内容 : `response.content`
   + `response.content` 会自动解码 gzip 与 deflate 传输编码的响应数据
3. **json 响应**内容 : `response.json`
   + Requests 内置 JSON 解码器,如果 JSON 解码失败会抛出异常
4. **响应状态码** : `response.status_code`
5. **响应头** : `response.headers`
6. **页面乱码**问题 : 针对处理 字符串响应内容
   1. 设置正确的编码格式 : `response.encoding` 设置一个正确的编码,设置之后 `resonse.text` 就可以获得正确的内容
   2. 通过 `response.content.decode('编码格式')` 将二进制内容按照提供编码格式编码成 unicode 字符串并显示

#### requests 模块 post 请求

1. 最基本的 requests 模块 : `import requests`

2. 发送请求,获取响应

   ```python
   response = requests.post(
   	url = "请求 url 地址",
       headers = "请求头字典",
       data = "请求数据字典",
   )
   ```

   

##### 最基本的 post 请求使用方法

+ post 发送请求头

  ```python
  headers = {
      'user-agent': 'User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
      # Refere 伪装请求来源
      'Referer': 'https://fanyi.baidu.com/',
      # ajax 请求附加头
      'X-Requested-With': 'XMLHttpRequest',
      # ajax 请求内容类型
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
  }
  ```

  

#### 爬虫和法律

##### 爬虫背后的法律风险

+ 《规范互联网信息服务市场秩序若干规定》
  1. 搜寻需经许可 : 未经用户许可,不得搜集与用户相关、能够单独或者与其他信息结合识别用户的信息,法律法规另有规定除外
  2. 限定搜集范围和用途 : 经用户同意搜集用户个人信息的，应当明确告知搜集和处理用户个人信息的方式、内容和用途,不得搜集其提供服务所必需以外的信息,不得将用户个人信息用于其提供服务之外的目的
  3. 用户个人信息保障 : 互联网信息服务提供者应当加强系统安全防护,妥善保管用户个人信息,未经用户同意,不得向他人提供用户上载信息,但在法律法规另有规定的除外

##### 网络爬虫怎么做比较好