### MySQL 数据库

#### MySQL 安装

1. ##### 下载 mysql-8.0.19-winx64.zip 文件,解压到安装文件夹

2. ##### MySQL软件bin目录添加到PATH环境变量中 C:\mysql-8.0.19-winx64\bin

3. ##### 在MySQL解压目录下创建my.ini文件(注意把注释删除掉)

   ```
   [mysqld]
   # 设置3306端⼝
   port=3306
   # 设置mysql的安装⽬录
   basedir=c:\mysql-8.0.19-winx64
   # 设置mysql数据库的数据的存放⽬录
   datadir=c:\mysql-8.0.19-winx64\data
   # 允许最⼤连接数
   max_connections=200
   # 允许连接失败的次数。
   max_connect_errors=10
   # 服务端使⽤的字符集默认为UTF8
   character-set-server=UTF8MB4
   # 创建新表时将使⽤的默认存储引擎
   default-storage-engine=INNODB
   # 默认使⽤“mysql_native_password”插件认证
   #mysql_native_password
   default_authentication_plugin=mysql_native_password
   [mysql]
   # 设置mysql客户端默认字符集
   default-character-set=UTF8MB4
   [client]
   # 设置mysql客户端连接服务端时默认使⽤的端⼝
   port=3306
   default-character-set=UTF8MB4
   ```

4. ##### 安装MySQL服务 : 以管理员运行cmd,执行切换到解压文件的bin目录下，执行mysqld --install MySQL

5. ##### 初始化安装MySQL数据库在bin目录下执行 `mysqld --initialize-insecure`，无密码安装

6. ##### 启动 MySQL 服务 : `net start mysql`

7. #####  MySQL连接测试 `mysql -u root -p`

8. ##### 修改密码 

   ```
   ALTER user 'root'@'localhost'
   identified with mysql_native_password
   by 'root'
   ```

   

#### 数据库卸载

1. ##### 停止服务，删除mysql目录下剩余的所有文件，把mysql文件夹也删了,以管理员身份打开cmd然后执行下面的命令

   ```
   net stop mysql
   ```

2. ##### windows+R运行“regedit”文件，打开注册表

3. ##### 删除注册表：

   + HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL文件夹 

   + HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL文件夹

4. ##### 使用管理员权限进去cmd,sc delete 要删除的服务名 ,这里是MySQL

   ```
   sc delete mysql
   ```

   






#### 数据库操作

1. ##### 创建数据库

   + 基本语法格式

     ```mysql
     CREATE DATABASE db_name DEFAULT CHARSET=UTF8MD4;
     ```

     + CREATE : 创建命令
     + DATABASE : 数据库关键字
     + db_name : 自定义数据库名称

2. ##### 切换数据库

   + 基本语法格式

     ```mysql
     USE db_name;
     ```

3. ##### 查询数据库

   + 基本语法格式

     ```mysql
     SHOW databses;
     ```

4. ##### 删除数据库

   + 基本语法格式

     ```mysql
     DROP DATABASE db_name;
     ```

