### 语法综述

### re 正则表达式

1. #### 正则表达式 (规则表达式, Regular Expression)
    + 程序中常用缩写 regex / regexp
    + 专门用于进行文本 (字符串) 检索、匹配、替换等操作
    
2. #### python 正则表达式库
    `import re`
    
3. #### 字符查询匹配函数
    + 参数
        + pattern:  正则表达式 
        + string:    要去操作的字符串  
        + flags=0     标志位 用于控制正则表达式的方式
        + re.I   匹配时忽略大小写
        + re.M   多行匹配   
        + re.S   让.可以匹配所有的单个字符 包括换行符 
    
    函数 | 描述
    :---: | :---:
    re.match(patter, string) | 用于在**开始位置**匹配目标字符串 string 中符合正则表达式 patter 的字符，匹配完成会返回一个 match 对象，匹配不成功返回 None
    re.search(patter, string) | 扫描**整个字符串string**中符合正则表达式 patter 的字符，匹配完成会返回匹配的第一个 match 对象，匹配不成功返回 None
    re.findall(patter, string) | 扫描**整个字符串string**, 将符合正则表达式 patter 的字符全部提取出来存放在列表中,返回
    re.fullmatch(patter, string) | 扫描**整个字符串string**，如果整个字符串都包含在正则表达式表示的范围中, 返回整个字符串, 否则返回None
    re.finditer(patter, string) | 扫描**整个字符串string**，将匹配到的字符保存在一个可以遍历的列表中
    
    ```python
   import re
    
   string = "Hello Word"
    
   res_match = re.match('He', string)
   res_search = re.search('Wo', string)
   res_findall = re.findall('o', string)
   res_full = re.fullmatch('Hello Word', string)
   res_finditer = re.finditer('o', string)
    
   print(res_match)
   print(res_match.group())
   print(res_search)
   print(res_search.group())
   print(res_findall)
   print(res_full)
   print(res_full.group())
   print(res_finditer)
   for i in res_finditer:
       print(i)
       print(i.group())
   """
   # 返回中 span 表示查到字符串位置 (start, end) 
   # 返回中 match 未匹配到字符 group() 或 group(0) 直接取出匹配字符
   <re.Match object; span=(0, 2), match='He'>
   He
   <re.Match object; span=(6, 8), match='Wo'>
   Wo
   ['o', 'o']
   <re.Match object; span=(0, 10), match='Hello Word'>
   Hello Word
   <callable_iterator object at 0x0000024A80F3EC18>
   <re.Match object; span=(4, 5), match='o'>
   o
   <re.Match object; span=(7, 8), match='o'>
   o
   """
    ```

    
4. #### 字符串拆分替换函数

    函数 | 描述
    :---: | :---:
    re.split(reg, string) | 使用正则表达式 reg 匹配的字符, 将字符串 string 拆分成一个字符串列表
    re.sub(reg, repl, string) | 使用**指定的字符串 repl**来 替换 **目标字符串string** 中匹配 **正则表达式reg** 的字符
    
    ```python
   import re

   string = "Hello Word"
    
   res_split = re.split('o', string)
   res_sub = re.sub('o', 'M', string)
    
   print(res_split)
   print(res_sub)
   """
   ['Hell', ' W', 'rd']
   HellM WMrd
   """
   ```
    
