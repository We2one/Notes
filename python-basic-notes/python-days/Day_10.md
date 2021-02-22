# Day_10

## 内置模块

+ random 模块 (随机模块)
    + 随机小数   
        + **random()** : 产生 0-1 之间的随机小数 
             ```
          import random
          # from random import random
          random.random()
          # random()
          ```
          
        + uniform(a, b) : 指定范围随机小数
    + 随机整数
        + randint(a, b) : 指定范围随机整数，包含开头结尾
        
        + randrange(start, stop, [step]) : start, stop 范围内间隔指定步长 (step) 的整数，包含开头不包含结尾
        
    + 随机选择一个数据
        + random.choice(lst) : 随即返回可迭代序列的一个数据
            ```python
          # from random import choice
          import random
          lst = [1,2,3,4,5]
          random.choice(lst)
          # choice(lst)
          ```
    
    + 打乱
        
        + random.shuffle(可迭代序列) : 打乱列表顺序
    
+ sys 模块    `imort sys`
  
    + sys.version : 返回解释器版本号
        ```
      >>> sys.version
      '3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]'
      ```
    
    + sys.path : 返回模块搜索路径
        ```
      >>> sys.path
      ['', 'E:\\PyCharm 2020.2\\python3.7\\python37.zip', 'E:\\PyCharm 2020.2\\python3.7\\DLLs', 'E:\\PyCharm 2020.2\\python3.7\\lib', 'E:\\PyCharm 2020.2\\python3.7', 'E:\\PyCharm 2020.2\\p
      ython3.7\\lib\\site-packages', 'E:\\PyCharm 2020.2\\python3.7\\lib\\site-packages\\win32', 'E:\\PyCharm 2020.2\\python3.7\\lib\\site-packages\\win32\\lib', 'E:\\PyCharm 2020.2\\python3
      .7\\lib\\site-packages\\Pythonwin']
      ```
    
    + sys.argv : 接收命令行下参数
        ```
      import sys
    
      print(sys.argv)
      print(ret[0])
      print(ret[1])
      print(ret[2])
      
      >>>python Day_10.py run start
          ['Day_10.py', 'run', 'start']
          Day_10.py
          run
          start
      ```
    
+ string : 提供系统中字符串的基本操作方式，描述当前编程语言中使用到的字符分类  `import string`
    + string 模块下 所有内容
        ```
      whitespace = ' \t\n\r\v\f'
      ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
      ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      ascii_letters = ascii_lowercase + ascii_uppercase
      digits = '0123456789'
      hexdigits = digits + 'abcdef' + 'ABCDEF'
      octdigits = '01234567'
      punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
      printable = digits + ascii_letters + punctuation + whitespace
      ```

    + 查看 string 模块 `dir(str)`
        ```
      >>> dir(string)
      ['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', 
      '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re',
      '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 
      'octdigits', 'printable', 'punctuation', 'whitespace']
      ```
      
    + 字符串显示大小写全英文字母  `string.ascii_letters`
        ```
      >>> string.ascii_letters
      'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
      ```
      
    + 字符串显示大写全英文字母  `string.ascii_uppercase`
        ```
      >>> string.ascii_uppercase
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      ```
      
    + 字符串显示小写全英文字母  `string.ascii_lowercase`
        ```
      >>> string.ascii_lowercase
      'abcdefghijklmnopqrstuvwxyz'
      ```
      
    + 字符串显示 0~9 十个数字    `string.digits`
        ```
      >>> string.digits
      '0123456789'
      ```
      
    + 字符串显示 十六进制用到的所有字母数字 `string.hexdigits`   
        (hexdigits = digits + 'abcdef' + 'ABCDEF')
        ```
      >>> string.hexdigits
      '0123456789abcdefABCDEF'
      ```
      
    + 字符串显示 八进制用到所有数字 `string.octdigits`
        (octdigits = '01234567')
        ```
      >>> string.octdigits
      '01234567'
      ```
      
    + string.whitespace  将为字符提供空格，制表符，换行符，返回符，换页符和垂直制表符。 `string.whitespace`
        ```
      >>> string.whitespace
      ' \t\n\r\x0b\x0c'
      ```
      
    + string.printable  返回所有标点符号集，数字，ascii_letters和空格。 `string.printable`
        ```
      >>> string.printable
      '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
      ```
      
    + random 与 string 模块结合生成六位数验证码

        ```
        >>>''.join(random.sample(string.ascii_letters+string.digits, 6))
        'A0yNxY'
        ```

        