#### 数据表操作

 1. ##### 数据类型

    1. 数值型

       ​	

       |   类型    | 字节  |                    描述                     |
       | :-------: | :---: | :-----------------------------------------: |
       |  TINYINT  | 1字节 |                 (-128, 127)                 |
       | SMALLINT  | 2字节 |               (-32768, 32767)               |
       | MEDIUMINT | 3字节 |            (-83388608, 83388607)            |
       |  **INT**  | 4字节 |                    整数                     |
       |  BIGINT   | 8字节 |                                             |
       | **FLOAT** | 4字节 |                                             |
       |  DOUBLE   | 8字节 |                   浮点数                    |
       |  DECIMAL  |       | DECIMAL(M,D),M>D为M+2否则为D+2 [自定义精度] |

    2. 时间日期型

       |     类型     | 字节   | 描述                              |
       | :----------: | ------ | --------------------------------- |
       |   **DATE**   | 3 字节 | 年-月-日                          |
       |   **TIME**   | 3 字节 | 时-分-秒                          |
       | **DATETIME** | 8 字节 | 年-月-日-时-分-秒                 |
       |     YEAR     | 1 字节 | 年                                |
       |  TIMESTAMP   | 4 字节 | 从1970-01-01 00:00:00到现在时间戳 |

    3. 字符串型

       | 类型        | 字节              |             描述              |
       | ----------- | ----------------- | :---------------------------: |
       | **CHAR**    | **0-255 字节**    |        **定长字符串**         |
       | **VARCHAR** | **0-65535 字节**  |        **变长字符串**         |
       | TINYBLOB    | 0-255 字节        | 不超过255个字符的二进制字数串 |
       | BLOB        | 0-65535 字节      |     二进制形式长文本数据      |
       | MEDIUMBLOB  | 0-16777215 字节   |  二进制形式中等长度文本数据   |
       | LONGBLOB    | 0-4294967295 字节 |    二进制形式极大文本数据     |
       | TINYTEXT    | 0-255 字节        |         短文本字数串          |
       | TEXT        | 0-65535 字节      |          长文本数据           |
       | MEDIUMTEXT  | 0-16777215 字节   |       中等长度文本数据        |
       | LONGTEXT    | 0-4294967295 字节 |         极大文本数据          |

    3. **VARCHAR 、CHAR 与 TEXT**
       
       + **CHAR** : 定长格式,长度范围 0-255,不足255长度的字符时,MySQL会用空格填充剩下字符,读取数据时,char 类型数据要进行处理,把后面空格去除
       + **VARCHAR** : V5.0.3 以下版本最大长度限制 255;V5.0.3以上版本最大长度限制 65532 (起始结束位占3个字节) 字节 
       + **TEXT** : 不可以有默认值数据,最大长度 2^16-1
       + 尽量使用 VARCHAR, 经常变化的字段使用 VARCHAR ,可以使用 VARCHAR 就不要使用 TEXT，超过 255 字符的只能用 VARCHAR 与 TEXT,知道固定长度用CHAR

2. ##### 查询数据表

     + 基本语法格式	

         ```mysql
         SHOW TABLES;
         ```

     + 查询表字段信息

       ```mysql
       desc tab_name;
       ```

       

3. ##### 创建数据表

   + 基本语法格式

     ```mysql
     CREATE TABLE tab_name(
     id INT PRIMARY KEY AUTO_INCREMENT COMMENT "注释",
     name VARCHAR(20) NOT NULL COMMENT "注释",
     date DATETIME COMMENT "注释"
     )DEFAULT CHARACTER SET 'UTF8MB4';
     ```

     + AUTO_INCREMENT : 自动增加
     + COMMENT : 注释
     + DEFAULT CHARACTER SET 'UTF8MB4' : 设置内容编码格式

4. ##### 修改列字段

   1. 增加列字段

      + 基本语法

        ```mysql
        ALTER TABLE tab_name 
        	ADD col_name 列定义 [FIRST | AFTER old_col_name]
     ```
   
   + 案例
   
     1. 末尾增加一列
   
           ```mysql
           ALTER TABLE tab_name
           	ADD col_name VARCHAR(200);
        ```
   
     2. 开头位置增加列
   
           ```mysql
           ALTER TABLE tab_name
           	ADD col_name VARCHAR(200) FIRST;
        ```
   
     3. 指定位置增加一列 (emp_name 列后增加的)
   
           ```mysql
           ALTER TABLE tab_name
           	ADD col_name VARCHAR(200)
           	AFTER emp_name;
        ```
   
2. 删除列字段
   
   + 基本语法
   
        ```mysql
        ALTER TABLE tab_name DROP col_name;
     ```
   
3. 修改列字段
   
      + 基本语法
   
     ```mysql
        ALTER TABLE tab_name
     	CHANGE old_col_name new_col_name 列定义 字段类型约束
        
     ALTER TABLE tab_name
        	MODIFY col_name 列定义 字段类型约束
        ```
   
      + 操作案例
   
        1. 设置列默认值
   
        ```mysql
           ALTER TABLE tab_name
        	ALTER col_name SET DEFAULT "默认值";
           ```

        2. 修改列类型
   
           ```mysql
           ALTER TABLE tab_name
        	MODIFY col_name VARCHAR(200);
           ```

        3. 修改列名
   
           ```mysql
           ALTER TABLE tab_name
        	CHANGE old_col_name new_col_name VARCHAR(100);
           ```

   5. ##### 重命名数据表
   
      + 基本语法
   
     ```mysql
        ALTER TABLE old_tab_name RENAME AS/TO new_tab_name;
     ```
   
