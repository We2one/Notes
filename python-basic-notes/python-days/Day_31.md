### jQuery 入门

#### 1.jQuery 简介

+ jQuery 是一个免费、开源的 JavaScript 库,也是目前使用最广泛的 JavaScript 函数库

+ 方便完成页面前端相关操作 : 节点操作、元素操作、事件绑定、AJAX 操作、解决兼容问题

+ jQuery 是一个 JS 文件、一个函数库,在页面 script 标签使用 src 引入这个 js 文件就可以使用

  1. CDN 加载 jQuery 库

     ```
     <script src="https://cdn.staticfile.org/jquery/2.2.4/jquery.min.js"></script>
     或
     <script src="https://apps.bdimg.com/libs/jquery/2.2.4/jquery.min.js"></script>
     或
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
     或
     <script src="http://lib.sinaapp.com/js/jquery/2.2.4/jquery-2.2.4.min.js"></script>
     ```

  2. 本地下载加载 jQuery 库

     ```
     npm install jquery
     <script src="../node_modules/jquery/dist/jquery.min.js"></script>
     ```

#### 2.jQuery 选择器

+ jQuery 选择器 通过 .css 方法获取 HTML 标签,修改样式

+ 常见选择器

  | 描述               | 案例                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | id 选择器          | `$("#div").css("background", "red").css("width", 100)...;`   |
  | 类 选择器          | `$(".div").css("background", "red").css("width", 100)...;`   |
  | 标签选择器         | `$("div").css("background", "red").css("width", 100)...;`    |
  | 属性选择器         | `$("[name]").css("background", "red").css("width", 100)...;`<br/>`$("[name = 'nice']").css("background", "red").css("width", 100)...;`<br/>`$("[name != 'nice']").css("background", "red").css("width", 100)...;` |
  | 后代选择器         | `$("#div p").css("background", "red").css("width", 100)...;` |
  | 子 选择器          | `$("#div>p").css("background", "red").css("width", 100)...;` |
  | 并列选择器         | `$("#div,.div").css("background", "red").css("width", 100)...;` |
  | first last         | `$("div:first").css("background", "red").css("width", 100)...;`<br/>`$("div:last").css("background", "red").css("width", 100)...;` |
  | eq通过索引获取元素 | `$("div:eq(2)").css("background", "red").css("width", 100)...;` |

#### 3.jQuery 元素操作

##### 3.1 jQuery 通过关系获取元素

​	

| 描述                     | 案例                                   |
| ------------------------ | -------------------------------------- |
| 获取子元素               | `var children = $("#div").children();` |
| 获取上一个兄弟元素       | `var prev = $("#div").prev();`         |
| 获取下一个兄弟元素       | `var next = $("#div").next();`         |
| 获取同级除了自己所有元素 | `var siblings = $("#div").siblings();` |
| 获取父元素               | `var parent = $("#div").parent();`     |
| 获取先祖元素             | `var parents = $("#div").parents();`   |

##### 3.2 jQuery 样式操作

1. `.css()` : 取出或设置 CSS 样式 

   1. CSS 如果只指出属性,没有给出值,可以获取对应属性的值

      ```
      var width = $("#box").css("width")
      ```

      

   2. CSS 方法如果只指出属性,给值,就修改样式

      ```
      $("#box").css("width", 100)
      ```

      

   3. CSS 方法也可以修改多个样式 

      ```
      $("#box").css({"width": "100px",
          "height": "100px",
          "background-color": "red",
          "border": "1px solid black"
      })
      ```

2. `.addClass()`,`.removeClass()`,`.toggleClass()` : 通过添加和减去class 属性值来修改样式

   1. 添加样式

      ```
      $("#box").addClass("div div1");
      ```

   2. 删除样式

      ```
      $("#box").removeClass("div1");
      ```

   3. 如果有效果就移除,如果没有就加上

      ```
      $("#box").toggleClass("div div1");
      ```

##### 3.3 jQuery 属性操作

1. `.attr()` : 取出或设置某个属性的值

   1. 取出属性值

      ```
      $("#box").attr("class");
      ```

   2. 设定属性值

      ```
      $("#box").css("class", "div div1");
      ```

   3. 直接指出多个属性和属性值

      ```
      $("#box").attr({
      	"class": "div div1",
      	"nice": "nice work"
      })
      ```

      

2. `removeattr()` : 删除属性

   ```
   $("#box").removeattr("nice");
   ```

##### 3.4 文本操作

1. `.html()` : 取出或设置 HTML 元素内容

   ```
   // 获取 HTML 内容
   var html = $("#box").html()
   // 设置 HTML 内容
   $("#box").html(
   	"<h1>你好</h1>"
   )
   ```

   

2. `.text()` : 取出或设置 TEXT 文本内容

   ```
   // 获取 Text 内容
   var text = $("#box").text()
   // 设置 Text 内容
   $("#box").html(
   	"<h1>你好</h1>"
   )
   ```

3. `.val()` : input 输入的内容获取和设置都用 val

   ```
   $("#input").val("hello")
   ```

#### 4.相关尺寸

1. 取出或设置被选元素的宽高

   ```
   var width = $("#box").width();
   var height = $("#box").height();
   ```

   

