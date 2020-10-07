### JavaScript

#### 1.DOM 操作

##### 1.1 DOM 简介

+ DOM (document object model 文档对象模型): 是 HTML 整个页面的文本内容的对象

+ Document 中每一个元素都可以认为是一个 Element 对象 

  + `document.all` : 当前页面所有标签
  + `document.images` : 当前页面所有 img 标签对象
  + `document.forms` : 当前页面所有 form 表单标签对象
  + `document.links` : 当前页面所有链接

  

##### 1.2 元素获取(document内置方法)

1. `.getElementById()` : 获取页面上设置 id 属性的元素,获取到的是一个 HTML 对象,然后将其赋值给一个变量

   ```html
   <div>
       <p id="p1">你好哥们</p>
   </div>
   <script>
       var id1 = document.getElementById('p1')
       console.log(id1)
   </script>
   /*
   <p id="p1">你好哥们</p>
   */
   ```

2. `.getElementByClassName()` : 通过类名获取元素,返回数组对象

   ```html
   <div>
       <p class="x">1</p>
       <p class="x">2</p>
       <p class="x">3</p>
   </div>
   <script>
       var id1 = document.getElementsByClassName('x')
       console.log(id1)
   </script>
   /*
   HTMLCollection(3)
   	0: p.x
   	1: p.x
   	2: p.x
   	length: 3
   */
   ```

3. `.getElementsByTagName()` : 通过标签名获取元素对象,返回类数组对象

   ```html
   <div>
       <p class="x1">1</p>
       <p class="x2">2</p>
       <p class="x3">3</p>
   </div>
   <script>
       var id1 = document.getElementsByTagName('p')
       console.log(id1)
   </script>
   /*
   HTMLCollection(3)
   	0: p.x1
   	1: p.x2
   	2: p.x3
   	length: 3
   */
   ```

4. `.getElementsByName()` : 获取当前页面所有指定 name 值的标签

   ```html
   <div class="x1" name="1">1</div>
   <div class="x2" name="1">2</div>
   <div class="x3" name="2">3</div>
   <script>
       var id1 = document.getElementsByName('1')
       console.log(id1)
   </script>
   /*
   NodeList(2)
   	0: div.x1
   	1: div.x2
   	length: 2
   */
   ```

   

##### 1.3 样式操作

+ `document.getElementByID` : 获取的是单个对象时

  + 通过 style 修改样式,style 后面可以加当前标签可以用的所有 CSS 属性

    ```html
    <div class="x1" name="1" id="pink_box"></div>
    <script>
        var p_box = document.getElementById('pink_box');
        p_box.style.width = '100px';
        p_box.style.height = '100px';
        p_box.style.backgroundColor = "pink";
    </script>
    ```

+ `document.getElementsById` 或 ``document.getElementsByName`` 或 `getElementsByTagName()`: 获取对象列表

  + 通过索引或循环后加 style

    ```html
    <ol>
        <li>Python</li>
        <li>Linux</li>
        <li>Shell</li>
        <li>MySql</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ol>
    <script>
        var lis = document.getElementsByTagName('li');
        for (var i in lis){
            if (i % 2 === 1){
                lis[i].style.backgroundColor = "pink";
            }else {
                lis[i].style.backgroundColor = 'blue';
            };
            lis[i].style.color = 'white';
        };
    </script>
    ```

+ 通过索引获取元素对象

  ```html
  <div class="x1" name="1">1</div>
  <div class="x2" name="1">2</div>
  <div class="x3" name="2">3</div>
  <script>
      var div = document.getElementsByTagName('div')
      div[1].style.height = '100px';
      div[1].style.width = '100px';
      div[1].style.backgroundColor = 'pink';
  </script>
  ```

+ 设置样式属性步骤
  1. 获取元素 : 确定获取到的是元素对象还是包含元素对象的数组
  2. 设置元素样式

##### 1.4 属性操作

