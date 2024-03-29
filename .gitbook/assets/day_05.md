# Day_05

### 元组 (组合数据中的一种，**不可变的**、**可存储的**、**有序的**、**不同类型的**、**可重复的**序列数据类型)
+ 格式 (tuple()) 
    + 使用 () 包裹，元素之间通过 "," 隔开

+ 元组数据的访问和操作
    + 通过索引访问: (变量名[index])
        + 不能直接通过元组索引 (变量名[index]) 修改数据，会报错
        + 如果元组中存有可变数据，那么可变数据可以通过 (变量名[index]) 修改
    + 循环遍历元组中数据 for i in 元组
    + 切片操作 (start, stop[, step])
    + 元组的拼接与重复
    + 元组的序列解包
    + tuple() 将其它类型数据转换为元组

+ 元组的内置方法
    + count() : 返回元组中指定元素的个数
    + index() : 从左到右返回第一个遇到的指定元素的索引，没有就报错
    + enumerate() : 内置函数，返回 索引 与 元素

+ 元组的使用
    + 不可修改数据的使用

### 字典

+ 字典的概述和声明格式
    + 具有映射关系，以键值对方式存储 (key: value)
    + 格式 : {key: value, key: value}
    + 使用 {} 包裹，一个 key 对应 一个 value，key: value 之间 ":"隔开，一对 key: value 是一组数据，数据之间用 "," 隔开
    + 字典的 key 是 **不可变的**， **不可重复的**
    + dict([(, ), (, ), (, )])
    + dict(name= "", age = "")
    + 创建字典 : fromkeys(iterable, value=None, /), 创建空字典，以 iterable 内容为 key 值， value 为 字典初始值 (默认为空)
        ```
      >>> {}.fromkeys([1,2,3,4,5])
      {1: None, 2: None, 3: None, 4: None, 5: None}
      >>> {}.fromkeys([1,2,3,4,5], "default")
      {1: 'default', 2: 'default', 3: 'default', 4: 'default', 5: 'default'}
      ```

+ 字典的操作方法

    + 操作方法
        ```
      >>> a
      {'name': '小明', 'age': 18}
      ```
        + 增加操作
            + 变量名[key] = value
                ```
              >>> a["gender"] = "男"
              >>> a
              {'name': '小明', 'age': 18, 'gender': '男'}
                ```
            + setdefault(key, default_value) : 通过 key 和 value ， 如果 key 存在什么都不改变
                ```
              >>> a.setdefault("gender", "男")
              '男'
              ```
        + 删除操作
            + pop(index) : 弹出，返回并删除指定键的对应值
                ```
              >>> a.pop("gender")
              '男'
              ```
            + popitem() : 弹出最后一个键值的元组
                ```
              >>> a.popitem()
              ('gender', '男')
              >>> a
              {'name': '小明', 'age': 18}
              ```
            + clear() : 清空字典
                ```
              >>> a.clear()
              >>> a
              {}
              ```
            + del : 删除整个字典，或通过字典的 key 删除对应键值对，Python内置方法 (def key[])
                ```
              >>> del a
              >>> a
              Traceback (most recent call last):
                File "<stdin>", line 1, in <module>
              NameError: name 'a' is not defined
              ```
        + 修改操作
            + 字典名[key] = value : 通过 key 添加 value 值，如果 key 存在则覆盖
                ```
              >>> a["name"] = "小红"
              >>> a
              {'name': '小红', 'age': 18}
              ```
            + update({"key": "value"}) 传递一个字典，如果 key 相同则覆盖，不存在则新建
                ```
              >>> a.update({"gender": "女"})
              >>> a
              {'name': '小红', 'age': 18, 'gender': '女'}
              ```
        + 查找操作
            + 根据 key 查找 (字典名[key]) : 如果存在 key 则返回 value，如果 key 不存在则报错 
                ```
                >>> a["name"]
                '小明'
                >>> a["gender"]
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                KeyError: 'gender'
                ```
            + get(key, default_value) :  如果存在 key 则返回 value，如果 key 不存在则返回 None (设置默认值的话，返回默认值)
                ```
                >>> a.get("age")
                18
                >>> a.get("gender")
                >>> a.get("gender", '男')
                '男'
              ```
            + keys : 以列表返回字典所有键
                ```
              >>> a.keys()
              dict_keys(['name', 'age'])
              ```
            + values : 以列表返回字典所有值
                ```
                >>> a.values()
                dict_values(['小明', 18])
                >>> list(a.values())
                ['小明', 18]
              ```
            + items : 以元组返回字典所有键值对
                ```
                >>> a.items()
                dict_items([('name', '小明'), ('age', 18)])
                >>> list(a.items())
                [('name', '小明'), ('age', 18)]
                >>> for key,value in a.items():
                ...     key
                ...     value
                ...
                'name'
                '小明'
                'age'
                18
              ```
            + len : 键值对个数
                ```
              >>> len(a)
              2
              ```
        + 字典常见操作 (字典遍历时的判断)
            + in : 查找指定的键是否存在
            + for .. in ... : 遍历字典
            + not in : 查找指定的键是否存在