6. ##### 删除数据表
   
      + 基本语法
   
     ```mysql
        DROP TABLE tab_name;
     ```
   
6. ##### 数据表约束
   
      1. **表约束** : 对数据格式和数据内容的限制
      2. **主键约束 (PRIMARY KEY)** :  标注表中每条记录都是唯一的标识
   3. **外键约束 (FOREIGN KEY)** : 标注当前数据表与其他数据表之间的关联关系
         + 逻辑外键 : 在逻辑上有关联关系 (外键字段不加约束)
      + 物理外键 : 外键字段添加约束，删除时如果与其他表有外键约束,无法删除
      4. **唯一约束 (UNIQUE)** : 标注当前字段数据的唯一性
      5. **默认约束 (DEFAULT)** : 标注当前字段默认数据
      6. **非空约束 (NOT NULL)** : 标注当前字段数据不能为空
      7. **自增约束 (AUTO_INCREMENT)** : 标注当前字段数据默认 +1 一般配合主键使用
      8. **无符号 (UNSIGNED)** : 数值类型，无符号代表正数

#### 导出数据为 CSV 文件

1. ##### 方法一、导出时包括列名

   + 必须在 **git bash** 内运行 win 下没有 **sed**

   + 实例

     ```
     mysql -u root -p -e "select * from db_name.table_name" | sed -e "s/\t/,/g" -e "s/NULL/  /g" -e "s/\n/\r\n/g" > d:/test.csv
     ```

   + `sed -e "s/\t/,/g" -e "s/NULL/  /g" -e "s/\n/\r\n/g"` 

     + `-e "s/\t/,/g"` : 将 数据库中 **列**转化为 **,** 隔开
     + `-e "s/NULL/  /g"` : 将 数据库中 的 **NULL** 数据转化到 csv 文件中为 **空**
     + `-e "s/\n/\r\n/g"` : 将数据库中的 每一**列**数据 转化到 csv 中 用 **\n** 换行

2. ##### 方法二、mysql 语句导出，不包含列名

   + **select .... into outfile** : 直接在mysql的交互界面使用select命令导出数据到文件

   + 实例 -- > 保存为 csv

     ```
     select * from table_name
     into outfile "/db/test1.csv"
     fields terminated by "," # 描述字段的分隔符，默认情况下是tab字符（\t） 
     optionally enclosed by '"' # 描述的是字段的括起字符。
     escaped by "\" # 描述的转义字符。默认的是反斜杠（backslash：\ )
     lines terminated by "\n"; # 行与行之间的分隔
     ```

3. ##### 方法三、Navicat 导出

#### 数据 CRUD

1. ##### INSERT 增加数据

   + 基本语法

     ```mysql
     INSERT INTO tab_name [(col_name, ...)]
     	VALUES 
     	(...),
     	(...);
     ```

     

   1. 增加单条数据  (如果不指定列,表示所有列都增加数据;指定列字段,则只给指定的列字段增加数据)

      1. 不指定列

         ```mysql
         INSERT INTO tab_name VALUES(..., ...);
         ```

      2. 指定列

         ```mysql
         INSERT INTO tab_name(col_name1, col_name2, ...)
         	VALUES(val1, val2n ...);
         ```

         

   2. 增加多条数据

      ```mysql
      INSERT INTO tab_name
      VALUES
      (val1, val2, ...),
      (val1, val2, ...);
      ```

      

   3. 查询增加数据

      1. 复制表结构创建历史表 (如果不写 WHERE false 条件,表中的数据也会被复制)

         ```mysql
         CREATE TABLE new_tab
         	SELECT * FROM old_tab WHERE 1=2;
         ```

      2. 查询的方式将当前表中的数据迁移到历史表

         ```mysql
         INSERT INTO new_tab
         	SELECT * FROM old_tab;
         ```