5. #### 正则表达式元字符
    
    元字符 | 描述
    :---: | :---:
     ^  | 表示匹配字符串的开头位置的字符
     $  | 表示匹配字符串的结束位置的字符
     .  | 表示匹配任意一个字符 (re.M 多行匹配)
     \d | 匹配一个数字字符
     \D | 匹配任意一个非数字字符
     \s | 匹配一个空白字符
     \S | 匹配一个非空白字符
     \w | 匹配一个数字\字母\下划线中的任意一个字符
     \W | 匹配一个非(数字\字母\下划线)中的任意一个字符
     \b | 匹配一个单词的边界
     \B | 匹配不是单词的开头或结束位置
     
     ```python
   import re
    
   # 正则表达式元字符
   string = '1783184424 Hello'
    
   # 任意一个字符
   res_1 = re.findall('.', string)
   # 一个数字字符
   res_2 = re.findall('\d', string)
   # 任意一个非数字字符
   res_3 = re.findall('\D', string)
   # 一个空白字符
   res_4 = re.findall('\s', string)
   # 一个非空白字符
   res_5 = re.findall('\S', string)
   # 一个数字\字母\下划线中的任意一个字符
   res_6 = re.findall('\w', string)
   # 一个非(数字\字母\下划线)中的任意一个字符
   res_7 = re.findall('\W', string)
   # 一个单词的边界
   res_8 = re.findall('\b', string)
   # 不是单词的开头或结束位置
   res_9 = re.findall('\B', string)
    
   print(res_1)
   print(res_2)
   print(res_3)
   print(res_4)
   print(res_5)
   print(res_6)
   print(res_7)
   print(res_8)
   print(res_9)
   """
   ['1', '7', '8', '3', '1', '8', '4', '4', '2', '4', ' ', 'H', 'e', 'l', 'l', 'o']
   ['1', '7', '8', '3', '1', '8', '4', '4', '2', '4']
   [' ', 'H', 'e', 'l', 'l', 'o']
   [' ']
   ['1', '7', '8', '3', '1', '8', '4', '4', '2', '4', 'H', 'e', 'l', 'l', 'o']
   ['1', '7', '8', '3', '1', '8', '4', '4', '2', '4', 'H', 'e', 'l', 'l', 'o']
   [' ']
   []
   ['', '', '', '', '', '', '', '', '', '', '', '', '']
   """
   ```
     
6. #### 正则表达式中的量词 (量词 : 用于限定字符出现数量的关键词)
 
    量词 | 描述
    :---: | :---:
     *  | 用于匹配符号 * 前面的字符出现 **0次或者多次**,不存在返回空
     +  | 用于匹配符号 + 前面的字符出现 **1次或者多次**,不存在则不返回
     ?  | 用于匹配符号 ? 前面的字符 (尽可能少的匹配)
     {n} | 用于匹配符号 {n} 前面的字符出现 **n** 次
     {m, n} | 用于匹配符号 {m, n} 前面的字符出现至少 m 次，最多 n 次
     {n, } | 用于匹配符号 {n, } 前面的字符出现至少 **n** 次
     
7. #### 正则表达式范围匹配 (针对字符串匹配, 类似于元字符匹配)
    
    范围 | 描述
    :---: | :---:
    [0-9] | 用于匹配一个 0~9 之间的数字 <==> \d
    [^0-9] | 用于匹配一个非数字字符 <==> \D
    [3-6] | 用于匹配一个 3~6 之间的数字
    [a-z] | 用于匹配一个 a~z 之间的字母
    [A-Z] | 用于匹配一个 A~Z 之间的字母
    [a-f] | 用于匹配一个 a~f 之间的字母
    [a-zA-Z] | 用于匹配一个 a~z或者A~Z 之间的字母，匹配任意一个字母
    [a-zA-Z0-9] | 用于匹配一个字母或数字
    [a-zA-Z0-9_] | 用于匹配一个数字\字母\下划线中的任意一个字符 <==> \w
    [^a-zA-Z0-9_] | 匹配一个非(数字\字母\下划线)中的任意一个字符 <==> \W
    
    ```python
   import re
    
   # 正则表达式范围匹配
   string = '17 83 18 442 4 Hello'
    
   res_1 = re.findall('[1-4]', string)
   res_2 = re.findall('[^0-9]', string)
   res_3 = re.findall('[a-z]', string)
   res_4 = re.findall('[A-Z]', string)
   res_5 = re.findall('[a-zA-Z]', string)
   res_6 = re.findall('[0-9a-zA-Z]', string)
   res_7 = re.findall('[^0-9a-zA-Z]', string)
    
    
   print(res_1)
   print(res_2)
   print(res_3)
   print(res_4)
   print(res_5)
   print(res_6)
   print(res_7)
   """
   ['1', '3', '1', '4', '4', '2', '4']
   [' ', ' ', ' ', ' ', ' ', 'H', 'e', 'l', 'l', 'o']
   ['e', 'l', 'l', 'o']
   ['H']
   ['H', 'e', 'l', 'l', 'o']
   ['1', '7', '8', '3', '1', '8', '4', '4', '2', '4', 'H', 'e', 'l', 'l', 'o']
   [' ', ' ', ' ', ' ', ' ']
   """
   ```
    