1. `.hasAttribute("判断属性")` : 判断指定元素是否有指定属性

   ```html
   <div class="x1" name="1" id="pink_box">1</div>
   <div class="x2" name="1">2</div>
   <div class="x3" name="2">3</div>
   <script>
       var div = document.getElementsByTagName('div')
       console.log(div[1].hasAttribute('id')); // false
   </script>
   ```

2. `.hasAttributes()` : 判断指定元素是否具有属性

   ```html
   <div class="x1" name="1" id="pink_box">1</div>
   <div class="x2" name="1">2</div>
   <div class="x3" name="2">3</div>
   <script>
       var div = document.getElementsByTagName('div')
       console.log(div[1].hasAttribute('id')); // false
       console.log(div[1].hasAttributes()); // true
   </script>
   ```

3. `.setAttribute(“属性名”, "属性值1 属性值2")` : 设置属性,属性名,值

   ```html
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
       <style>
           .red{
               color: pink;
               background-color: aquamarine;
               width: 200px;
               height: 200px;
           }
           .font{
               font-size: 22px;
               align-content: center;
           }
       </style>
   </head>
   <body>
   <script>
   <div class="box" id="item1">div1</div>
   <script type="text/javascript">
       var div = document.getElementById('item1');
       div.setAttribute("class", "red font");
   </script>
   </body>
   ```

4. `.getAttribute("属性名")` : 获取元素指定属性的值

   ```html
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
       <style>
           .red{
               color: pink;
               background-color: aquamarine;
               width: 200px;
               height: 200px;
           }
           .font{
               font-size: 22px;
               align-content: center;
           }
       </style>
   </head>
   <body>
   <script>
   <div class="box" id="item1">div1</div>
   <script type="text/javascript">
       var div = document.getElementById('item1');
       div.setAttribute("class", "red font");
       console.log(div.getAttribute("class")); // red font
   </script>
   </body>
   ```

5. `.removeAttribute("属性名")` : 删除元素的指定属性

   ```html
   <script>
   <div class="box" id="item1">div1</div>
   <script type="text/javascript">
       var div = document.getElementById('item1');
       div.setAttribute("class", "red font");
       console.log(div.getAttribute("class")); // null
   </script>
   ```

   

##### 1.5 文本操作

+ innerHTML : 设置和查看标签内容,包含 HTML 样式

+ innerText : 设置和查看标签内的纯文本内容

  ```html
  <div id="div_id"></div>
  <script type="text/javascript">
      var div = document.getElementById('div_id');
      div.innerHTML = "<p>这是添加的p标签</p><br>"; // 设置 div 内容
      div.innerText = "<p>这是添加文本添加的p标签</p>"; // 设置 div 的文本
      console.log(div.innerHTML); // &lt;p&gt;这是添加文本添加的p标签&lt;/p&gt;
      console.log(div.innerText); // <p>这是添加文本添加的p标签</p>
      div.innerText = ""; // 清除 div 内容
  </script>
  ```

  

##### 1.6 操作元素

1. 获取和添加元素

   | 方法                  | 说明                           |
   | --------------------- | ------------------------------ |
   | `.createElement("")`  | 创建对象,类型自己设置          |
   | `.createTextNode("")` | 创建文本节点,文本内容          |
   | `.cloneNode()`        | 克隆节点                       |
   | `.removeChild()`      | 删除节点                       |
   | `.appendchild()`      | 在指定标签的子元素尾部添加元素 |

2. 添加文本框

   ```html
   <div id="empty"></div>
   <script type="text/javascript">
       var empty_div = document.getElementById("empty");
       var p = document.createElement('p');
       var text = document.createTextNode("创建文本节点");
       p.appendChild(text); // 给 p 添加文本节点
       empty_div.appendChild(p); // 给 empty_div 添加 p 标签
   </script>
   ```

3. 添加 input 输入框

   ```html
   <div id="empty"></div>
   <script type="text/javascript">
       var empty_div = document.getElementById("empty");
       var input = document.createElement('input'); // 创建 input 对象
       var pas  = document.createElement('span');
       var text = document.createTextNode("密 码: ");
       pas.appendChild(text);
       input.setAttribute("type", "password");
       empty_div.appendChild(pas);
       empty_div.appendChild(input);
   </script>
   ```

