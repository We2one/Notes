### JavaScript

#### JavaScript 简介

+ 负责功能
  1. HTML 负责页面上有这个元素
  2. CSS 负责此元素的样式
  3. JS 负责元素的功能
+ JS 与 Python 
  + 共同点 : 都是一门脚本语言
  + 区别 : JavaScript 是浏览器解释执行的,是一门客户端脚本语言,通常被直接嵌入 HTML 页面
+ 脚本语言学习不同于 HTML 和 CSS,需要学习以下点:
  1. 基本数据类型
  2. 运算
  3. 流程控制
  4. 函数
  5. 对象

##### JavaScript 组成

1. DOM : 文档对象模型(Document Object Model),用于获取或者设置**文档中标签**的属性
2. BOM : 浏览器对象模型(Bowser Object Model),用来获取**浏览器**属性、行为

##### JavaScript 使用方式

1. 行内式

   ```js
   <input type='button' name="" onclick="alert('ok!');">
   ```

2. 页面 script 标签嵌入

   ```js
   <script type="text/javascript">
   	alert('hello world');
   </script>
   ```

3. 外部引入 (在script 标签上链接了外部的 JS 文件,script 当中写的 JS 代码就失效了)

   ```js
   <head>
   	<meta charset="utf-8">
   	<title>Title</title>
   	<script type="text/javascript" src="js/index.js"></script>
   </head>
   ```

4. HTML 中 CSS 与 JavaScript 使用

   + CSS 使用
     1. style 标签页内编写
     2. link 标签链接外部的 CSS 文件
   + JS 使用
     1. script 标签进行编写
     2. script 标签链接外部的 JS 文件

##### JavaScript 语法格式

1. 一条 JavaScript 语句应该以 ";" 结尾
2. JavaScript 注释
   1. 单行注释 : `//`
   2. 多行注释 : `/*注释内容*/`

##### JavaScript 语句输出

1. console.log() : 将结果输出到**浏览器控制台** (F12 到 控制台 Console 查看)

   ```html
   <input onclick="console.log('hello world');" type="button" value="点击">
   ```

2. alert() : 以**弹窗**形式输出内容

   ```html
   <script type="text/javascript">
       alert('你好')
   </script>
   ```

3. document.write() : 在**页面**显示内容

   ```html
   <script type="text/javascript">
       // alert('你好');
       document.write("你好")
   </script>
   ```

#### JS 变量和基本的数据类型

+ JavaScript 是一种弱类型语言,变量的类型由它的值决定

  + 定义变量关键字 `var` (全局作用域) ,同时定义多个变量用 "," 隔开,共用一个 var 关键字

    ```js
    var a = 123; // int
    var b = "123"; // string
    var c = "张三", d = 212;
    ```

  + 定义变量关键字 `let` (块级作用域) ,同时定义多个变量用 "," 隔开,共用一个 let 关键字

    ```js
    <script type="text/javascript">
        let d = 5, e = 6;
    </script>
    ```

  + `let` 与 `var` 异同

    1. 共同点 : var和let都有函数级作用域
    2. 不同点 ; 
       1. var 属于**ES5**规范，let 属于**ES6**规范
       2. var 没有块级作用域 , let 有块级作用域
       3. var 是全局作用域 , let 不是

  + 定义常量关键字 `const`

    1. const 定义的值不可以修改,必须初始化

    2. 常量的含义是指对象不能修改，但是可以改变对象内部的属性

       ```js
       const app = {
           id:1,
           name:"lhs"
       }
       app.name="ljq";
       console.log(app.name);//输出：ljq
       ```

##### 变量、函数、属性、函数命名规范

1. 字母数字下划线($)组成
2. 首字母不能为数字
3. 严格区分大小写
4. 不能使用关键字

##### 基本数据类型	

| 数据类型  | 代表                                        |
| --------- | ------------------------------------------- |
| string    | 字符串,用引号包围起来的字母、数字、其他符号 |
| number    | 数字                                        |
| boolean   | 布尔值 (true / false)                       |
| object    | 对象                                        |
| null      | 类似于 python 的 None                       |
| function  | 函数类型                                    |
| undefined | 如果变量是 undefined类型                    |

+ JS 查看数据类型的方法 : `typeof`

  ```js
  <script type="text/javascript">
      console.log(typeof "张三")
  </script>
  ```