8. #### 正则表达式分组 (再一次完整的匹配过程中，将匹配到的结果进行分组，细化对匹配结果的操作，正则表达式通过 () 分组，以提取匹配结果的部分结果)

    分组 | 描述
    :---: | :---:
    (expression) | 使用圆括号直接分组; 正则表达式本身匹配的结果就是一个组，可以通过 group() 或 group(0) 获取; 然后正则表达式中包含的圆括号就是按照顺序从 1 开始编号的子组
    (?P<name>expression) | 使用 圆括号分组, 然后给当前的圆括号表示的小组命名为 name ,可以通过 group(name) 进行数据的获取

    ```python
   import re
    
   string = '<a href="http://www.baidu.com">百度</a><a href="http://www.mi.com">小米</a>'
    
   res = re.findall('<a href=".*?">.*?</a>', string)
   res_1 = re.findall('<a href="(.*?)">.*?</a>', string)
   # 分组匹配
   res_2 = re.search('<a href="(.*?)">(.*?)</a>', string)
   # 命名匹配
   res_3 = re.search('<a href="(?P<url>.*?)">(?P<content>.*?)</a>', string)
    
   print(res)
   print(res_1)
   print(res_2)
   print(res_2.group())
   print(res_2.group(1))
   print(res_2.group(2))
    
   print(res_3)
   print(res_3.group('url'))
   print(res_3.group('content'))
   """
   ['<a href="http://www.baidu.com">百度</a>', '<a href="http://www.mi.com">小米</a>']
   ['http://www.baidu.com', 'http://www.mi.com']
   <re.Match object; span=(0, 37), match='<a href="http://www.baidu.com">百度</a>'>
   <a href="http://www.baidu.com">百度</a>
   http://www.baidu.com
   百度
   <re.Match object; span=(0, 37), match='<a href="http://www.baidu.com">百度</a>'>
   http://www.baidu.com
   百度
   """
   ```

9. #### 贪婪模式和懒惰模式
    + 贪婪模式 (*, +默认贪婪模式 , .*, .+ 尽可能多的匹配数据) 
        + 正则表达式的一种模式，速度快，但是匹配到的内容会**从字符串两头**向中间搜索匹配，一旦匹配到就不向中间继续匹配
        + 贪婪模式就是从两头向中间查找，找到匹配就停止，两匹配符内部所有一并返回
        
    + 懒惰模式/禁止贪婪 (.*?, .+? 尽可能少的匹配数据)
        + 正则表达式另一种模式，会首先搜索匹配正则表达式开始位置的字符，然后逐步向字符串结束位置查找，一旦找到匹配的就返回，然后继续查找。
        + 懒惰模式就是从头向尾查找，找到匹配就返回，一直查找
        
    ```python
   import re
    
   # 贪婪和非贪婪
   string = '<a href="http://www.baidu.com">百度</a><a href="http://www.mi.com">小米</a>'
    
   res_1 = re.findall('<a.*?>', string)
   res_2 = re.findall('<.*>', string)
    
   print(res_1)
   print(res_2)
   """
   ['<a href="http://www.baidu.com">', '<a href="http://www.mi.com">']
   ['<a href="http://www.baidu.com">百度</a><a href="http://www.mi.com">小米</a>']
   """
    ```
        
### 迭代器

1. #### 迭代器
    
    1. 迭代 : 迭代是访问集合元素的一种方式，可以将某个数据集内的数据 "一个接一个的取出来" 
    
    2. 可迭代协议 : 内部实现了 \_\_iter__ 方法
    
    3. 迭代器协议 : 必须拥有 \_\_iter__ 方法和 \_\_next__ 方法
    
    4. 迭代器内三个方法:
        + \_\_next__() : 取数据
        + \_\_length_hint__() : 记录数据个数
        + \_\_setstate__() : 纪录迭代的位置
    
2. #### for 循环原理
    
    1. for 循环一个可迭代的对象 (实现 \_\_iter__ 方法)
    
    2. \_\_iter__ 方法返回一个迭代器 (迭代器实现了 \_\_iter__ 方法和 \_\_next__ 方法)
    
    3. for 先判断对象地方可迭代，然后调用迭代器的 \_\_next__ 方法获取值
    