+ time 模块

    + python 表示时间的三种方式

        1. **时间戳 (timestamp)** [计算机能够识别的时间格式, float类型]

           + 表示的是从 1970年1月1日00:00:00 开始到现在的秒值

        2. **时间元组 (struct_time)** [人方便观看的时间格式]

           + 9 个元素 (年、月、日、时、分、秒、一周的第几日、一年的第几天、夏令时)

             元素| 属性 | 值
             :---: | :---: | :---:
             tm_year | 年 | (4 位数) 2008
             tm_mon  | 月 | 1 - 12
             tm_mday | 日 | 1 - 31
             tm_hour | 小时 | 0 - 23
             tm_min  | 分钟 | 0 - 59
             tm_sec  | 秒   | 0 - 61 (60 或 61 是闰秒)
             tm_wday | 一周的第几日 | 0 - 6 (0 是周一)
             tm_yday | 一年的第几日 | 1 - 366 (儒略历)
             tm_isdst | 夏令时 | -1, 0, 1 (-1 是决定是否为夏令时的旗帜) 

        3. **格式化的时间字符串** [便于操作的时间格式]

            + 表示方式 : '1999-1-02'
              
                元素 | 属性 | 值
                :---: | :---: | :---:
                %y | 两位数的年份表示 | 00 - 99
                %Y | 四位数的年份表示 | 000 - 9999
                %m | 月份 | 01 - 12
                %d | 月内的一天 | 0 - 31
                %H | 24 小时制小时数 | 0 - 23
                %I | 12 小时制小时数 | 01 - 12
                %M | 分钟数 | 0 - 59
                %S | 秒 | 0 - 59
                %a | 本地简化星期名称
                %A | 本地完整星期名称
                %b | 本地简化月份名称
                %B | 本地完整月份名称
                %c | 本地相应的日期表示和时间表示
                %j | 年内的一天 | 001 - 366
                %p | 本地 A.M. 或 P.M. 的等价符 上午下午
                %U | 一年中的星期数 (星期天为星期的开始) | 00 - 53
                %w | 星期 (星期天为星期的开式) | 0 - 6
                %W | 一年中的星期数 (星期一为星期的开始) | 00 - 53
                %x | 本地相应的日期表示
                %X | 本地相应的时间表示
                %Z | 当前时区的名称
                %% | % 号本身

    + **time.sleep(seconds)** : 睡眠功能，是程序休眠多少秒后继续执行

    + **time.time()** : 时间戳
        
        + 使用 : 定义两个时间戳(start, end)在程序的开始与结尾， end-start 为程序运行时间
        
    + **time.localtime(seconds=None**) : 时间元组 (可以传入时间戳来转化为时间元组)
        
      ```
      # 将当前时间戳转化为时间元组
      >>> time.localtime()
      time.struct_time(tm_year=2020, tm_mon=8, tm_mday=21, tm_hour=10, tm_min=27, tm_sec=27, tm_wday=4, tm_yday=234, tm_isdst=0)
      ```
      
    + **time.strftime(format, p_tuple=None)** : 根据格式规范将**时间元组**转换为字符串, 默认为当前时间
        
        + format : 自定义的时间格式
        + p_tuple : 需要 **元组** 或 **struct_time** 参数 默认为当前时间(struct_time类型为 time.localtime()返回类型)
      ```
      >>> time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
      '2020-08-21 10:32:50'
      >>> time.strftime('%Y-%m-%d %H:%M:%S')
      '2020-08-21 10:35:31'
      >>> time.strftime('%Y/%m/%d %H:%M:%S')
      '2020/08/21 10:36:10'
      >>> time.strftime('%x %X')
      '08/21/20 10:37:58
      ```
      
    + 时间戳与时间元组转换
        + 时间戳转化为时间元组 
            + **time.gmtime(seconds=None)** UTC 时间 (世界统一时间比北京时间少 8 小时)和 time.localtime() (本地时间) 默认为当前时间
                
              ```
              >>> time.gmtime()
              time.struct_time(tm_year=2020, tm_mon=8, tm_mday=21, tm_hour=2, tm_min=48, tm_sec=18, tm_wday=4, tm_yday=234, tm_isdst=0)
              >>> time.localtime()
              time.struct_time(tm_year=2020, tm_mon=8, tm_mday=21, tm_hour=10, tm_min=48, tm_sec=55, tm_wday=4, tm_yday=234, tm_isdst=0)
              ```
        + 时间元组转化为时间戳
            + **time.mktime()** 
                
              ```
              >>> time.mktime(time.localtime())
              1597978194.0
              >>> time.mktime(time.gmtime())
              1597949433.0
              >>> time.time()
              1597978205.5068083
              ```
        
    + 时间元组和格式化字符串之间的转换
        + 时间元组转化字符串
            + **time.strftime("格式定义", "结构化时间")** 结构化时间若不传，默认为当前时间
                
              ```
              >>> time.strftime('%x %X')
              '08/21/20 10:37:58'
              ```
        + 字符串转时间元组
            + **time.strptime("时间字符串", "字符串对应格式")**
                
              ```
              >>> time.strptime('Fri Aug 21 10:52:32 2020')
              time.struct_time(tm_year=2020, tm_mon=8, tm_mday=21, tm_hour=10, tm_min=52, tm_sec=32, tm_wday=4, tm_yday=234, tm_isdst=-1)
              >>> time.strptime("2020-2-1", "%Y-%m-%d")
              time.struct_time(tm_year=2020, tm_mon=2, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=32, tm_isdst=-1)
              ```
        
    + 时间元组 --> %a %b %d %H:%M:%S %Y 时间串 (周 月 日 时:分:秒 年)
        + **time.asctime("结构化时间")** 若不传参数，默认为当前时间的格式串
            
          ```
          >>> time.asctime()
          'Fri Aug 21 10:52:32 2020'
          ```
        
    + 时间戳 --> %a %b %d %H:%M:%S %Y 时间串 (周 月 日 时:分:秒 年)
        + **time.ctime("时间戳"**) 若不传参数，默认为当前时间的格式串
            
          ```
          >>> time.ctime(time.time())
          'Fri Aug 21 10:53:28 2020'
          >>> time.ctime(time.mktime(time.localtime()))
          'Fri Aug 21 10:54:00 2020'
          >>> time.ctime(time.mktime(time.gmtime()))
          'Fri Aug 21 02:54:23 2020'
          ```

