```yaml
   Author: Gentleman.Hu
   Create Time: 2021-06-18 17:26:25
   Modified by: Gentleman.Hu
   Modified time: 2021-06-18 18:19:23
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: HTTP基础
 ```

## HTTP的定义

Hypertext Transfer Protocol, 超文本传输协议, 与HTML一起诞生, 用于请求和传输HTML内容.

## HTTP工作机制

### 浏览器

用户输入地址后回车或点击链接->浏览器拼装HTTP报文并发送给服务器->服务器处理请求后发送响应报文给浏览器->浏览器解析响应报文并使用渲染引擎显示到界面

### 手机APP

用户点击界面或者自动触发联网请求-> Android代码调用拼装HTTP报文并发送请求到服务器->服务器处理请求后发送响应报文给手机->Android代码处理响应报文并作出相应处理(存储数据,加工数据,显示数据到界面等)

## URL和HTTP报文

### URL格式

1. 协议类型
2. 服务器地址(端口号)
3. 路径(path)

协议://服务器地址[:port]/路径
https://www.crushing.xyz

### 报文格式

- 请求报文
  
![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20210618173705.png)

- 响应报文

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20210618173840.png)

### 请求方法 - Request Method

- GET
  - 获取资源
  - 不对服务器数据进行修改
  - 不发送body
  
```json
GET /users/1 HTTP/1.1
Host: api.github.com
```

对应的Retrofit代码:

```java
@GET("/users/{id}")
Call<User> getUser(@Path("id") String id, @Query("gender") String gender);
```

- POST
  - 增加或者修改资源
  - 发送给服务器的内容在body里

```json
POST /users HTTP/1.1 
Host: api.github.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

name=godlin&gender=male
```

对应Retrofit代码:

```java
@FormUrlEncoded
@POST("/users")
Call<User> addUser(@Field("name") String name, @Field("gender") String gender);
```

- PUT

```json
PUT /users HTTP/1.1
Host: api.github.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

gender=female
```

对应Retrofit代码:

```java
@FormUrlEncoded
@PUT("/users/{id}")
Call<User> updateUser(@Path("id") String id, @Field("gender") String gender);
```

- DELETE

```json
DELETE /users HTTP/1.1
Host: api.github.com
```

Retrofit代码

```java
@DELETE("/users/{id}")
Call<User> deleteUser(@Path("id") String id,@Query("gender") String gender);
```

- HEAD
  - 跟GET用法一致
  - 唯一区别,返回响应无Body

### 状态码 - Status Code

- 1xx: 临时消息,100继续发送,101正在切换协议
- 2xx: 成功.200 ok,201 创建成功
- 3xx: 重定向. 301永久移动,302临时移动,304内容未改变
- 4xx: 客户端错误. 400客户端请求错误,401认证失败,403禁止,404找不到
- 5xx: 服务器错误. 500服务器内部错误.

### 头部 - Header

> 作用: HTTP消息的metadata

- Host: 目标主机. ! 不是用于网络寻址的,而是在目标服务器上用于定位子服务器的.
- Content-Type: 指定Body类型,主要4类
  - text/html
  - x-www-form-urlencoded
  - multipart/form-data
  - application/json, image/jpeg, application/zip ... 
- Content-Length
- Transfer: chunked
- Location
- User-Agent: 用户代理.谁实际发送请求,接受响应.
- Range/Accept-Range
  - Accept-Range: bytes 服务器按照字节取范围数据
  - Range: bytes=<start>-<end> 请求报文出现,表示取那段数据
  - Content-Range: <start>-<end>/total 响应报文中出现,表示发送的是那段数据
  - 作用: 断点续传,多线程下载
- Accept: 客户端可以接受的数据类型.如 text/html
- Accept-Charset: 客户端接受的字符集.如 utf-8
- Accept-Encoding: 客户端接受的压缩编码类型.如gzip
- Content-Encoding: 压缩类型. 如gzip

## Cache

> 作用: 在客户端或者中间网络节点缓存数据,降低从服务器取数据的频率,提高网络性能.

## REST

- 使用资源的格式定义URL
- 规范使用method定义网络请求操作
- 规范使用status code表示响应状态
- 其他服务HTTP规范的设计准则

> copy from hencoder notes pdf