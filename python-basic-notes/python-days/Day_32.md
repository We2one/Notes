### Bootstrap

+ Bootstrap : 一个成熟的 Web 前端框架,涵盖了页面开发的大部分 CSS 布局、JS 特效
+ 常规开发 : 先编写 HTML , 然后编写 HTML 样式 CSS , 接着编写 HTML 功能 JS
+ Bootstrap 开发 : 先定义好样式特效 , 如果需要可以直接通过 class 和其他属性调用
+ 本文中代码系 Bootstrap 3.3.7

#### 1.Bootstrap 安装

##### 1.1 CDN 加速加载 Bootstrap

```html
<!-- CSS only -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

<!-- JQuery 加载 -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<!-- popper.js 加载 -->
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<!-- JS 加载 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
<!--3.3-->
<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
```

##### 1.2 本地加载 Bootstrap最新版

1. 下载 Bootstrap

   + Bootstrap 的 `package.json` 文件包含了一些额外的元数据：
     1. `less` - Bootstrap 源码的入口文件的路径
     2. `style` - Bootstrap 的未压缩 CSS 文件的路径

   ```
   // 下载 Bootstrap最新版
   npm install bootstrap
   // 下载 Bootstrap旧版 @版本号
   npm install bootstrap@3
   ```

2. 加载 Bootstrap (jQuery 加载必须在 bootstrap 之前)

   ```html
   <!-- JQuery	 加载 -->
   <script type="text/javascript" src="../node_modules/jquery/dist/jquery.min.js"></script>
   <!-- JS 加载 -->
   <script type="text/javascript" src="../node_modules/bootstrap/dist/js/bootstrap.min.js"></script>
   <!-- CSS 加载 -->
   <link type="text/css" rel="stylesheet" href="../node_modules/bootstrap/dist/css/bootstrap.min.css">
   <!-- bootstrap 4.5 不兼容3.x的 3.4 不兼容3.3的 3.3 又不兼容2.x的 -->
   ```

#### 2.栅格系统

+ 栅格系统是 Bootstrap 推出的一种快速页面布局方案 --> 将真个页面的宽度分为 12 份,只需要设置每份之间的间距即可

+ 栅格系统可以快速的进行布局

  1. 栅格系统必须在 **class** 值为 **container** 或者 **container-fluid** 下,如果不在这两个页面下,不生效.
     1. `class="container"` : 固定宽度,如果浏览器比其宽就居中显示
     2. `class="container-fluid"` : 100% 宽度
  2. 栅格系统一行被分为 12 份,如果所有元素没有占满 12 份 也可以布局,如果超出,超出部分另起一行布局
  3. 栅格系统是用 row 进行垂直划分
  4. Bootstrap 可以适应大部分终端 的布局方式

+ 代码

  ```html
  <div class="container">
      <div class="row">
          <div class="col-md-1">
              (1,1)
              <!-- // 第一行第一列 -->
          </div>
          <div class="col-md-1">
              (1,2) 
              <!-- // 第一行第二列 -->
          </div>
          <div class="col-md-1">
              (1,3)
              <!-- // 第一行第三列 -->
          </div>
          <div class="col-md-1">
              (1,4) 
              <!-- // 第一行第四列 -->
          </div>
      </div>
      <div class="row">
          <div class="col-md-1">
              (2,1)
              <!-- // 第二行第一列 -->
          </div>
          <div class="col-md-1">
              (2,2)
              <!-- // 第二行第二列 -->
          </div>
          <div class="col-md-1">
              (2,3)
              <!-- // 第二行第三列 -->
          </div>
          <div class="col-md-1">
              (2,4)
              <!-- // 第二行第四列 -->
          </div>
      </div>
  </div>
  ```

  

#### 3.导航

```html
<!--导航-->
<div class="container-fluid">
    <div class="row">
        <!--navbar: 导航 navbar-default: bootstrap 默认导航样式-->
        <nav class="navbar navbar-default">
            <!--强调导航是百分比还是固定宽度-->
            <div class="container-fluid">
                <div>
                    <!--navbar-brand 导航的标识部分,通常写在左边-->
                    <a class="navbar-brand" href="#">中共优就业电商</a>
                </div>
                <div>
                    <!--nav 当前 ul 是一个导航选项(去除li前面的点) navbar-nav 保持在一行 navbar-right 右边布局-->
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">登录</a></li>
                        <li><a href="#">退出</a></li>
                        <li><a href="#">2020-09-22</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</div>
```



