### CSS

#### CSS 简介

+ CSS 值层叠样式表 (Cascading Style Sheets)

  + 将 HTML 结构和样式分开
  + 布局和美化网页,并定义如何显示 HTML 页面

+ 语法格式

  ```
  选择器 : {key:value; key;value}
  h1	  : {color:blue; font-size:12px}
  ```

#### CSS 的使用方式

##### 嵌入式

+ 在 `<head></head>` 标签内添加一个 style 标签,把样式写在 `<style></style>` 标签之间, 把样式嵌入到 HTML 文档内

##### 外链式

+ 在 `<head></head>` 标签内添加一个 `<link rel="styleshee" href="">` 标签,通过 link 的 href 属性引入外部的 .css 文件,将样式写在 .css 内,语法和嵌入式相同

##### 行间样式

+ 给标签添加 style 属性, 在 style 属性内部写样式

  ```html
  <div style="width: 200px; height: 200px; background-color: red"></div>
  ```

##### 使用情况

1. 行内 CSS 通常用于单独的小的样式修改
2. 嵌入 CSS 通常用于单个文件的教学或独立的案例
3. 外链 CSS 通常用于复杂方式
4. 引入优先级为就近原则

#### CSS 选择器 

+ 在为指定元素设置样式时通过选择器定位元素
+ 几乎所有标签都具有 style, title, id, class 元素

##### 通配符选择器

+ \* : 所有的元素

##### 基本选择器

1. 标签选择器
   + 通过标签名直接定位元素,获取页面中所有符合选择器条件的元素,大范围影响
2. id 选择器
   + 通过元素 **id** 值定位元素,一个 id 值对应一个标签，且不会重复,一次只设置一个元素样式,影响范围最小
   + 选择符 : `#id值`
3. 类选择器 (class 选择器)
   + 通过元素 **class** 属性的值定位元素,一个元素可以设置多个 class 值,一个 class 值可以被多次使用(使用最灵活,使用最多),id 选择器 < 影响范围 < 标签选择器
   + 选择符 : `.class值`

##### 属性选择器

+ 根据元素的属性来获取元素

  + 找到拥有 data 属性并且值为 item1 的 div 元素

    ```css
    div[data="item1"]
    ```

  + 找到拥有 data 属性并且值以 i 开头的 div 元素

    ```css
    div[data^="i"]
    ```

  + 找到拥有 data 属性并且值以 1 结尾的 div 元素

    ```css
    div[data$="1"]
    ```

  + 找到拥有 data 属性并且值包含 item1 的 div 元素

    ```css
    div[data~="item1"]
    ```

##### 关系选择器

1. 后代 (包含选择器)

   + 格式 : `E F{}` // 选择所有被 E 包含的 F 元素

   + 选择符 : 空格

     ```html
     <head>
         <meta charset="UTF-8">
         <title>Day_27</title>
         <style>
             .wrap p{
                 color: red;
             }
         </style>
     </head>
     <body>
     <div class="wrap">
         <p>
             你好
         </p>
         <div>
             <p>
                 你好
             </p>
         </div>
     </div>
     ```

2. 子元素选择器

   + 格式 : `E>F{}` // 选择 E 元素的子元素 F

   + 选择符 : >

     ```html
     <head>
         <meta charset="UTF-8">
         <title>Day_27</title>
         <style>
             .wrap>p{
                 color: red;
             }
         </style>
     </head>
     <body>
     <div class="wrap">
         <p>
             你好
         </p>
         <div>
             <p>
                 你好
             </p>
         </div>
     </div>
     ```

3.  并列选择器

   + 格式 : `E,F{}` // 同时给 EF 元素设置样式

   + 选择符 : ,

     ```html
     <head>
         <meta charset="UTF-8">
         <title>Day_27</title>
         <style>
             .box1,.box2{
                 width: 100px;
             }
             .box1{
                 background-color: red;
             }
         </style>
     </head>
     <body>
     <div class="box1"></div>
     <div class="box2"></div>
     </body>
     ```

##### 伪类和伪元素选择器

1. 伪类选择器
   
   + 选择器 : `:hover{}` //当鼠标悬浮在指定元素上时,加载指定 CSS 样式
   
