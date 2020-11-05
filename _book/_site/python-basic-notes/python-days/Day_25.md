### 存储过程  -->  一行或多行 SQL 语句

#### 存储过程和函数的创建 --> 可以在 SQL 语句 或 其他存储过程和函数调用 中执行和调用

 1. ##### CREATE PROCEDURE : 创建存储过程

    + 基本语法

      ``` mysql
      CREATE PROCEDURE proc_name ([proc_parameters])
      [characteristics] routing_body;
      ```
      + proc_name : 创建的存储过程名称

      + proc_parameters : 执行存储过程时的参数

      + [IN | OUT | INOUT]  parameter_name : 存储过程的参数
          + IN : 输入参数
          + OUT : 输出参数
          + INOUT : 输入或输出参数
          
      + routing_body : 存储过程执行体 --> 将多个 SQL 语句包含在 BEGIN ... END 之间,描述存储过程的功能主体

          ```mysql
          \d ||
          CREATE PROCEDURE proc_name()
          begin
          SQL 语句;
          end||
          ```

          

    + 调用执行

      ```mysql
      call proc_name(@参数);
      ```

      

 2. ##### 存储过程基础语法

     1. 变量使用 --> 临时存储数据,通过变量进行

        + 定义变量

          ```mysql
          DECLARE @var_name [, @var_name2,]... date_type [default value];
          ```

          + DECLARE : 声明一个变量
          + var_name : 声明变量的名称, 可以一次或多次声明
          + date_type : 变量类型
          + default value : 变量的默认数据

        + 变量赋值

          ```mysql
          SET @var_name = expr [, @var_name = expr2];
          ```

          + SET : 变量赋值
          + var_name : 正在赋值的变量, 一般情况下为了区分变量和其它关键字的区别,变量前用 @ 标识
          + expr : 变量的值, 可以是具体数据, 也可以是表达式

     2. 流程处理  --> 顺序处理结构、选择结构、循环结构

        + if 选择结构 基本语法

          ```mysql
          if 条件
          then
          	条件满足时的sql语句
          end if;
          ```

        + case 选择结构基本语法

          ```mysql
          case 变量
          when 值1 then
          	执行语句
          when 值2 then
          	执行语句
          else
          	执行语句
          end case;
          ```

        + while 循环结构基本语法

          ```mysql
          while 条件 do
          	执行语句
          end while;
          ```

        + loop 循环结构基本语法

          ```mysql
          MY_LOOP_TAG:loop
          	执行语句
              [leave MY_LOOP_TAG]
          end loop;
          ```

#### 函数

1. ##### CASE 流程函数

   + 基本语法

     ```mysql
     -- 值匹配
     CASE value
     	WHEN [compare-value] THEN result
     	[WHEN [compare-value] THEN result ...]
     	[ELSE result] 
     END;
     -- 表达式匹配
     CASE WHEN [condition] THEN result
     	[WHEN [condition] THEN result ...]
     	[ELSE result]
     END;
     ```

   + 案例

     ```mysql
     -- 值匹配
     SELECT CASE 'a'
     	WHEN 'A' THEN '优秀'
     	WHEN 'B' THEN '良好'
     	ELSE 'three'
     END;
     -- 表达式匹配
     SELECT CASE 
     	WHEN 100 > 80 THEN '大于关系成立'
     	WHEN 100 < 80 THEN '小于关系成立'
     	ELSE '其他关系'
     END;
     ```

2. ##### IF 流程函数

   + 基本语法

     ```mysql
     -- 基本 IF 流程函数 : 条件为 expr1, 条件为 True则返回 expr2, 否则返回 expr3
     IF (expr1, expr2, expr3)
     -- 简化 NULL 判断操作 : 如果 expr1 表达式不为 NULL 则返回 expr1, 否则返回 expr2; 发回值为数字或字符串
     IFNULL(expr1, expr2)
     -- 检查 等价判断操作 : 如果 expr1 和 expr2 相等则返回 NULL,否则返回 expr1
     NULLIF(expr1, expr2)
     ```

   + 案例

     ```mysql
     -- IF 判断
     SELECT IF(1, '条件成立', '条件不成立'); -- 条件成立
     -- IFNULL 判断
     SELECT IFNULL(NULL, 'hello'); -- hello
     -- NULLIF 判断
     SELECT NULLIF(12, 11); -- 12
     SELECT NULLIF(12, 12); -- NULL
     ```

3. ##### 内置函数

   + 字符串处理函数
     + concat(s1, s2, ... sn) : 连接 s1, s2, ... sn 为一个字符串
     + length(str) : 返回值为字符串 str 的长度
   + 数值函数
     + abs(x) : 返回 x 的绝对值
     + round(x, y) : 返回参数 x 的四舍五入的有 y 位小数的值
   + 日期和事件函数
     + now() : 返回当前日期和时间
     + unix_timestamp(date) : 返回  date 时间的 unix 时间戳
     + date_fomat(date, fmt) : 返回按字符串 fmt 格式化日期 date 值
     + datediff(expr1, expr2) : 返回起始时间和结束时间的间隔天数
   + 其他常用函数
     + database() : 返回当前数据库名
     + version() : 返回当前数据库版本
     + user() : 返回当前登录用户名
     + inet_aton : 返回当前 IP 地址的数字表示  `inet_aton('192.168.1.1')`
     + inet_ntoa(num) : 返回当前数字表示的 IP `inet_ntoa(3232256250)`
     + password(str) : 返回当前 str 的加密版本
     + md5(str) : 返回字符串 str 的 md5 值

#### 管理员密码丢失处理

 1. ##### 通过系统服务停止 MySQL 服务,或者在命令窗口直接执行命令停止数据库服务

    ```
    net stop mysql
    ```

2. ##### 创建一个 SQL 文件,将修改密码的命令添加到文件

   ```mysql
   alter user 'root'@'localhost' identified by 'new_password';
   ```

3. ##### 启动服务器, 使用 mysqld 命令 附带 --init-file 参数执行命令

   ```
   mysqld --init-filed=SQL文件path --console
   ```

#### 数据库三范式

1. ##### 第一范式(1NF)

   + 要求数据库表的每一列都是不可分割的原子数据项

2. ##### 第二范式(2NF)

   + 数据库表中的每一列都与主键相关,而不能只与主键的某一部分相关

3. ##### 第三范式(3NF)

   + 需要确保数据表中的每一列数据都和主键直接相关,而不能间接相关;在多表关系中,当前表中只能存储另一张表的主键字段,不能存储其他表的非主键字段