3. #### 迭代器作用
    + 节约内存，取用的时候再生成数据, python 2.7 的时候 range() 方法立刻生成数据，占用大量内存空间

4. #### 应用场景
    + 数据类型转换就是使用的迭代器
        ```
      str1 = 'Fibo'
      print(list(str1))
      print(tuple(str1))
      """
      ['F', 'i', 'b', 'o']
      ('F', 'i', 'b', 'o')
      """
      ```
    
    + 斐波拉契数列
        ```
        class Fibonacci:
    
        def __init__(self, all_num):
            self.all_num = all_num
            self.a = 1
            self.b = 1
            self.current_num = 0
    
        def __iter__(self):
            # 返回自己调用自己的 __next__() 方法
            return self
    
        def __next__(self):
            if self.all_num <= 2:
                self.current_num += 1
                if self.current_num == 3:
                    raise StopIteration
                return self.a
            else:
                if self.current_num < self.all_num:
                    ret = self.a
                    self.a, self.b = self.b, self.a + self.b
                    self.current_num += 1
                    return ret
                else:
                    raise StopIteration
    
    
        for i in Fibonacci(100):
            print(i)
      ```
      
### 生成器 (本质: 迭代器)

+ 项目中有大量数据需要存储
    + 通过列表生成式，直接创建列表存储
        + 弊端 : 内存开销大，耗时长，只要创建无论数据是否被使用，都已经存储至内存
    + 通过生成器生成，优化，**记录数据的生成**，需要时生成需要的数据，不是一次生成全部

+ 生成器函数 (一个包含 yield 关键字的函数就是一个生成器函数。并且 yield 不能与 return 共用, yield 只能用在函数内)
    1. 生成器函数执行之后会得到一个生成器作为返回值，并不会执行函数体
    2. 执行了\_\_next__() 方法之后才会执行函数体,并获得返回值
    3. next() 内置方法, 内部调用生成器函数的\_\_next__方法
    4. yield 和 return 相同的是都可以返回值，不同的是 yield 不会结束函数
    ```
    def generator():
        print('zzz')
        yield
    
    
    ret = generator()
    print(ret)
    # <generator object generator at 0x0000026FC9A12840>
    print(ret.__next__())
    # zzz
    # None
  ```
    ```
  def generator():
      print('zzz')
      yield 1
    
    
  res = generator()
  ret = res.__next__()
  print(ret)
  # zzz
  # 1
  ```
  
+ send() : 获取下一个值的效果和 next() 基本一致, 只是在获取下一个值的时候,给**上一个** yield 的位置传递一个数据 (如果没有上一个yield send(None))
    + 注意事项
        1. 第一次使用生成器的时候是用 next 获取下一个值
        2. 最后一个 yield 不能接受外部的值
    
    ```python
  def generator():
      print("a")
      count = yield 1
      print(f'---->, {count}')
      print('b')
      yield 2
    
    
  g = generator()
  next(g)
  ret2 = g.send('123')
  print(ret2)
  """
  a
  ---->, 123
  b
  2
  """
  ```
  ```python
  def fund():
      print("爬取数据")
      a = yield "爬取到的数据"
      print(f'{a}是send传递的数据')
    
      yield 'over'
    
    
  res =fund()
    
  print(res.send(None))
  print(res.send('123'))
  #  报错最后一个 yield 不能接受外部的值
  print(res.send("2222"))
  """
  StopIteration
  爬取数据
  爬取到的数据
  123是send传递的数据
  over
  """
  ```
    
+ yield from : 循环遍历容器类型
    ```python
  def func():
      yield from range(1,10)
    
    
  res = func()
  print(res)
  print(list(res))
  """
  <generator object func at 0x0000010DDF342840>
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
  """
   ```

+ 生成器表达式  (存储的是生成方式)
    + 格式 
        + 将列表解析式 [] 改为 () 即可
        + 使用是可以遍历
    ```python
  import sys
    
  arr = [i for i in range(1000000)]
    
    
  print(sys.getsizeof(arr))
    
  # 生成器
    
  tup = (i for i in range(1000000))
    
  print(sys.getsizeof(tup))
  print(tup.__next__())
  print(next(tup))
  """
  8697464
  120
  0
  1
  """
  ```