4. 克隆

   ```html
   <div id="empty"></div>
   <div id="div_id"></div>
   <script type="text/javascript">
       var empty_div = document.getElementById("empty");
       var div_id = document.getElementById("div_id");
       var input = document.createElement('input'); // 创建 input 对象
       var pas  = document.createElement('span');
       var text = document.createTextNode("密 码: ");
       pas.appendChild(text);
       input.setAttribute("type", "password");
       empty_div.appendChild(pas);
       empty_div.appendChild(input);
       var new_div = empty_div.cloneNode(true); // 克隆 empty_div 内容存入 new_div
       div_id.appendChild(new_div); // 将new_div 作为子内容存入 div_id 内
   </script>
   ```

5. 删除节点

   ```html
   <div id="empty"></div>
   <div id="div_id"></div>
   <script type="text/javascript">
       var empty_div = document.getElementById("empty");
       var div_id = document.getElementById("div_id");
       var input = document.createElement('input'); // 创建 input 对象
       var pas  = document.createElement('span');
       var text = document.createTextNode("密 码: ");
       pas.appendChild(text);
       input.setAttribute("type", "password");
       empty_div.appendChild(pas);
       empty_div.appendChild(input);
       var new_div = empty_div.cloneNode(true);
       div_id.appendChild(new_div);
       console.log(empty_div.childNodes) // 0 : span ; 1 : input
       empty_div.removeChild(empty_div.childNodes[0]); // 删除 span 内容
       empty_div.removeChild(empty_div.childNodes[0]); // 删除 input 内容 ,删除 span 之后 input 变为 div 内 第一个内容 下标 0
   </script>
   ```

   

#### 2. 事件

+ Js 事件

  | Js 事件     | 事件说明                       |
  | ----------- | ------------------------------ |
  | onabort     | 图像加载被中断                 |
  | onblur      | 元素失去焦点                   |
  | onchange    | 域的内容被改变                 |
  | onclick     | 当用户单击某个对象是调用的事件 |
  | ondblclick  | 当用户双击某个对象是调用的事件 |
  | onerror     | 在加载文档或图像时发生错误     |
  | onfocus     | 元素获得焦点                   |
  | onkeydowm   | 某个键盘按键被按下             |
  | onkeypress  | 摸个键盘按键被按下并松开       |
  | onkeyup     | 某个键盘按键被松开             |
  | onload      | 一张页面或一幅图片完成加载     |
  | onmousedown | 鼠标按钮被按下                 |
  | onmousemove | 鼠标被移动                     |
  | onmouseout  | 鼠标从某元素移开               |
  | onmouseover | 鼠标移到某元素上               |
  | onmouseup   | 鼠标按键被松开                 |
  | onresize    | 重置按钮被点击                 |
  | onselect    | 文本被选中                     |
  | onsubmit    | 确认按钮被点击                 |
  | onunload    | 用户退出页面                   |

+ 调用事件时考虑该标签对象是否有此事件

+ 键盘对应数字编码 (常用)

  | 数字编码          | 代表按键  |
  | ----------------- | --------- |
  | `keycode 48-57`   | 0 - 9     |
  | `keycode 58-90`   | A - Z     |
  | `keycode 112-123` | F1 - F12  |
  | `keycode 8`       | Backspace |
  | `keycode 9`       | Tab       |
  | `keycode 13`      | Enter     |
  | `keycode 16`      | Shift     |
  | `keycode 18`      | Alt       |
  | `keycode 32`      | Space     |
  | `keycode 35`      | End       |
  | `keycode 36`      | Home      |
  | `keycode 37-40`   | ←↑→↓      |
  | `keycode 20`      | CapsLock  |

  

#### 3. 内置对象

##### 3.1 计时器