### 集合

+ 格式
    + 集合 盛放**多个数据类型** , 集合中的元素的是 **无序的** **唯一的** **不可变的**
    + 格式
        + 变量名 = {元素, 元素, ...}
            ```
          >>> b = {2,2,3,4,5}
          >>> b
          {2, 3, 4, 5}
          ```
        + 变量名 = set(序列) (序列包括: 元组、字符串、...)  set 创建集合
            ```
          >>> b = set([1,2,3,4,5,4])
          >>> b
          {1, 2, 3, 4, 5}
          ```
        
+ 操作
    + 添加操作 (添加进去重复的自动去重)
        + add()
            ```
          >>> b.add(7)
          >>> b
          {1, 2, 3, 4, 5, 7}
          ```
        + update()
            ```
          >>> a
          {1, 2, 3, 4, 5, 6}
          >>> b
          {4, 5, 6, 7, 8, 9}
          >>> a.update(b)
          >>> a
          {1, 2, 3, 4, 5, 6, 7, 8, 9}
          ```
            
    + 删除操作
        + pop() : 随机删除
            ```
          >>> b.pop()
          1
          >>> b
          {2, 3, 4, 5}
          ```
        + remove()
            ```
          >>> b.remove(3)
          >>> b
          {2, 4, 5}
          ```
        + clear()
            ```
          >>> b.clear()
          >>> b
          set()
          ```
        + del
            ```
          >>> del b
          >>> b
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          NameError: name 'b' is not defined
          ```
    + 遍历集合
        ```
      >>> for i in b:
      ...     i
      ...
      1
      2
      3
      4
      5
      ```
    
+  集合数学运算
    ```
   >>> a = {1,2,3,4,5,6}
   >>> b = {4,5,6,7,8,9}
   ```
    + 交集 (& 或者 intersection) : 取公共部分
        ```
      >>> a & b
      {4, 5, 6}
      >>> a.intersection(b)
      {4, 5, 6}
      ```
    + 并集 (| 或者 union) : 取两集合所有内容，去除重复值
        ```
      >>> a | b
      {1, 2, 3, 4, 5, 6, 7, 8, 9}
      >>> a.union(b)
      {1, 2, 3, 4, 5, 6, 7, 8, 9}
      ```
    + 差集 (- 或者 difference) : 取 两集合 主集合(-前边的集合) 去除公共部分后的内容
        ```
      >>> a - b
      {1, 2, 3}
      >>> a.difference(b)
      {1, 2, 3}
      ```
    + 反交集 (^ 或者 symmetric_difference) : 取两集合去除 重复部分 的其他内容
        ```
      >>> a ^ b
      {1, 2, 3, 7, 8, 9}
      >>> a.symmetric_difference(b)
      {1, 2, 3, 7, 8, 9}
      ```
    + 子集 (< 或者 issubset) : 判断是否是子集，返回布尔值
        ```
      >>> a < b
      False
      >>> a.issubset(b)
      False
      ```
    + 超集 (> 或者 issuperset) : 判断是否是超集，返回布尔值
        ```
      >>> a > b
      False
      >>> a.issuperset(b)
      False
      ```
     