2. ##### DELETE 删除数据

   + 基本语法

     ```mysql
     DELETE FROM tab_name [WHERE 条件];
     ```

   1. 全表删除 (清空表中数据)

      1. **`TRUNCATE TABLE [tab_name]`** : 删除表中数据,包括重置主键编号等，变为空表

         ```mysql
         TRUNCATE TABLE tab_name;
         ```

      2. **`DELETE FROM [tab_name]`** :  仅仅删除表中数据,其他标的特征信息不变

         ```mysql
         DELECT FROM tab_name;
         ```

   2. **`DELECT`** : 指定条件筛选删除,避免误伤 

      ```mysql
      DELECT FROM tab_name WHERE 条件;
      ```

   3. **`LIMIT`** : 指定删除数量,防止删除引起 CPU 大量占用

      ```mysql
      DELECT FROM tab_name LIMIT 删除数目n;
      ```

3. ##### UPDATE 修改数据 (修改过程中一定要条件明确)

   + 基本语法

     ```mysql
     UPDATE tab_name
     	SET col_name1=修改数据1,
     	col_name2=修改数据2...
     	[WHERE 条件];
     ```

4. ##### SELECT 查询数据

   1. 单表查询 (基于单个数据表的查询)

      1. 全表查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name;
           ```

      2. 指向字段查询

         + 基本语法

           ```mysql
           SELECT col_name1, col_name2 FROM tab_name;
           ```

      3. 剔重字段查询

         + 基本语法

           ```mysql
           SELECT DISTINCT col_name FROM tab_name;
           ```

      4. 单条件比较查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name WHERE 条件;
           ```

      5. 多条件逻辑与查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name
           	WHERE 条件1 and 条件2
           ```

      6. 多条件逻辑或查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name
           	WHERE 条件1 or 条件2;
           ```

      7. BETWEEN...AND 范围查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name
           	WHERE col_name BETWEEN 开始范围 AND 结束范围;
           ```

      8. IN 范围查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name
           	WHERE col_name IN (范围内容);
           SELECT * FROM tab_name
           	WHERE col_name NOT IN (范围内容);
           ```

      9. IS NULL 空值查询

         + 基本语法

           ```mysql
           SELECT * FROM tab_name
           	WHERE col_name IS NULL;
           SELECT * FROM tab_name
           	WHERE col_name IS NOT NULL;
           ```

      10. 模糊查询

          + 基本语法 (% 匹配任意多个字符,_匹配单个字符)

            ```mysql
            SELECT * FROM tab_name
            	WHERE col_name LIKE '模糊查询内容(eg: %头领)'
            ```

      11. 排序查询

          + 基本语法 (默认顺序ESC, 倒序 DESC)

            ```mysql
            SELECT * FROM tab_name
            	ORDER BY col_name DESC;
            ```

      12. 分页查询

          + 基本语法

            ```mysql
            SELECT * FROM tab_name
            	ORDER BY tab_name DESC
            	LIMIT 起始序号(start), 检索数量(size);
            ```

      13. 分组查询

          + 基本语法

            ```mysql
            SELECT GROUP_CONCAT(col_name1), col_name2
            	FROM tab_name
            	GROUP BY col_name
            	HAVING 条件;
            ```
      
      
   
2. 聚合查询 (通过 MySQL 内建聚合函数,完成数据库中查询数据的聚合运算结果)
   
    1. count() : 按照指定的条件,查询数据表中所有记录数
      
       + 基本语法
       
            ```mysql
            SELECT count(col_name\*) FROM tab_name;
         ```
      
   2. sum() : 求和函数,查询指定列所有数据和
   
      + 基本语法
   
           ```mysql
           SELECT sum(col_name) FROM tab_name;
        ```
   
   3. avg() : 求平均值函数
   
      + 基本语法
   
           ```mysql
           SELECT avg(col_name) FROM tab_name;
        ```
   
   4. max() : 查询指定列最大值
   
      + 基本语法
   
           ```mysql
           SELECT max(col_name) FROM tab_name;
        ```
   
   5. min() : 查询指定列最小值
   
      + 基本语法
   
           ```mysql
           SELECT min(col_name) FROM tab_name;
        ```
   
         