1. 定时器
   1. `setlnterval()` : 间隔指定的毫秒数不停的执行指定的代码

   2. `clearInterval` : 关闭反复执行的定时器

      ```html
      <head>
          <meta charset="UTF-8">
          <title>计时器</title>
          <style>
              .box{
                  width: 100px;
                  height: 100px;
                  background-color: red;
                  position: absolute;
              }
          </style>
      </head>
      <body>
          <button id="btn">停止</button>
          <div class="box" id="boxid">1</div>
          <script type="text/javascript">
              var box = document.getElementById('boxid');
              var interval = setInterval(
                  function () {
                      box.style.top = box.offsetTop + 10 + "px";
                  }, 1000 // 单位毫秒
              );
              var stop = document.getElementById('btn')
              stop.onclick = function () {
                  clearInterval(interval);
              }
          </script>
      </body>
      ```

2. 倒计时器 (倒数指定时间执行) 执行一次

   1. `setTimeout()` : 设置计数器

   2. `clearTimeout()` : 关闭计时器

      ```html
      <head>
          <meta charset="UTF-8">
          <title>计时器</title>
          <style>
              .box{
                  width: 100px;
                  height: 100px;
                  background-color: red;
                  position: absolute;
              }
          </style>
      </head>
      <body>
          <button id="btn">停止</button>
          <div class="box" id="boxid"></div>
          <script type="text/javascript">
              var box = document.getElementById('boxid');
              var timer = setTimeout(
                  function () {
                      box.innerHTML = "<p>3s倒数结束</p>"
                  }, 3000
              );
              var stop = document.getElementById("btn");
              stop.onclick = function () {
                  clearTimeout(timer);
              }
          </script>
      </body>
      ```

      

##### 3.2 时间

+ 时间对象在使用时需要使用 new 创建

  ```html
  <script type="text/javascript">
      var data = new Date(); // 创建时间对象
      console.log(data.getTime()); //时间戳,1970年0点到现在秒数
      console.log(data.getFullYear()); //年份
      console.log(data.getMonth()); // 月份
      console.log(data.getDate()); // 日
      console.log(data.getHours()); // 小时
      console.log(data.getMinutes()); // 分
      console.log(data.getSeconds()); // 秒
  </script>
  ```

  

##### 3.3 JS 数组

1. 创建数组

   ```html
   <script type="text/javascript">
       // 通过 array 对象 创建数组
       var array = new Array(1, 2, "a", "b");
       console.log(array); // Array(4) --> 0: 1  1: 2  2: "a"  3: "b"
       // 直接创建数组
       var arr2 = [1,2,3,4,5,"xxx"];
       console.log(arr2); // Array(6) --> 0: 1 1: 2 2: 3 3: 4 4: 5 5: "xxx"
   </script>
   ```

2. 数组的特点 : 可以存储其他类型元素 , 包括函数

   ```html
   <script type="text/javascript">
       var func = [
           function (a, b) {
               return a - b
           },
           function (a, b) {
               return a + b
           },
           function (a, b) {
               return a * b
           },
           function (a, b) {
               return a / b
           },
       ]
       console.log(func[0](15, 5)); // 10
       console.log(func[1](15, 5)); // 20
       console.log(func[2](15, 5)); // 75
       console.log(func[3](15, 5)); // 3
   </script>
   ```