2. 取出或设置被选元素相对于文档的偏移坐标

   ```
   var offset = $("#box").offset();
   // 偏移坐标 offset
   // 向上部偏移 offset.top
   // 左部偏移 offset.left
   ```

#### 5.动画效果

##### 5.1 显示和隐藏

1. `.hide()`,`.show()`,`.toggle()` : 设置显示和隐藏

   ```js
   <div id="box"></div>
   <button id="btn">点击</button>
   <script type="text/javascript">
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
           .hide(1000)
           .show(1000)
       ;
       $("#btn").click(
           function () {
               $("#box").toggle(); // 如果显示就隐藏,如果隐藏就显示
           }
       )
   </script>
   ```

2. jQuery 动画函数普遍接收一个 fast(块),slow(慢),normal(正常)作为对动画快慢的描述,也可以用数字描述

   ```js
   $("#box")
           .width("slow")
           .height("fast")
   ```

3. `.fadeln()`,`.fadeOut()`,`fadeToggle()` : 设置元素淡入淡出

   ```js
   <div id="box"></div>
   <button id="btn">点击</button>
   <script type="text/javascript">
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
           .slideUp(10000) // 如果现在是展开状态,向上滑动
           .slideDown(10000) // 如果现在是折叠状态,向下滑动
       ;
       $("#btn").click(
           function () {
               $("#box").slideToggle(1000); // 如果折叠就展开,如果展开就折叠
           }
       )
   </script>
   ```

##### 5.2 自定义动画

1. `.animate()` : 方法设置自定义动画

   + 语法 : `$(selector).animate(styles, speed, easing, callback)`

   + 参数

     | 参数     | 描述                                                         |
     | -------- | ------------------------------------------------------------ |
     | styles   | 必需。规定产生动画效果的 CSS 样式和值。                      |
     | speed    | 可选。规定动画的速度。默认是 "normal"，"fast","slow"         |
     | easing   | 可选。规定在不同的动画点中设置动画速度的 easing 函数。内置的 easing 函数: swing 和 linear |
     | callback | 可选。animate 函数执行完之后,要执行的函数                    |

2. `.ready()` : 开始动画

   ```js
   <div id="box"></div>
   <button id="btn">点击</button>
   <script type="text/javascript">
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
       $(document).ready(
           function () {
               $("#btn").click(
                   function () {
                       $("#box").animate({"height": "300px"});
                   }
               )
           }
       )
   </script>
   ```

   

3. `.stop()` : 停止动画

   ```js
   <div id="box"></div>
   <button id="btn">点击</button>
   <script type="text/javascript">
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
           .hide(10000)
           .show(100)
       $("#btn").click(
           function () {
               // $("#box").stop(); // 停止当前动画进入下一次动画
               $("#box").stop(true); // 停止所有动画
           }
       )
   </script>
   ```

   

4. `.delay()` : 延迟动画

   ```js
   <div id="box"></div>
   <button id="btn">点击</button>
   <script type="text/javascript">
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
           .delay(1000).animate({"height": "300px"})
       $("#btn").click(
           function () {
               $("#box").delay(1000).animate({"width": "300px"});
           }
       )
   </script>
   ```

#### 6.关于事件

+ 事件改动

  + 事件的名称由 on 事件变成了 事件名称

  + 事件调用由 "=" 变成了 参数 "()"

  + jQuery 所有事件和 JS 一样需要用函数描述

  + JS 事件执行函数

    ```js
    var div = document.getElementById("box");
    div.onclick = function() {}
    ```

  + jQuery 事件执行函数

    ```js
    var div = $("#box");
    div.click(function() {})
    ```

+ jQuery 常用事件

  | 事件    | 描述         |
  | ------- | ------------ |
  | blur    | 表单失去焦点 |
  | focus   | 表单获取焦点 |
  | submit  | 表单提交     |
  | change  | 表单发生修改 |
  | keydown | 键盘按下     |
  | keyup   | 键盘弹起     |

+ 鼠标常用事件

  | 事件      | 描述               |
  | --------- | ------------------ |
  | click     | 鼠标单击事件       |
  | mouseover | 鼠标移动到对象上面 |
  | mousemove | 鼠标移动           |
  | mouseout  | 鼠标移除           |
  | mousedown | 鼠标按下           |
  | mouseup   | 鼠标弹起           |

#### 7.jQuery 节点操作

##### 7.1 创建节点

+ 代码

  ```
  var $div = $('<div>');
  var $div2 = $('<div>div元素</div>');
  ```

##### 7.2 插入节点

1. `.append()` : 在现存元素内部,从后面插入元素

   ```js
   <div id="box"></div>
   <script>
       var $span = $("<span>span标签</span>")
       $("#box")
           .width("100px")
           .height("100px")
           .css({"background-color": "red", "border": "1px solid black"})
           .append($span);
   </script>
   ```

2. `.prepend()` : 在现存元素内部,从前面插入元素

3. `.after()` : 在现存元素外部,从后面插入元素

4. `.before()` : 在现存元素外部,从前面插入元素

##### 7.3 删除节点

1. `$(element).remove()` : 删除当前元素
2. `$(element).clear()` : 清空当前元素

##### 7.4 克隆节点

+ `$(element).clone(true)` : 克隆节点