#### JS 数据类型转换

1. 转换为字符串 : `String(转换数据)`

   ```js
   console.log(typeof (String(123)));
   ```

2. 转换为数字 : `Number(转换数据)` 或 `parseInt(转换数据)` 或 `parseFloat(转换数据)`

   ```js
   console.log(Number("123")) // 123
   console.log(Number("1.23")) // 1.23
   console.log(Number("1.23a")) // NaN
   console.log(parseInt("1.23")) // 1
   console.log(parseInt("1.23a")) // 1
   console.log(parseFloat("1.23")) // 1.23
   console.log(parseFloat("1.23a")) // 1.23
   ```

3. 布尔类型转换 (0 和 空 为 false) : `Boolean(转换数据)`

   ```js
   console.log(Boolean('a')) // true
   console.log(Boolean("")) // false
   ```

#### JS 运算符

##### 算术运算符

​	

| 运算符 | 描述 | 代码                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| +      | 加   | `num=12`<br/>`var c = num + 2` : 14                          |
| -      | 减   | `var d = num - 2` : 10                                       |
| *      | 乘   | `var e = num * 2` : 24                                       |
| /      | 除   | `var f = num / 2` : 6                                        |
| ++     | 递增 | 1. `var b = num++` (12) : 先赋值,再自增<br/>2. `var c = ++num` (14) : 先自增,再赋值 |
| --     | 递减 |                                                              |

##### 字符串连接

+ "+" : 拼接字符串 (JS 中数字与字符串相加只会形成新的字符串,不会报错)

  ```js
  cosole.log(1 + '23') // "123"
  ```

##### 赋值运算

​	

| 运算符 | 描述     |
| ------ | -------- |
| =      | 赋值     |
| +=     | 加等于   |
| -=     | 减等于   |
| %=     | 取模等于 |

##### 比较运算符

​	

| 运算符 | 描述           |
| ------ | -------------- |
| <      | 小于           |
| >      | 大于           |
| >=     | 大于等于       |
| <=     | 小于等于       |
| ==     | 等于           |
| ===    | 等值等型       |
| !=     | 不等于         |
| !==    | 不等值或不等型 |

##### 逻辑运算符

+ 运算符
  1. `&&` : and 与关系
  2. `||` : or 或关系
  3. `!` : 非关系

+ 注意事项
  + 逻辑运算符 与 比较运算符同时出现
  + 三种运算符优先级 : `!` > `&&` > `||`

##### 三目运算符

+ 格式 : `比较代码?条件1:条件2;`

+ 如果比较执行成功 --> 执行条件1;比较失败 --> 条件2

  ```js
  var num = 4>3?3:2; // 3
  ```

  

#### JS 流程控制

##### 判断语句

1. if 判断语句

   + 语法结构 (把范围较大的判断条件写在后面)

     ```js
     if(条件1){
     	满足条件1执行代码;
     }else if(条件2){
     	满足条件2执行代码;
     }else{
     	都不满足执行代码
     }
     ```

   + 例子

     ```js
     var num = 4>3?3:2;
     // document.write(num)
     if(num === 3){
         document.write("三目表达式执行成功")
     }else if(num === 2){
         document.write("三目表达式执行失败")
     }else{
         document.write("执行出错")
         }
     /*
     三目表达式执行成功
     */
     ```

     

2. switch 分支判断语句

   + 语法结构 

     ```js
     switch(条件){
     	case 结果1:
     		第一个结果执行代码;
     		Break;
         case 接过2:
         	第二个结果执行代码;
         	Break;
     }
     ```

   + 例子

     ```js
     let a = 4, b = 3
     let app = {
         a,
         b
     }
     switch (a>b?0:1){
         case 0:
             document.write("a>b");
             break;
         case 1:
             document.write("a<b");
             break
     }
     /*
     a>b
     */
     ```

     

3. 一个判断语句无论有多少分支,只有一个可以执行成功.

##### JS 循环

1. for 循环

   1. for in 循环

      ```js
      for (let i in "abcde"){
          document.write(i); // i 不是序列内元素,是序列的索引
          document.write("abcde"[i]); // 通过索引获取元素
      }
      /*
      0a1b2c3d4e
      */
      ```

   2. for 循环 : `for (初始值; 循环条件; 累加操作){执行代码}`

      ```js
      for (let i=0;i<10;i++){
          document.write(i); // 0123456789
      }
      ```

   3. for 死循环 (使 循环条件无限增加或减小)

      ```js
      for (let i=0;i>0;i++){
          document.write(i);
      }
      ```