3. 数组方法

   1. 添加数据

      1. `.push("")` : 在数组尾部添加元素

      2. `.unshift("")` : 在数组头部添加元素

         ```html
         <script type="text/javascript">
             var arr = [1, 2, 3, 4, 5];
             console.log(arr);
             arr.push(6, 7, "yyy");
             console.log(arr);
             arr.unshift(0, "xxx");
             console.log(arr); // 添加操作完成后才进行输出,所以三个输出完全相同 ["xxx", 0, 1, 2, 3, 4, 5, 6, 7, "yyy"]
         </script>
         ```

   2. 获取数据

      1. `数组名[下标]` : 索引获取
      2. `数组名.length` : 数组元素长度

   3. 删除和修改数据

      1. pop 删除并返回最后一个元素

         ```html
         <script type="text/javascript">
             var arr = [1, 2, 3, 4, 5];
             var arr1 = arr.pop();
             console.log(arr1); // [1,2,3,4]
             console.log(arr); // [1,2,3,4]
         </script>
         ```

      2. shift 删除并返回第一个元素

         ```html
         <script type="text/javascript">
             var arr = [1, 2, 3, 4, 5];
             // var arr1 = arr.pop();
             var arr1 = arr.shift();
             console.log(arr1); // [2, 3, 4, 5]
             console.log(arr); // [2, 3, 4, 5]
         </script>
         ```

      3. `splice(index, howmany, item1, ..., itemX)` : 删除从 index 处开始的零个或多个元素，并且用参数列表中声明的一个或多个值来替换那些被删除的元素

         1. index : 规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。

         2. howmany : 要删除的项目数量。如果设置为 0，则不会删除项目

         3. item1, ..., itemX : 向数组添加的新项目

            ```html
            <script type="text/javascript">
                var arr = [1, 2, 3, 4, 5];
                arr.splice(3, 0, "Hello")
                // arr.splice(0, 1)
                for (var i=0;i<arr.lenth;i++){
                    document.write(arr[i]) // 123Hello4
                    // document.write(arr[i]) // 2345
                }
            </script>
            ```

            

##### 3.4 JS 数学对象 Math

1. `Math.round()` : 四舍五入

2. `Math.max(arr)` 或 `Math.min(arr)` : 最大值和最小值

3. `Math.floor()` 或 `Math.ceil()` : 向下取整、向上取整

4. `Math.random()` : 0-1 之间随机小数(16位小数) `Math.floor(Math.random()*10)` : 0-9 随机小数

   ```html
   <script type="text/javascript">
       var result = [Math.random(), Math.random(), Math.random(), Math.random(), Math.random()]
       for (var i=0;i<result.length;i++) {
           result[i] = Math.floor(result[i]*10)
           document.write(result[i]) // 29518
       }
   </script>
   ```

   

#### 4. JS 正则

+ 声明方式

  1. new RegExp() : 如果有转义字符必需两次转义
  2. /hehe/ : 直接定义 (推荐使用)

+ 转义字符

  | 转义字符 | 使用            | 含义                   |
  | -------- | --------------- | ---------------------- |
  | \w       | var reg = /\w/; | 单个的字母数字下划线   |
  | \W       | var reg = /\W/; | 单个的非字母数字下划线 |
  | \d       | var reg = /\d/; | 单个数字字符           |
  | \D       | var reg = /\D/; | 单个非数字字符         |
  | \s       | var reg = /\s/; | 单个空白字符,例如空格  |
  | \S       | var reg = /\S/; | 单个的非空白字符       |

+ 元字符

  | 转义字符 | 使用                                     | 含义                                |
  | -------- | ---------------------------------------- | ----------------------------------- |
  | .        | var reg = /./;                           | 除了换行以外其他任意字符            |
  | *        | var reg = /z*/;                          | 匹配 0 次或多次                     |
  | +        | var reg = /z+/;                          | 匹配至少 1 次或多次                 |
  | ？       | var reg = /\w+?/;                        | 禁止贪婪                            |
  | {}       | var reg = /{5}/;<br>var reg = /{5, 12}/; | 限制匹配的次数<br>限制匹配5 - 12 次 |
  | []       | var reg = /[a-zA-Z0-9]+/;                | 字符范围                            |
  | ()       | var reg = /\d(\w+)\w+/;                  | 子组,可以有可以没有                 |
  | \|       | var reg = /abc\|def\|123/;               | 或                                  |
  | ^        | var reg = /^\d/;                         | 限制开始                            |
  | $        | var reg = /a$/;                          | 限制结尾                            |

  ```html
  <script type="text/javascript">
      var str = "hello"
      var reg = /\w/;
      var res1 = reg.test(str);
      var res2 = reg.exec(str);
      document.write(res1 + "<br>"); // 判断匹配是否正确 true
      document.write(res2); //返回匹配到的元素 h
  </script>
  ```

  