#### 4.标签页

```html
<div class="container-fluid">
    <div class="row">
        <ul class="nav nav-tabs col-md-8 pull-right">
            <li class="active"><a href="#">个人信息&emsp;</a></li>
            <li><a href="#">订单管理&emsp;</a></li>
            <li><a href="#">地址管理&emsp;</a></li>
        </ul>
    </div>
</div>
```



#### 5.面板

##### 5.1 面板格式

```html
<div class="panel panel-default">
    <div class="panel-heading">
        个人日程管理
    </div>
    <div class="panel-body">
        <div>Python基础</div>
        <div>Web 框架</div>
        <div>爬虫学习</div>
        <div>人工智能</div>
    </div>
</div>
```



##### 5.2 面板的样式

```html
<div class="container-fluid">
    <div class="row">
        <div class="col-md-4">
            <div class="panel panel-default">
                <div class="panel-heading">
                    个人日程管理
                </div>
                <div class="panel-body">
                    <div>Python基础</div>
                    <div>Web 框架</div>
                    <div>爬虫学习</div>
                    <div>人工智能</div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4">
            <div class="panel panel-danger">
                <div class="panel-heading">
                    个人日程管理
                </div>
                <div class="panel-body">
                    <div>Python基础</div>
                    <div>Web 框架</div>
                    <div>爬虫学习</div>
                    <div>人工智能</div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4">
            <div class="panel panel-info">
                <div class="panel-heading">
                    个人日程管理
                </div>
                <div class="panel-body">
                    <div>Python基础</div>
                    <div>Web 框架</div>
                    <div>爬虫学习</div>
                    <div>人工智能</div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    个人日程管理
                </div>
                <div class="panel-body">
                    <div>Python基础</div>
                    <div>Web 框架</div>
                    <div>爬虫学习</div>
                    <div>人工智能</div>
                </div>
            </div>
        </div>
    </div>
</div>
```



#### 6.表单

+ 账号密码样式表单

  ```html
  <!--表单-->
  <!--每一组在一行中-->
  <form action="" class="form-horizontal">
      <!--组成一组-->
      <div class="form-group">
          <!--使用col-*变成一行-->
          <!--control-label 让文字和文本框居中对齐-->
          <label for="username" class="col-sm-1 control-label">用户名</label>
          <div class="col-sm-6">
              <input type="text" id="username" class="form-control" placeholder="用户名">
          </div>
      </div>
      <div class="form-group">
          <label for="pwd" class="col-sm-1 control-label">密码</label>
          <div class="col-sm-6">
              <input type="text" id="pwd" class="form-control" placeholder="密码">
          </div>
      </div>
  </form>
  ```

  

+ 搜索框样式的表单

  ```html
  <form action="" class="form-horizontal">
      <div class="input-group">
          <input type="text" class="form-control" aria-describedby="hello">
          <span class="input-group-addon" id="hello">@</span>
          <input type="text" class="form-control" aria-describedby="hello">
      </div>
      <br>
      <div class="input-group">
          <input type="text" class="form-control" aria-describedby="hello">
          <span class="input-group-addon" id="hi">
              <button class="btn btn-primary">
                  百度一下
              </button>
          </span>
      </div>
  </form>
  ```

  

#### 7.表格

+ 常规表格

  ```html
  <table class="table table-bordered table-hover col-md-8">
      <tr>
          <td>序号</td>
          <td>年龄</td>
          <td>姓名</td>
      </tr>
      <tr>
          <td>01</td>
          <td>12</td>
          <td>ash</td>
      </tr>
      <tr>
          <td>02</td>
          <td>20</td>
          <td>zofia</td>
      </tr>
  </table>
  ```