+ 集合应用
    + 过滤其他数据中的重复项

### 列表、元组、字典、集合的区别

数据类型比较 | 列表 | 元组 | 字典 | 集合
:---: | :---: | :---: | :---: | :---:
是否有序 | 是 | 是 | 否 | 否
能否修改 | 可以 | 不可以 | 可以 | 可以
方法多少 | 一般 | 很少 | 较多 | 一般
能否重复 | 可以 | 可以 | Key 不可重复, Value 可以重复 |不可
常用用途 | 临时存储批量数据 (使用时遍历)，不适合存储大量数据 (浪费内存空间) | 在项目中固定数据的声明 | 操作方式灵活，适用多数据操作 | 数据去重

### 字符串

+ 字符串概述 : 使用 ''/""/''''''' 包裹起来的数据

+ 字符串声明 : 
    + 变量 = ''
    + 变量 = "信息" 
    + 变量 = """信息(可换行)"""
    
+ 不可变类型 : 字符串一旦创建，内存中就不允许修改，如果需要修改，实在内存重新分配空间存储新字符串

+ 字符串索引 : 变量名[索引值]

+ 字符串切片 : 变量名[start, stop[, step]]

+ 字符串拼接 : 
    + "+" : 将两个字符串合并形成新字符串
    + "*" : 将一个字符串进行连续拼接
    
+ 赋值语句
    + 变量名 = ""
    + 变量名 = str(数据类型) (数据类型可以是 int ,float, bool)