2. 伪元素

   + 选择器: `:target{}` //找到目标元素并显示

   + 选择器 : `:after{}` // 设置在对象后 (依据对象树的逻辑结构) 发生的内容.用来和 content 属性一起使用
   + 选择器 : `:before{}` // 设置在对象前 (依据对象树的逻辑结构) 发生的内容.用来和 content 属性一起使用

##### 选择器优先级

+ 每个选择器都有对应的数值,使用选择器渲染时,数值大的优先级最高

  |    选择器    | 优先级 |
  | :----------: | :----: |
  |   行间样式   |  1000  |
  |  id 选择器   |  0100  |
  | class 选择器 |  0010  |
  |  标签选择器  |  0001  |

+ 如果为关系型选择器,将所有选择器的对应值相加值大的优先级高,值相等的按照就近原则

#### CSS 常用属性

##### CSS 的颜色表示方式

1. 单词表示
   + 常见颜色 : red (红)、green (绿)、blue (蓝)、blank (黑)、pink (粉)
2. 十六进制
   + 格式 : `#000000`
   + 以 # 开头的六位十六进制组成,每两位代表一种颜色
3. 十进制数字表示
   + 格式 : `rgb(0, 0, 0)`
   + 由三位数字组成,三原色,第一位红,第二位绿,第三位蓝
   + 取值范围 : 0-255
4. 透明度
   + 格式 : `rgb(0, 0, 0, 0.5)`
   + 最后一位 a 是 alpha, 透明度 0-1 , 0 完全透明, 1 不透明

##### 常用 CSS 样式属性

1. 背景属性

   |        属性         |                             使用                             |       说明       |
   | :-----------------: | :----------------------------------------------------------: | :--------------: |
   |  background-color   |                    background-color: red                     |     背景颜色     |
   |  background-image   |                 background-image: url(path)                  |     背景图片     |
   | background-position | left : 左 &emsp;center : 中&emsp;right : 右<br/>top : 上&emsp; bottom : 下 |   背景图片位置   |
   |  background-repeat  | no-repeat : 不重复&emsp;repeat-x : 水平重复&emsp;repeat-y : 垂直重复 | 背景图片是否平铺 |
   |   background-size   |                  background-size: 100% 100%                  |   背景图片大小   |

   + 简写

     ```css
     background: bg_color 	url() 	repeat-y scroll 	50% 0
     			背景颜色  背景图片地址  背景平铺	 背景滚动   背景位置
     ```

2. 字体属性

   |    属性     |                             说明                             |
   | :---------: | :----------------------------------------------------------: |
   |    color    |                           字体颜色                           |
   |  font-size  |                           字体大小                           |
   | font-weight | 字体粗细 :<br>&emsp;1. Normal : 正常粗细<br>&emsp;2. Bold : 加粗<br>&emsp;3. Bolder : 更粗<br>&emsp;4. lighter : 更细<br>&emsp;5. 自定义粗细 : 100-900 |
   | font-family |                           字体类型                           |
   | font-style  | 字体样式<br/>&emsp;1. normal : 正常<br/>&emsp;2. italic : 斜体 |

3. 文本属性

   |          属性          |                 说明                 |
   | :--------------------: | :----------------------------------: |
   |      text-indent       |             设置首行缩进             |
   |       text-align       | 设置文本对齐方式,left、center、right |
   |      line-height       |    行高,一般用于单行文本垂直居中     |
   | vertical-align: middle |             垂直对齐方式             |
   |    text-decoration     |           none; 去除下划线           |

4. 边框属性

   |               属性               |                             说明                             |
   | :------------------------------: | :----------------------------------------------------------: |
   |           border-style           | 边框样式:<br>&emsp;1. solid : 实线<br/>&emsp;2. dotted : 点状线<br/>&emsp;3. dashed : 虚线 |
   |           border-color           |                           边框颜色                           |
   |           border-width           |                           边框粗细                           |
   |           border 连写            |      `border : border-width border-style border-color`       |
   |            border-top            |                           顶部边框                           |
   |          border-bottom           |                           底部边框                           |
   |           border-left            |                           左侧边框                           |
   |           border-right           |                           右侧边框                           |
   | CSS 新增属性: <br/>border-radius | 圆角边框<br/>1. 如果四个值: 左上、右上、左下、右下<br/>2. 三个值 : 左上、右上左下对角、右下<br/>3. 两个值 : 左上右下、左下右上<br/>4.一个值 : 四个角 |

   

