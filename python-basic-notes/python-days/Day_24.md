#### 索引

 1. ###### 索引介绍

    + 索引 : 是一种**提升查询速度**的, 特殊的**存储结构**
    + 包含了对数据表里的记录的指针,类似于字典的目录
    + 添加索引时, 会单独创建一张表去存储和和管理索引, 索引比原数据大,占用更多资源

	2. ##### 索引的种类

    	1. 普通索引 index
        + index : 可以为空、可以重复
    	2. 唯一索引 unique
        + 可以为空但不可以重复
    	3. 主键索引 primary key
        + 不可以为空不可以重复
    	4. 多列索引
        + 为多个字段添加一个索引

	3. ##### 索引的优缺点

    + 优点
      + 提升查询速度
      + 通过建立唯一索引保证数据的唯一性
    + 缺点
      + 索引需要占据更多的物理空间
      + 增加后期维护成本
      + 降低增删改操作的效率

	4. ##### 索引是否越多越好？

    + 数据量较大的时候可以使用索引
    + 经常用 where 查询的字段添加索引
    + 字段重复率过高就不推荐添加索引,添加会降低查询速度
    + 使用索引时遵循 最左原则
    + 多列索引查询时,注意字段顺序

	5. ##### 索引操作

    	1. 添加索引

        	1. 建表时添加索引 primary key

        	2. 表建好之后添加索引

            ```mysql
            ALTER TABLE tab_name
            ADD 索引类型 [索引名](字段名);
            ```

    2. 查看索引

       ```mysql
       SHOW INDEX FROM tab_name;
       ```

    3. 删除索引

       ```mysql
       DROP INDEX 索引名 
       ON tab_name;
       ```

    4. 删除主键索引 : 必须先去除主键索引的自增属性, 然后执行

       ```mysql
       ALTER TABLE tab_name
       DROP PRIMARY KEY;
       ```

6. ##### 索引的实现 (存储结构划分)

   1. HASH 索引
      + 基于哈希表实现,只有精确匹配索引所有的列查询才有效,对于每一行数据,存储引擎会对于所有的索引类列计算一个哈希码,并且hash索引将所有的哈希码存储在索引中,同时索引表中保存指向每个数据的指针
      + 哈希索引能够最快的进行数据定位,对于固定的数据查询效率很高,对于范围性的查询,因为HASH索引的不连续性,查询性能会下降.
   2. B Tree 索引
      1. B- Tree 索引
         + B-Tree能加快数据的访问速度,存储引擎不在需要全表扫描,数据分布在各个节点之中
      2. B+ Tree 索引
   3. full-index 全文索引
   4. R- Tree 索引

#### 视图

 1. ##### 视图的定义

     	1. **视图是一个虚拟的表**,**从一个或者多个表中导出来的数据组成的虚拟的表**.并不在库中真是存在,作用和真是的表一样,包含一些列带有行和列的数据.
          	2. 视图中的数据依赖源表当源表中的数据发生变化时,视图中的数据也会发生变化.
          	3. 视图中的数据默认是只读的,不允许通过视图直接进行数据改动.

 2. ##### 视图的定义

     1. 创建视图

        ```mysql
        CREATE VIEW 视图名 
        AS sql查询语句;
        ```

    2. 使用视图

       ```mysql
       SELECT * FROM 视图名;
       ```

    3. 查看视图

       ```mysql
       SHOW TABLE status WHERE comment='view';
       ```

    4. 删除视图

       ```mysql
       DROP VIEW 视图名;
       ```

	3.  ##### 视图的优缺点

    	1. 优点
        	1. 视图使用简单 ： 使用视图的用户完全不同关心后面对应的表结构,关联条件是什么和筛选条件是什么, 对于用户来说,已经是过滤好的符合条件的结构.
        	2. 视图使用安全 : 使用视图的用户只能访问被允许的查询结构集,数据库提供权限管理并不能限制某一列,通过视图可以简单的实现
        	3. 视图内数据独立 : 一旦视图被创建了,视图的结构不会受到原表结构的变化而变化, 当视图创建了,如果在给原表添加字段,也不会对视图造成影响
    	2. 缺点
        	1. 视图的性能 : 通过视图查询数据速度会很慢,特别是基于视图创建的视图, 简单查询存入视图,利用视图查询数据,会变成复杂查询