+ 字符串函数
    + 字符串查找
        
        方法 | 描述
        :---: | :---:
        **.find()** | 查找，返回从左第一个指定字符的索引，找不到返回 -1
        .rfind() | 查找，返回从右第一个指定字符的索引，找不到返回 -1
        **.index()** | 查找，返回从左第一个指定字符的索引，找不到报错
        .rindex() | 查找，返回从右第一个指定字符的索引，找不到报错
        **.count()** | 计数，返回查找字符在字符串中个数
        **.endswith(suffix[, start[, end]])** | 返回值为 布尔值，如果以指定的后缀结尾，则返回True，否则返回False。start 为开始位置，end为结束位置，默认为整个字符串 (Python内置)
        **.startswith(prefix[, start[, end]])** | 返回值为 布尔值，如果以指定的字符串开头，则返回True，否则返回False。start 为开始位置，end为结束位置，默认为整个字符串 (Python内置)
        
    + 字符串拆分
    
        方法 | 描述
        :---: | :---:
        .partition() | 把 字符串 以 从左到右第一个匹配到的字符分为三个部分 (str 前、自身、后)
        .splitlines() | 按行 (换行符) 分割，返回一个包含各行作为元素的列表
        **.split()** | 按照指定"元素"分割，maxsplit: 默认将指定所有内容进行分割，可以指定 maxsplit 值 (maxsplit值为 1 只按照第一个指定内容分割，后面不分个割)
        
        ```
          >>> str = "124\n441"
          >>> str.splitlines()
          ['124', '441']
          >>> str.partition("\n")
          ('124', '\n', '441')
          >>> str.split("4")
          ['12', '\n', '', '1']
          ```
   
    + 字符串替换 
    
         方法 | 描述
        :---: | :---:
        **.replace()** | 从左到右替换指定元素，可以指定替换个数，默认全部替换
        .translate() | 按照对应关系替换内容 from string import maketrans
        
    + 字符串修饰
    
        方法 | 描述
        :---: | :---:
        **.center(width, fillchar)** | 让字符串在指定长度居中，如果不能居中 左短右长，可以指定填充内容，默认空格填充，如果指定长度小于原字符串长度则返回原字符串
        .ljust(width, fillchar) | 让字符串在指定长度左对齐，可以指定填充内容，默认空格填充，如果指定长度小于原字符串长度则返回原字符串
        .rjust(width, fillchar) | 让字符串在指定长度右对齐，可以指定填充内容，默认空格填充，如果指定长度小于原字符串长度则返回原字符串
        .zfill(width) | 返回指定长度的字符串，使原字符串右对齐，前面用 0 填充到指定字符串长度，若指定长度小于字符串长度，则直接输出元字符串
        **.format(value, format_spec)** | 通过 {} 和 : 代替之前的 % 。使用 format() 格式化字符串时，子字符串中使用 {} 作为占位符，占位符的内容将引用 format() 中参数进行替换。
        **.strip(chars)** | 去除字符串 开头结尾 处指定的字符，不会去除字符串中间对应的字符，默认为空格 (chars : 要去除字符)
        .rstrip(chars) | 截掉字符串右边空格或指定字符，默认为空格 (chars : 要去除字符)
        .lstrip(chars) | 截掉字符串左边空格或指定字符，默认为空格 (chars : 要去除字符)
        
    + 字符串格式化
        + format() 用法
            ```
          # 数据传参
          >>> "年龄: {}, 性别: {}，姓名:{}".format(19, "男", "小明")
          '年龄: 19, 性别: 男，姓名:小明'
          # 通过索引设置
          >>> print("年龄: {2}, 性别: {1}，姓名:{0}".format("小明","男", 19))
          年龄: 19, 性别: 男，姓名:小明
          # 通过 键值对索引 设置
          >>> "年龄: {age}, 性别: {gender}，姓名:{name}".format(name="小明",gender="男", age=19)
          '年龄: 19, 性别: 男，姓名:小明'
          # 字典传参
          >>> info = {"name": "小红", "age": 18}
          >>> "姓名:{name},年龄:{age}".format(**info)
          '姓名:小红,年龄:18'
          ```
            + 填充与格式化 
                + 格式 : :[填充字符][对齐方式<^>][宽度]
                    + ":<" : 左对齐
                        ```
                      >>> print("{:0<10}".format("你好"))
                      你好00000000
                      ```
                    + ":^" : 居中对齐
                        ```
                      >>> print("{:0^10}".format("你好"))
                      0000你好0000
                      ```
                    + ":>" : 右对齐 (默认)
                        ```
                      >>> print("{:0>10}".format("你好"))
                      00000000你好
                      ```
            + 精度与进制
                + :.2f  : 浮点数
                    ```
                  >>> print("{:.2f}".format(2))
                  2.00
                  ```
                + :b    : 二进制
                    ```
                  >>> print("{:b}".format(2))
                  10  
                  >>> print("{:0>10.2f}".format(16))
                  0000016.00
                  ```
                + :o    : 八进制
                    ```
                  >>> print("{:o}".format(16))
                  20
                  ```
                + :x    : 十六进制
                    ```
                  >>> print("{:x}".format(16))
                  10
                  ```
             
        + 字符串格式化 --> 百分号
            
            格式 | 描述
            :---: | :---:
            %% | 百分号标记
            %s | 字符串
            %f | 浮点型数字
            %d/i | 有符号整数 (十进制)
        
        + 字符串格式化 --> f-string
            + 格式 : f"{变量名}"
            + 在 {} 中可以做简单的运算
                ```
              >>> f"{2*8}"
              '16'
              ```
            + 左对齐/右对齐/居中对齐 </>/^
            + f"{:.2f}"
                ```
              >>> f"{13:.2f}"
              '13.00'
              ```
            + f"{:d}"
                ```
              >>> f"{13:b}"
              '1101'
              ```
            + f"{:o}"
                ```
              >>> f"{13:o}"
              '15'
              ```
            + f"{:x}"  
                ```
              >>> f"{13:x}"
              'd'
              ```
            
    + 字符串变形
    
        方法 | 描述
        :---: | :---:
        **.upper()** | 将字符串中的所有小写字母转换为大写字母
        **.lower()** |  将字符串中的所有大写字母转换为小写字母
        .swapcase() |  将字符串str中的大小写字母同时进行互换。即字符串中大写字母转换为小写字母，小写字母转换为大写字母。
        **.title()** | 返回一个满足 标题格式 的字符串。即所有英文单词**首字母大写**，其余英文字母小写
        .capitalize() | 将字符串的第一个字母变成大写，其余字母变为小写
        .expandtabs() | 把字符串中的 tab 符号 (\t) 转化为空格 (\t 默认空格数为 8 )
        .casefold() | 将字符串中的所有大写字母转换为小写字母。也可以将 **非英文语言** 中的大写转化为小写
        
    + 字符串判断
        
        方法 | 描述
        :---: | :---:
        .isalnum() | 检测字符串是否由字母和数字组成。str 中至少有一个字符且所有字符都是字母或数字则返回 True，否则返回 False
        .isalpha() | 检测字符串是否只由字母组成。字符串中至少有一个字符且所有字符都是字母则返回 True，否则返回 False
        .isdigit() | 检测字符串是否只由数字组成。字符串中至少有一个字符且所有字符都是数字则返回 True，否则返回 False (① 也是数字)
        .isupper() | 检测字符串中字母是否全由大写组成。(可包含非字母字符)，返回值为 布尔值
        .islower() | 检测字符串中字母是否全由小写组成。(可包含非字母字符)，返回值为 布尔值
        .istitle() | 检测判断字符串中所有首字母是否为大写，且其他字母是否为小写，字符串中可以存在其他非字母的字符。若字符串中所有单词的首字母大写，其他字母小写返回 True 否则返回 False
        .isspace() | 检测字符串是否由空格组成。若只包含空格返回 True ，否则返回 False
        .endswith(suffix[, start[, end]]) | 返回值为 布尔值，如果以指定的后缀结尾，则返回True，否则返回False。start 为开始位置，end为结束位置，默认为整个字符串 (Python内置)
        .startswith(prefix[, start[, end]]) | 返回值为 布尔值，如果以指定的字符串开头，则返回True，否则返回False。start 为开始位置，end为结束位置，默认为整个字符串 (Python内置)
        .split() | 按照指定"元素"分割，maxsplit: 默认将指定所有内容进行分割，可以指定 maxsplit 值 (maxsplit值为 1 只按照第一个指定内容分割，后面不分个割)