2. while 循环 : `while(初始变量条件){执行代码; 初始变量改变;}`

   1. 普通 while 循环

      ```js
      let i = 0
      while (i<8){
          document.write(i); // 01234567
          i++;
      }
      ```

   2. while 死循环 (不设置循环条件)

      ```js
      let i = 0
      while (i){
          document.write(i);
          i++;
      }
      ```

3. 嵌套循环 : 外层循环一次,内层循环一遍

   ```js
   let num1 = "1234567890"
   let num2 = "0987654321"
   for (let i in num1){
       for (let j in num2){
           document.write(num1[i],num2[j],";");
       }
   }
   /*
   10;19;18;17;16;15;14;13;12;11;20;29;28;27;26;25;24;23;22;21;......
   */
   ```

   

4. break 和 continue

   1. break : 结束循环,不执行循环之后的代码,执行循环外代码
   2. continue : 结束本次循环,开始下一次循环,不执行此次循环之后的代码

#### 函数

+ 函数是对一个完整功能代码的封装
+ 用于多次不规律调用,使用函数编程,减少冗余代码,有利于保持代码一致性

##### 函数定义及调用

+ 格式

  ```js
  function 函数名(形参) {
  	内部代码;
  }
  函数名(传入实参); // 函数调用,不调用不执行
  ```

##### 函数参数

1. 传参

2. arguments : 特殊对象,无需指定参数名,可以访问所有参数

   ```js
   let num1 = "1234567890"
   let num2 = "0987654321"
   function get_num(num1, num2){
       console.log(num1); // 1234567890
       console.log(num2); // 0987654321
       console.log(arguments); // Arguments: 点击可查看 (0:1234567890,1:0987654321)
       // document.write(arguments); // [object Arguments]
       console.log(arguments[1]); // 0987654321
   }
   get_num(num1, num2)
   ```

3. 默认值参数

   ```js
   let num1 = 1234
   function get_num(num1,let num2=2){
       console.log(num2);
   }
   get_num(num1) // 2
   get_num(num1, 12) // 12
   ```

##### 函数返回值

+ return : 返回函数内容,结束函数,如果没有返回值,默认返回 undefined

  ```js
  let num1 = 12
  let num2 = 11
  
  function sum(num1, num2){
      return num1+num2;
  }
  document.write(sum(num1, num2)) // 23
  ```

##### 函数其他定义方式

1. 匿名函数 : JS 特效编写过程中使用较多

   ```js
   var a = function () {
   	console.log("hello");
   }
   a();
   ```

2. 自运行函数 : 函数定义的同时执行函数

   ```js
   (function() {
   	console.log("Hello");
   })();
   ```

#### JS 对象

##### 对象的定义方式

1. 使用 object 定义对象 (不常使用)

   ```js
   var person = new Object();
   person.firstName = "张三";
   person.lastName = "张四";
   person.money = function () {
   	console.log("工作");
   };
   console.log(person.firstName); // 张三
   console.log(person.lastName); // 张四
   person.money(); // 工作
   ```

   

2. 直接创建对象,用于开发者定义普通类

   ```js
   var person = {
   	firstName: "张三",
   	lastName: "张四",
   	money: function() {
   		console.log("工作");
   	}
   };
   console.log(person.firstName); // 张三
   console.log(person.lastName); // 张四
   person.money(); // 工作
   ```

   

3. 使用自定义构造函数定义类 (在框架上实例框架对象时使用)

   ```js
   function Person(firstName, lastName, money) {
   	this.firstName = firstName;
   	this.lastName = lastName;
   	this.money = money;
   }
   var p = new Person(
   	"张三",
   	"张四",
   	function () {
   		console.log("工作");
   	}
   );
   console.log(person.firstName); // 张三
   console.log(person.lastName); // 张四
   person.money(); // 工作
   ```

   

##### this 关键字

+ JS 中 this 指向调用对象的一方

  ```js
  function f() {
  	console.log(this) // window
  }
  f();
  var p = {
  	age: 18,
  	f: function () {
  		console.log(this); //p
  	}
  }
  ```

  