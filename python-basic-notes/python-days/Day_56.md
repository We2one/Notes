

### Fiddler 和 MongoDB

#### Fiddler 工具

##### Fiddler 简介

+ **Fiddler** : 抓包工具
+ Fiddler 原理 : 以 web 代理服务器形式工作, **代理地址** : 127.0.0.1:8888 可以修改端口
+ **代理** : 客户端和服务器之间设置的一道关卡,客户端先将请求数据发送出去后,代理服务器会将数据包进行拦截,代理服务器再冒充客户端发送数据到服务器;同理,服务器返回响应数据,代理服务器将数据拦截.

##### Fiddler 分析下载 QQ 音乐

+ 代码链接[QQmusic](https://github.com/Forgotten-Forever/scrapy-project/tree/main/QQMusic_fiddler)

#### NoSQL 简介

##### NoSQL 简介

+ NoSQL (NoSQL = Not Only SQL . 不仅仅是 SQL) : **非关系型数据库**，对于不同于传统的关系型数据库的数据库的管理系统的统称
+ NoSQL 用于**超大规模数据的存储**,这些数据存储**不需要固定的格式**,**无需多余操作就可以横向拓展**

##### RDBMS vs NoSQL

+ **RDBMS** : 关系数据库管理系统
  + 高度组织化结构数据
  + 结构化查询语言 SQL
  + 数据和关系都存储在单独的表内
  + 数据操纵语言,数据定义语言
  + 严格的一致性
  + 基础的事务
+ **NoSQL**
  + 无声明查询语言
  + 无预定义的模式
  + 键值对存储,列存储,文档存储,图形数据库
  + 最终一致性,而非 ACID 属性
  + 非结构化和不可预知数据
  + 高能性，高可用性和可伸缩性

#### MongoDB 简介

##### MongoDB 简介

+ MongoDB : 基于 **分布式文件存储**的开源数据库系统,由 C++ 编写,旨在为 **WEB应用**提供 **可拓展的高性能** 数据存储解决方案
+ MongoDB : 介于关系型数据库和非关系型数据库之间,非关系型数据库中功能最丰富,最像关系数据库的
+ MongoDB 将数据存储为一个**文档**,数据结构由 **键值对(key=>value)** 组成,MongoDB文档类似于 JSON 对象,字段值可以包含其他文档,数组以及文档数组

##### MongoDB 主要特点

1. MongoDB **文档数据库**,存储的是文档
2. MongoDB 内部执行引擎是 **JS解释器**.当我们存储一个文档时,文档将被保存为 BSON 格式,查询时将其转换为 JS 对象,可以通过 JS 语法操作
3. MongoDB 数据库和集合可以隐式创建

#### MongoDB 基础操作

+ 开启 多个端口的 Mongo 数据库 : `mongod --dbpath E:\data\db27018 --port 27018`

##### MongoDB 概念解析 

1. MongoDB 基本概念 : 文档、集合、数据库

2. SQL 和 MongoDB 术语比较

   | SQL 术语 / 概念 | MongoDB 术语 / 概念 | 解释 / 说明                            |
   | --------------- | ------------------- | -------------------------------------- |
   | database        | database            | 数据库                                 |
   | table           | collection          | 数据库表 / 集合                        |
   | row             | document            | 数据记录行 / 文档                      |
   | column          | field               | 数据字段 / 域                          |
   | index           | index               | 索引                                   |
   | table joins     |                     | 表链接 / MongoDB 不支持                |
   | primary key     | primary key         | 主键, MongoDB自动将 _id 字段设置为主键 |

3. MongoDB 数据库初步 : 一个 MongoDB 中可以**创建多个数据库**.MongoDB 的**单个实例**可以容纳**多个独立的数据库**,每一个都有自己的**集合和权限**,不同的数据库也放置在不同的文件中

   1. 基础操作指令
      1. `show dbs` : 显示所有数据库的列表
      2. `db` : 显示当前数据库对象或集合
      3. `use db_name` : 连接到一个指定的数据库
   2. 数据库命名要求 : 数据库名可以是满足以下条件的任意 UTF-8 字符串
      1. 不能是空字符串 ("")
      2. 不能含有**空格**,**点**,**$**,**/**,**`\`** 和 **`\0`** (空字符)
      3. 数据库名应该全小写,最多 64 字节
      4. 有些数据库名是保留的,有特殊作用的 
         + admin : 从权限角度看这是 root 数据库, 用于将新用户添加到此数据库，这个用户自动继承所有数据库权限.一些特定的服务器端命令也只能在这个数据库运行，eg: 关闭服务器、列出所有页面
         + local : 这个数据库永远不会被复制, 存储限于本地单台服务器的任意集合

4. 文档 : 一组 **键值对 (key=>value)** 即 (BSON) . MongoDB 文档不需要设置相同的字段,并且相同的字段不需要相同的数据类型

   + 注意点:
     1. 文档中 键/值 对是有序的
     2. 文档中的值不仅可以是在双引号里面的字符串,还可以是其他几种数据类型 (设置可以是整个嵌入的文档)
     3. MongoDB 区分类型和大小写
     4. MongoDB 文档中不能有重复的键
     5. 文档的键是字符串
   + 文档键命名规范
     1. 键不能含有 `\0` (空字符)，这个字符用来表示键的结尾
     2. `.` 和 `$` 有特殊意义,仅可以在特定环境下使用
     3. 以下划线开头的 键是保留的 
   + 文档的数据结构和 JSON 基本一样,所有存储在集合中的数据都是 BSON 格式 (BSON 是一种类 JSON 的一种二进制形式存储格式简称: Binary JSON)

5. 集合 : MongoDB 的文档组, 类似于 RDBMS (关系型数据库) 中的表格 (table)

   + 集合存在与数据库中,没有固定的结构

6. 合法的集合名

   1. 集合名不可以是空字符串 (" ")
   2. 集合名不能含有 `\0` 字符 (空字符，结尾标识)
   3. 集合名不可以是 `system.` 开头,此开头为系统集合保留的前缀
   4. 用户创建的集合名字不可以含有保留字段 (`$`)

##### MongoDB 创建数据库 与 删除数据库

1. 创建数据库
   + 语法 : MongoDB 创建数据库 (`use database_name`) 是**隐式创建**的, 如果数据库存在则切换到指定内容，如果不存在则创建
2. MongoDB 删除当前数据库
   1. 语法 : `db.dropDatabase()`
   2. 删除当前数据库,需要先进入删除的数据库 `use db_name` ，再执行删除命令 `db.dropDatabase()`

##### MongoDB 创建集合 与 删除集合

1. 查看已有集合 : `show tables` 或 `show collections`

2. MongoDB 创建集合

   1. 语法格式

      ```
      db.createCollection(name, options)
      ```

   2. 参数

      1. name : 集合名称

      2. options 可选参数, 指定有关内存的大小以及索引的选项

         | 字段        | 类型 | 描述                                                         |
         | ----------- | ---- | ------------------------------------------------------------ |
         | capped      | 布尔 | (可选)如果为 True : 创建固定集合 (有固定大小的集合), 达到最大值时自动覆盖最早的文档<br>当该值为 True 时,必需指定 size 参数 |
         | autoIndexId | 布尔 | (可选) 如果为 True 自动在 _id 字段创建索引,默认为 True       |
         | size        | 数值 | (可选) 为固定集合指定一个最大值(以字节计)<br>如果capped 为 True,也可以指定该字段 |
         | max         | 数值 | (可选) 指定固定集合中包含文档的最大数量                      |

   3. 插入文档时,MongoDB **首先**检查固定集合的 **size** 字段,然后检查 **max** 字段

   4. 隐式创建集合 : `db.collection_name.insert({key: value})`

3. MongoDB 删除集合

   + 语法格式

     ```
     db.collection.drop()
     ```

##### MongoDB 插入文档

+ MongoDB 使用 insert() 方法向集合中插入文档 : `db.集合名.insert(插入内容)`

+ 查看已插入文档 : `db.集合名.find()`

+ 两种单条插入方法

  1. 直接插入

     ```
     > use python
     switched to db python
     > db.python.find()
     > db.python.insert({title: '爬虫', by: 'offcn'})
     WriteResult({ "nInserted" : 1 })
     > db.python.find()                            })
     { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫", "by" : "offcn" }
     ```

  2. 定义变量后由变量插入

     ```
   > document = {title: '网络爬虫',by: 'text'}
     { "title" : "网络爬虫", "by" : "text" }
     > db.python.insert(document)
     WriteResult({ "nInserted" : 1 })
     > db.python.find()                     xt'}
     { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫", "by" : "offcn" }
     { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "by" : "text" }
     ```
  
+ 多条插入文档 : `db.集合名.insert([document1, document2, ...])`

##### MongoDB 查询表达式

+ MongoDB 中查询表达式相当于 sql 中的 where 子句查询条件,可以用来过滤数据<br>
  1. **等于** : `{field:value}` 表示 field = value

  2. **小于** : `{field:{$lt:value}}` 表示 field < value

  3. **大于** : `{field:{$gt:value}}` 表示 field > value

  4. **小于等于** : `{field:{$lte:value}}` 表示 field <= value

  5. **大于等于** : `{field:{$gte:value}}` 表示 field >= value

  6. **不等于** : `{field:{$ne:value}}` 表示 field != value

  7. **$not** : `{$not: [{条件1}, {条件2}, ...]}` 多个条件都不满足 

     + 实例: 取出不属于第三栏且不属于第十一栏目的商品 (与 **nin** 实例结果相同)

       ```mariadb
       db.goods.find({$not:[{cat_id:3}, {cat_id:11}]},{_id:0,goods_name:1,cat_id:1}).pretty()
       ```

       

  8. **$and** : `{$and: [{条件1}, {条件2}, ...]}` 多个条件同时满足,相当于逻辑中的且

  9. **$or** : `{$or: [{条件1}, {条件2}, ...]}` 多个条件满足其中之一,相当于逻辑关系中的或

  10.  **$nin** : `{ field: { $nin: [ <value1>, <value2> ... <valueN> ]} }` 该 field **值**不在指定范围 或 不存在

      + 实例: 取出不属于第三栏且不属于第十一栏目的商品

        ```mariadb
        db.goods.find({cat_id:{$nin: [3, 11]}},{_id:0,goods_name:1,cat_id:1}).count()
        // 14
        db.goods.find({cat_id:{$nin: [3, 11]}},{_id:0,goods_name:1,cat_id:1}).pretty()
        ```

        

##### MongoDB 更新文档

+ `update()` 方法 : 更新已存在的文档

  + 语法格式

    ```mariadb
    db.collection.update(
    	<query>,
    	<update>,
    	{
    		upsert: <boolean>,
    		multi: <boolean>,
    		writeConcern: <document>
    	}
    )
    ```

  + 参数说明

    1. **query** : 查询表达式
    2. **update** : update 的对象和一些更新的操作符 (如 $, $inc 等), 也可以理解为 sql (查询内 set 后面的内容,一般配合更新表达式操作)
    3. **upset** : **可选**,如果不存在 更新记录,是否插入 objNew,true 为插入, false 为不插入, 默认为 false
    4. **multi** : **可选**,MongoDB 默认 false,只更新找到的第一条记录,如果为 true,把按条件查出来的多条记录全部更新

+ 新文档替换旧文档

  + MongoDB update 方法中的 update 条件配合一定的更新表达式达到文档更新的目的

  + 如果 update 条件对应参数是一个文档,则该 update 方法的实际操作其实是 : 用 updata 条件对应的 文档替换 query 查询出来的文档

  + 命令格式

    ```mariadb
    > db.python.update({title:"爬虫"}, {title:"爬虫测试", by:"测试"})
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
    > db.python.find()                              试"})   "测试"})
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "by" : "测试" }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "by" : "text" }
    ```

    

+ 更新表达式参数

  + `$set` : 修改某列的值:有则更新，无则插入

    ```mariadb
    > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "by" : "测试" }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "by" : "text" }
    > db.python.update({title:"爬虫测试"}, {$set:{by:"李四"}})
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
    > db.python.find()                                  四"}})
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "by" : "李四" }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "by" : "text" }
    ```

  + `$unset` : 删除某个列

    + 默认删除匹配数据的第一个删除,需要删除更多的话,需要将 multi 参数 设为 true : `db.python.update({title:"爬虫测试"}, {$set:{by:"李四"}}, {multi:true})`

      ```mariadb
      > db.python.find()
      { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四", "uid" : "01", "price" : 160 }
      { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "后端开发", "创作者" : "AngleLiu", "uid" : "01", "price" : 180 }
      > db.python.update({uid:"01"}, {$unset: {price: 1}})
      WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
      > db.python.find()
      { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四", "uid" : "01" }
      { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "后端开发", "创作者" : "AngleLiu", "uid" : "01", "price" : 180 }
      ```

  + `$rename` : 重命名某个列

    ```mariadb
  > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "by" : "李四" }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "创作者" : "text" }
    > db.python.update({title:"爬虫测试"}, {$rename:{by:"创作者"}}, {multi:true})
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
    > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四" }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "网络爬虫", "创作者" : "text" }
    ```
  
  + `$inc` : 增长某个列(做减法)

    ```mariadb
  > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四", "uid" : "01", "price" : 200 }
  { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "后端开发", "创作者" : "AngleLiu", "uid" : "01", "price" : 200 }
    > db.python.update({uid:"01"}, {$inc:{price:-20}})
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
    > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四", "uid" : "01", "price" : 180 }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "后端开发", "创作者" : "AngleLiu", "uid" : "01", "price" : 200 }
    > db.python.update({uid:"01"}, {$inc:{price:-20}}, {multi:true})
    WriteResult({ "nMatched" : 2, "nUpserted" : 0, "nModified" : 2 })
    > db.python.find()
    { "_id" : ObjectId("5facdf85ae691aca255d6256"), "title" : "爬虫测试", "创作者" : "李四", "uid" : "01", "price" : 160 }
    { "_id" : ObjectId("5facdfd9ae691aca255d6257"), "title" : "后端开发", "创作者" : "AngleLiu", "uid" : "01", "price" : 180 }
    ```
  
    

##### MongoDB 删除文档

+ `remove()`方法 : 移除集合中数据

  + 基本语法格式

    ```mariadb
    db.集合名.remove(
    	<query>,
        {
        	justOne: <boolean>,
        	writeConcern: <document>
        }
    )
    ```

  + 参数

    1. **query**: **可选**,删除文档的条件,查询表达式
    2. **justOne** : **可选**,如果设置为 true 或 1,则只删除一个文档,默认全部删除
    3. **writeConcern** : **可选**, 抛出异常的级别

##### MongoDB 查询文档

+ MongoDB 查询文档使用 find() 方法

+ `find()` 方法: 以非结构的方式显示所有文档

  + 基本语法格式

    ```mariadb
    db.集合名.find(query, projection)
    ```

  + 参数

    1. **query** : **可选**,使用查询操作符指定查询条件
    2. **projection** : **可选**, 查询结果中是否显示列
       + 语法: `{field:1/0}`
         + 1 : 显示
         + 0 ： 不显示

+ `pretty()` 方法 : 结构化显示文档

  + 基本语法格式 : `db.集合名.find().pretty()`

    ```mariadb
    > db.python.find().pretty()
    {
            "_id" : ObjectId("5facdf85ae691aca255d6256"),
            "title" : "爬虫测试",
            "创作者" : "李四"
    }
    {
            "_id" : ObjectId("5facdfd9ae691aca255d6257"),
            "title" : "网络爬虫",
            "创作者" : "text"
    }
    ```

    

##### MongoDB 中的 limit、skip、sort、count 方法

1. `limit()` 方法: 读取指定数量的数据记录,接受一个数字参数,指定从 MongoDB 中读取记录条数

   + 基本语法 : `db.集合名.find().limit(Number)`

     ```mariadb
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1}).limit(3).pretty()
     {
             "_id" : ObjectId("5fad00c22b27f6c5659ca5e1"),
             "cat_id" : 4,
             "goods_name" : "KD876"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5ed"),
             "cat_id" : 4,
             "goods_name" : "诺基亚5800XM"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5"
     }
     ```

2. `skip()` 方法: 跳过指定数量的数据,接受一个数字参数做为跳过记录条数

   + 基本语法 : `db.集合名.find().limit(Number1).skip(Number2)`

     ```mariadb
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1}).limit(3).skip(2).pretty()
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5"
     }
     ```

3. `sort()` 方法 : 对数据进行排序,可以通过参数指定排序的字段,并使用 **1 (升序)** 和 **-1 (降序)** 指定排序方式

   + 基本语法 : `db.集合名.find().sort({KEY:1})`

     ```mariadb
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1}).limit(3).pretty()
     {
             "_id" : ObjectId("5fad00c22b27f6c5659ca5e1"),
             "cat_id" : 4,
             "goods_name" : "KD876"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5ed"),
             "cat_id" : 4,
             "goods_name" : "诺基亚5800XM"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5"
     }
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1}).limit(3).skip(2).pretty()
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5"
     }
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1}).limit(3).pretty()
     {
             "_id" : ObjectId("5fad00c22b27f6c5659ca5e1"),
             "cat_id" : 4,
             "goods_name" : "KD876"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5ed"),
             "cat_id" : 4,
             "goods_name" : "诺基亚5800XM"
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5"
     }
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1, shop_price:1}).limit(3).pretty()
     {
             "_id" : ObjectId("5fad00c22b27f6c5659ca5e1"),
             "cat_id" : 4,
             "goods_name" : "KD876",
             "shop_price" : 1388
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5ed"),
             "cat_id" : 4,
             "goods_name" : "诺基亚5800XM",
             "shop_price" : 2625
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5",
             "shop_price" : 2878
     }
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1, shop_price:1}).limit(3).sort({KEY:1}).pretty()
     {
             "_id" : ObjectId("5fad00c22b27f6c5659ca5e1"),
             "cat_id" : 4,
             "goods_name" : "KD876",
             "shop_price" : 1388
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5ed"),
             "cat_id" : 4,
             "goods_name" : "诺基亚5800XM",
             "shop_price" : 2625
     }
     {
             "_id" : ObjectId("5fad01002b27f6c5659ca5f1"),
             "cat_id" : 4,
             "goods_name" : "夏新T5",
             "shop_price" : 2878
     }
     ```

4. `count()` 方法 : 对数据数量进行统计

   + 基本语法 : `db.集合名.find().count()`

     ```mariadb
     > db.goods.find({cat_id:4},{cat_id:1, goods_name:1, shop_price:1}).count()
     3
     > db.goods.find({cat_id:4}).count()
     3
     > db.goods.find().count()
     31
     ```

##### MongoDB 导出数据

+ mongodb 数据库文件夹下的各种工具介绍<br>
  1. **mongo.exe** : 客户端工具
  2. **mongod.exe** : 服务端工具

+ 将 mongodb 中数据导出为其它文件数据 

  1. **mongoexport.exe** : 数据库导出工具

     + **-type** : 导出类型 (csv、txt、json等)

     + **-o** : 输出文件名 ,可以添加路径
     + **-d** : 导出数据库名

     + **-c** : 导出集合名
     + **-f** : 导出列名 (字段名)，多个字段以逗号隔开
     + **-q** : 查询表达式
     + **--pretty** : 以漂亮的打印格式JSON输出文档

  2. **mongoimport.exe** : 数据库导入工具