#### 触发器

 + ##### 由事件来触发,当对一个表进行操作 (insert, delete, update) 时就会激活它执行

 + ##### 基础命令 (固定格式)

    + 创建触发器

       ```mysql
       CREATE TRIGGER 触发器名字tri_name 触发时机 事件
       ON tab_name 
       FOR EACH ROW
       BEGIN
        需要执行的 SQL 语句
       END;
       ```
       
    + 数据备份 (当去表内删除数据时,对删除的数据进行备份)

       1. 创建表结构与删除数据表一样的备份表

          ```mysql
          create table 原表名 as select * from 备份表名 where 1=2;
          ```

          + 添加数据 (将 表a 的数据添加到 表b)

            ```mysql
            create table 表名a as select * from 表名b
            ```

       2. 创建触发器
       		1. 修改默认结束符 ";" 	
       			```
       			\d ||
       		```

			2. 创建触发器
              ```mysql
              create trigger tri_name 
              befor delete on 原表名
              for each row
              begin
                insert into 备份表名 values(old.id,old.name,....);
              end;
              ```

          

    + 查看触发器

       ```mysql
       SELECT * FROM INFORMATION_SCHEMA.TRIGGERS;
       ```

    + 删除触发器

      ```mysql
      DROP TRIGGERS 触发器名字tri_name;
      ```

#### 用户权限管理

 1. ##### 添加用户  (来源地: 是否允许用户在其他地方登陆, %代表任意来源地)

    ```mysql
    CREATE USER '用户名'@'来源地' IDENTIFIED BY '密码';
    ```

	2. ##### 删除用户

    ```mysql
    drop user '用户名'@'来源地'
    ```

2. ##### 授权操作  (\*.\* 库名.表名： 对当前所有库和表都具有权限)

   ```mysql
   GRANT 权限 ON 库名.表名 TO '用户名'@'来源地';
   ```

   + insert : 插入
   + select : 查询
   + update : 更新

4. ##### 权限回收

   ```mysql
   REVOKE UPDATE ON *.* FROM '用户名'@'来源地';
   ```

4. ##### 修改密码

   1. 先查看 mysql 库中的 user 表中,用户是否有密码

      ```mysql
      SELECT *
      FROM user 
      WHERE user='用户名'\G;
      ```

      

   2. 如果有密码需要先删除 (置空)

      ```mysql
      UPDATE user 
      SET authentication_string=""
      where user='user_name';
      ```

      

   3. 重新设置新的密码

      ```mysql
      alter user '用户名'@'来源地' identified by '新密码';
      ```

      

#### 快捷键

 1. ##### \d : 改变数据库结尾 ";" 为 指定结尾

    ```mysql
    \d ||
    ```

2. \q : 退出数据库

3. \c : 放弃此次编辑,不报错

4. \G : 格式化显示数据

#### Python 连接数据库

 1. ##### 安装 Pymysql

    ```
    pip install pymysql
    ```

2. ##### 导入模块

   ```python
   import pymysql
   ```

   

3. ##### 连接数据库 (cursorclass : 显示为字典)

   ```python
   db = pymysql.connect(host='localhost', user='root',password='',database='', port=3306, cursorclass=pymysql.cursors.DictCursor)
   ```

4. ##### 创建游标

   ```python
   cursor = db.cursor()
   ```

   

1. ##### 编写 sql 语句

   ```
   sql = "mysql 语句"
   ```

   

2. ##### 执行/传入 sql 语句 (如果 sql 语句要求传参)

   ```
   cursor.execute(sql, (参数1,餐数2,))
   ```

   

7. ##### 获取结果

   1.  获取一条数据

      ```
      res = cursor.fetchone()
      ```

   2.  获取指定条数据

      ```
   res = cursor.fetchmany(size)
      ```
   
      ```
   res = cursor.fetchmany(2)
      print(res)
      """
      ((10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26)), (10002, datetime.date(1964, 6, 2), 'Bezalel', 'Simmel', 'F', datetime.date(1985, 11, 21)))
      """
      ```
   
   3. 获取所有数据

      ```
   res = cursor.fetchall()
      ```

      
   
8. ##### 退出数据库,关闭游标与数据库

   ```
   db.commit()
   cursor.close()
   db.close()
   ```

   