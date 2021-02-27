### 动态 HTML 处理

#### 爬虫与反爬虫

+ 爬虫的建议
  1. 尽量减少请求次数,能抓列表页就不抓详情页,减轻服务器压力,不要只看 Web 网站,还有手机 App 和 H5, 反爬措施会少一点
  2. 对性能要求比较高的时候,需要考虑多线程、分布式
+ **反爬策略**
  1. 通过**user-agent来判断**是否是爬虫.
     + 解决办法：
       1. **封装user-agent**。
       2. **准备user-agent池**
  2.  **封ip**：是网站针对爬虫最终策略。
     + 解决办法：使用**代理ip**---代理池项目
  3. 通过**请求的频率**来限制爬取。
     + 解决办法：
       1. 设置**请求头频率**限。time.sleep(0.1-0.9)
       2. **减少请求次数**：能在列表页获取，就不再详情页。但是要记得保存详情页url。能一次获取，就不多次获取。（ajax请求。limit:50）	   
  4. **验证码**：**破解验证码**
  5. 数据不是直接渲染到html页面中，而是通过**js异步获取数据**。
     + 解决办法：
       1. 使用**内置浏览器引擎**的爬虫（selenium+chrome/phantomjs）

#### Ajax 数据获取

##### Ajax 介绍

+ Ajax 技术 : 表单提交后,从服务器获取信息之后,网站的页面不需要重新刷新
+ Ajax 不是一门语言,是用来完成网络任务 的一系列技术.Ajax 全称 (Asynchronous JavaScript and XML : 异步 JavaScript 和 XML), 网站不需要使用单独的页面请求就可以和网络服务器进行交互 (收发信息)
+ Ajax 是一种客户端技术, 当浏览器通过一些 JavaScript 动作 (页面滑动、点击按钮等),此时 Ajax 引擎发送 HTTP 请求,服务器返回数据给 Ajax 引擎,最后 Ajax 引擎将服务器返回的数据渲染到浏览器当前的页面中,不需要对整个页面进行刷新就能加载数据
+ 爬取 Ajax 请求数据时,可以直接获取 HTTP 请求接口,从此接口获取数据,大大提升爬虫爬取效率

##### Ajax请求分析

+ Ajax 请求 位于浏览器 开发者模式中 Network 的 XHR (XmlHttpRequest) 对象中
+ Ajax 请求分析步骤
  1. **分析请求** : 找到页面中的 Ajax 请求 对于网页`F12 --> NetWork --> XML --> 查看发送与响应`
  2. **分析响应** : 找到 Ajax 请求并确认具体哪条获得页面数据的 Ajax 请求
     + 对于Ajax 请求,点开具体链接,分析该请求的详细信息,**response**、**preview**
     + 如果响应内容中包含页面数据,那么该请求就是需要获取请求
  3. **解析响应内容** : 一般 Ajax 请求都是 JSON 数据,解析 JSON 数据即可

#### Selenium 数据获取

##### Selenium 简介

+ Selenium : **Web 自动化测试工具**,可以按照指定的命令自动操作,Selenium 可以直接运行在浏览器上,支持所有主流浏览器 (包括 PhantomJS 等无界面浏览器)

+ Selenium 可以根据我们的指令,让浏览器自动加载界面,获取需要的数据,网页截屏,判断网站发生的动作

+ Selenium不自带浏览器,需要与第三方浏览器结合才可使用,使用方法

  1. 使用 PhantomJS 工具代替真实浏览器

  2. 下载火狐浏览器的 `geckodriver` [下载链接](https://github.com/mozilla/geckodriver/releases) 或 谷歌浏览器的 `chromedriver` (与浏览器版本对应， chromedriver 下载链接构造 **https://chromedriver.storage.googleapis.com/index.html?path=谷歌浏览器版本/**)

     1. 火狐浏览器不弹出页面

        ```python
        from selenium.webdriver.firefox.options import Options
         
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(firefox_options=options, executable_path=ex_path)
        ```

     2. 谷歌浏览器不弹出界面

        ```python
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from PIL import Image,ImageEnhance
         
        path = 'C:/dd/chromedriver.exe'  # chromedriver.exe 驱动的路径
         
        #打开浏览器
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
         
        # 创建浏览器对象
        driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        ```

+ Selenium 常用方法:

  1. `driver = webdriver.Chrome(executable_path=executable_path)` : 创建 driver 对象 **executable_path** 表示浏览器 chromedriver  地址
     1. `driver.get(url)` : 打开指定 url 界面
     2. `driver.quit()` : 关闭 打开页面
     3. `driver.page_source` : 获取页面源码 (加载过 AJAX 等请求后的页面源码)
     4. `driver.maximize_window()` : 打开窗口最大化
     5. `driver.save_screenshot('go.png')` : 页面截屏,截取全屏
  2. 模拟按键操作
     1. 导入 **Keys** 方法 : `from selenium.webdriver.common.keys import Keys`
     2. 获取操作对象的标签 : `input_label = driver.find_element_by_id('kw')`
     3. 对操作对象传参或者按键操作
        1. 传参 : `input_label.send_keys("python")`
        2. 按键操作 :
           + 单个按键 : `input_label.send_keys(Keys.ENTER)` (回车键)
           + 组合按键 : `input_label.send_keys(Keys.CONTROL, "x")` (Ctrl+X)
        3. 获取操作对象的左顶点位置 (返回 x, y 坐标字典数据) : `input_label.location`
        4. 获取操作对象的尺寸 (返回 height 和 weight 字典数据) : `input_label.size`

+ Selenium 操作的重点在于 确定等待时间 以提高效率

  1. 强制等待 : `import time`

     ```python
     import time
     time.sleep(3)
     ```

  2. 隐式等待 : `driver.implicitly_wait(wait_time)`

     + 页面全部加载结束开始运行,指定最大等待时长,超出等待时长或等待时长内加载失败报一个异常
     + 等待加载包括页面广告、静态 JS 等无用信息，
     + 遇到页面异步加载不能使用

  3. 显式等待 (WebDriverWait) : 等待页面特定元素 (使用元素定位器定位) 满足特定条件 (定位器和特定查询条件) 开始加载

     1. 导入 定位器、查询条件、显式等待所用方法

        ```python
        from selenium.webdriver.common.by import By  # 定位器
        from selenium.webdriver.support import expected_conditions as EC  # 查询条件
        from selenium.webdriver.support.wait import WebDriverWait  # 显式等待
        ```

     2. 创建显式等待对象

        ```python
        wait = WebDriverWait(driver, 20)
        ```

     3. 使用定位器 根据 查询条件 确定加载等待用时

        + `EC.presence_of_element_located(查询方法, 定位语句)` : 定位单个元素

        + `EC.presence_of_all_elements_located(查询方法, 定位语句)` : 定位多个元素

        + 实例

          ```python
          wait.until(EC.presence_of_all_elements_located(By.XPATH, '等待位置的 XPATH 语句'))   # 等到元素出现为止,传入定位器
          ```

          

##### PhantomJS 简介

+ PhantomJs : 基于 Webkit 的 "无界面" (headless) 浏览器,会把网站加载到内存并执行页面上的 JavaScript,由于不展示图形界面,所以使用效率更高
+ PhantomJS 只能从官网[下载](https://phantomjs.org/download.html),pahntomJS 是一个功能完善的浏览器

##### JS 简介

+ 判断 PhantomJS 安装成功:
  1. 设置环境变量后,打开 cmd ,直接输入 `phantomjs` 成功运行则安装成功
  2. `driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows\bin\phantomjs.exe')`