+ 其他表格

  ```html
  <table class="table table-bordered table-hover col-md-8">
      <caption>统计表</caption>
      <thead>
      <!--表头，表字段-->
          <tr>表头</tr>
      </thead>
      <tbody>
          <tr>表内容</tr>
      </tbody>
      <tfoot>
          <tr>表尾</tr>
      </tfoot>
  </table>
  ```

+ .class 样式

  | CSS样式                                               | 描述         |
  | ----------------------------------------------------- | ------------ |
  | `.table-bordered`                                     | 显示表格边框 |
  | `.table-hover`                                        | 鼠标经过效果 |
  | `.table-striped`                                      | 奇数行有背景 |
  | `.active`, `.success`, `.warning`, `.danger`, `.info` | tr背景颜色   |

  

#### 8.列表

```html
<div class="container">
    <ul class="list-group">
        <li class="list-group-item active">蔬菜</li>
        <!-- active 是一种样式 (蓝色背景) -->
        <li class="list-group-item">水果</li>
        <li class="list-group-item">海鲜</li>
        <li class="list-group-item">生鲜</li>
    </ul>
</div>
```



#### 9.分页

```html
<div class="container">
    <nav>
        <ul class="pagination">
        <!-- 使用 样式 -->
            <li><a href="">1</a></li>
            <li><a href="">2</a></li>
            <li><a href="">3</a></li>
            <li><a href="">下一页</a></li>
        </ul>
    </nav>
</div>
```



#### 10.缩略图

```html
<div class="row">
    <div class="col-md-4">
        <a href="#" class="thumbnail">
            <img src="../Day_30/face1.jpg" alt="">
        </a>
    </div>
</div>
```



#### 11.模态框

+ 当触发一个事件,弹出一个对话框,此时下面页面不可被操作

  ```html
  <button class="btn btn-default" data-target="#myModal" data-toggle="modal">激活模态框</button>
  <div class="modal" id="myModal">
  <!--包裹模态框-->
      <div class="modal-dialog">
      <!--模态框-->
          <div class="modal-content">
          <!--模态框内容部分-->
              <div class="modal-header">
              <!--头部-->
                  <h4>删除用户</h4>
              </div>
              <div class="modal-body">
              <!--身体-->
                  确定删除?
              </div>
              <div class="modal-footer">
              <!--脚部、尾部-->
                  <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                  <button type="button" class="btn btn-danger" data-dismiss="modal">确定删除</button>
              </div>
          </div>
      </div>
  </div>
  ```

  

#### 12.轮播图

+ 导入轮播图使用的 Bootstrap 的 CSS 和 JS 目录下要有 Bootstrap 的 fonts，需要左右箭头图片

  ```html
  <!--轮播图-->
  <div class="container">
      <!--轮播全局-->
      <div id="hiworld" class="carousel slide" data-ride="carouse">
          <!--小点部分
              几张图几个小点, data-toggle 和全局 id 要对应 class="active" 是首先被选中的小点
          -->
          <ol class="carousel-indicators">
              <li data-target="#hiworld" data-slide-to="0" class="active"></li>
              <li data-target="#hiworld" data-slide-to="1"></li>
              <li data-target="#hiworld" data-slide-to="2"></li>
              <li data-target="#hiworld" data-slide-to="3"></li>
          </ol>
          <!--图片部分-->
          <div class="carousel-inner" role="listbox">
              <div class="item active">
                  <img src="../Day_28/pictures/1.png" alt="" width="100%">
              </div>
              <div class="item">
                  <img src="../Day_28/pictures/2.png" alt="" width="100%">
              </div>
              <div class="item">
                  <img src="../Day_28/pictures/3.png" alt="" width="100%">
              </div>
              <div class="item">
                  <img src="../Day_28/pictures/4.png" alt="" width="100%">
              </div>
          </div>
          <!--控制部分-->
          <a class="left carousel-control" href="#hiworld" role="button" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
          </a>
          <a class="left carousel-control" href="#hiworld" role="button" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
          </a>
      </div>
      <div class="row">
          <span class="glyphicon glyphicon-user"></span>
          <span class="glyphicon glyphicon-user"></span>
      </div>
  </div>
  ```

  

#### 13.SVG 图像