+ 字符串编码
    
    + encode() : 编码，以指定的编码格式编码字符串，默认为 "utf-8"，将字符串转换为字节码 str -> byte
        + 语法：str.encode(encoding="utf-8", errors='strict')
            + encoding: 可选参数、默认 "utf-8"，常用类型 utf-8、gb2312、cp936、gbk等
            + errors:   可选参数，设置不同错误的处理方案。默认为 "strict"，意为编码错误引起一个 UnicodeEncodeError。其他可能为 'ignore'、'replace'、'xmlcharrefreplace' 以及通过 codecs.register_error() 注册其他的值
    + decode() : 解码，以 encoding 指定的编码格式解码字符串，默认编码为字符串编码，将字节码转换为字符串 byte -> str
        + 语法：str.decode(encoding="utf-8", errors='strict')
            + encoding: 可选参数、默认 "utf-8"，常用类型 utf-8、gb2312、cp936、gbk等
            + errors:   可选参数，设置不同错误的处理方案。默认为 "strict"，意为编码错误引起一个 UnicodeEncodeError。其他可能为 'ignore'、'replace'、'xmlcharrefreplace' 以及通过 codecs.register_error() 注册其他的值

+ 转义字符 (改变原有字符意义)

    转义 | 描述
    :---: | :---:
    \\ | 产生一个 反斜杠 (\) 符号
    \' | 产生一个 单引号 (')
    \" | 产生一个 双引号 (")
    \n | 换行
    \t | 横向制表符 (tab) 占 8 个字符
    \newline | 连续 (当一行代码太长时使用)
    \other | 不转义，保留原有字符
    
+ 元字符串
    + 在任意字符串前添加字母 r 或者 R ，当前字符串所有转义字符都不会进行转义。(正则表达式中常见格式)