+ datetime 模块   `import datetime`
    + **datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])**   生成 日期和时间的结合
        
        + 必须输入年，月和日。
        + tzinfo可以为None，或者为tzinfo子类的实例。
        + 其余参数是整数。
      ```
      >>> print(datetime.datetime(2020,3,4,5,5,6))
      2020-03-04 05:05:06
      ```
    + **datetime.date(year, month, day)**  生成理想化的简单型日期，它假设当今的公历在过去和未来永远有效
        
      ```
      >>> print(datetime.date(2020,5,6))
      2020-05-06
      ```
    + **datetime.time(hour, minute, second[, microsecond[, tzinfo]])** 生成独立于任何特定日期的理想化时间，它假设每一天都恰好等于 24*60*60 秒。 （这里没有“闰秒”的概念。）
        
      ```
      >>> print(datetime.time())
      00:00:00
      >>> print(datetime.time(4,5,6))
      04:05:06
      ```
    + **d = datetime.now()** 当年时间 年月日时分秒
        
      ```
      >>> datetime.datetime.now()
      datetime.datetime(2020, 8, 21, 13, 56, 59, 65930)
      ```
        + d.year  年
        + d.month  月
        + d.day  日
        + d.hour 时
        + d.minute  分
        + d.microsecond 微秒
    
+ hashlib 模块 (加密模块) `import hashlib`
    + 加密方式 ['algorithms_available', 'algorithms_guaranteed', 'blake2b', 'blake2s', 'md5', 'new', 'pbkdf2_hmac', 'scrypt', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']

## 面向对象 编程(Object Oriented Programming， OOP)

+ 术语
    + 类 : 具有共同特征以及行为的对象的抽象，描述一类事物
    + 对象 : 实际存在的物体，包含具体属性和方法的实体
    + 属性 : 变量 ，存储数据， 描述事物的特征
    + 方法 : 类中声明的 函数， 描述事务的行为
    + 构造方法 : 通过指定的类创造对象的方法，通过构造方法按照需求创建对应类的对象
    + 类和对象关系 : 计算机编程语言中描述事物的载体。对象是类的实例，类是对象的模板

+ 类的声明 (class) 
    + 基本语法 
        ```
      class 类名:
        """类的文档注释"""
        def __init__(self, name):
            """声明属性的方法"""
            # 自定义属性: 固定语法
            self.name = name
      
        def study(self):
            """方法文档注释"""
            代码
      ```
    
+ 面向对象设计开发
    + 面向对象分析 (OOA: Object-Oriented Analysis)
    + 面向对象设计 (OOD: Object-Oriented Design)
    + 面向对象编程 (OOP: Object-Oriented Programming)
    + 面向对象测试 (OOT: Object-Oriented Testing)
    
+ \_\_new\_\_(cls, *args, **kwargs) : 创建对象实例方法 (最先被调用) ，实例化时先 \_\_new\_\_ 再 \_\_init\_\_ 
    
    + 当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。
+ \_\_init\_\_(self) : 类的构造函数或初始化方法，可以让创建对象更加灵活
+ \_\_str\_\_(self) : 目标是可读性，或者说，\_\_str\_\_的结果是让人看的。打印对象的属性信息，方便我们调试代码。
+ \_\_repr\_\_(self) : 目标是准确性，或者说，\_\_repr\_\_的结果是让解释器用的,转化为供解释器读取的形式
+ \_\_del\_\_(self) :  当一个对象被从内存中销毁前(把这个对象从内存中删除掉),会自动调用\_\_del\_\_方法
+ \_\_dict\_\_ : 类的属性（包含一个字典，由类的数据属性组成）
+ \_\_doc\_\_ : 类的文档字符串
+ \_\_module\_\_: 类定义所在的模块（类的全名是'\_\_main\_\_.className'，如果类位于一个导入模块mymod中，那么className.\_\_module\_\_ 等于 mymod）
+ \_\_bases\_\_ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
+ \_\_cmp\_\_ ( self, x ) : 对象比较, 简单的调用方法 : cmp(obj, x)