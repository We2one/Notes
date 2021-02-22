## 反射方法 
+ 通过字符串的形式，操作对象相关的属性,多人开发中，每人负责一个或多个功能是，使用判断其他人是否完成，若完成，执行
  
    魔术方法|描述
    :---:|:---:
    hasattr(obj, name) | **判断**是否包含名称为name的属性 
    setattr(obj, name, value) | 给名称为name的属性**设置**value数据 
    getattr(obj, name) | **获取**名称为name的属性的具体数据 
    delattr(obj, name) | **删除**名称为name的属性 

+ 设计模式
    + 被反复使用的、多数人知晓的、代码设计经验 的总结，合理使用设计模式能有效解决很多问题
    + 软件开发六大原则
        + 开闭原则
        + 里氏代换原则
        + 依赖倒转原则
        + 接口隔离原则
        + 迪米特法则
        + 单一职责原则
    + 23 种常用设计模式
        + 创建型模式 : 一般是创建时使用
            + **单例模式**、**工厂方法模式**、抽象工厂模式、建造者模式、原型模式

                + **单例模式**
                    
                    + 需求: 项目中的某个类中处理项目中的公共数据，此时需要该类型创建的对象在任何其他对象访问时，任何时候任何方式获取到的都是同一个对象，以**保证数据的一致性**。
                    
                    + 实现: 单例模式
                        ```python
                      # 单例模式
                      class MyData:
                      	"""单例类"""
                      	__ins = None
                          
                          def __new__(cls, *args, **kwargs):
                      		if not cls.__ins:
                      			cls.__ins == object.__new__(cls)
                      		return cls.__ins
                      ```
                      
                      
                    
                + **工厂模式** : 将复杂对象的创建过程封装在方法的内部，提供了一个简单的创建方式给用户使用

                  ```python
                  # 用户只需要在工厂类中进行操作就可以对其他操作进行
                  class Factory:
                  
                  	def buy_vehicle(selfm, brand):
                  		if brand == 1:
                  			return Motorbike()
                          elif brand == 2:
                  			return Minibus()
                  		elif brand == 3:
                  			return Sedan()
                  		else:
                  			return "没有你需要的车"
                  ```

                  
        + 结构型模式 : 将问题结构化
            
            + 适配器模式、装饰模式、桥接模式、组合模式、享元模式、代理模式、外观模式
        + 行为型模式 : 将问题的算法和结构分离
            + 观察者模式、访问者模式、中介者模式、解释器模式、迭代器模式
            + 状态模式、命令模式、策略模式、备忘录模式、职责链模式、模板方法模式


## 文件 I/O、异常处理

1. 关于文件

    + 文件
        + 狭义 : 文本文件
        + 广义 : 超文本文件、图片、声音、超链接、视频
    
    + 二进制文件:二进制数据组成
        + 图片、音频、视频...

2. 读写文件简单操作
    
+ 读取文件  `open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)`
    
3. 文件权限 : 文件不存在会自动创建 (不会创建目录)

    读写方式  |  可否读写    |   若文件不存在   |  写入方式
    :---:   |   :---:     |     :---:     |   :---: 
    w      |    写入      |       创建    |       覆盖写入
    w+      |   读取+写入    |     创建      |    覆盖写入
    wb      |   二进制写入   |     创建      |     覆盖写入
    wb+     |   二进制读写   |     创建      |     覆盖写入
    r       |   读取        |     报错      |     不可写入
    r+      |   读取+写入    |     报错      |    覆盖写入
    rb      |   二进制读取   |     报错      |     不可写入
    rb+     |   二进制读写   |     报错      |    覆盖写入
    a       |   追加写入     |     创建      |     附加写入
    a+      |   读取+写入    |     创建      |     附加写入
    ab      |   二进制读写    |     创建     |     追加写入
    ab+     |   二进制追加   |       创建     |    追加读写

4. 文件操作

    + 读操作
        + **read(self, n: int = -1)**
            
            + 一次性读取文件全部内容 (大于 10G 会超出内存) ，反复调用read(size) 方法，size 是每次最多读取内容
                ```python
              file = open('../../../js_note.txt', encoding="utf-8")
              ret = file.read()
              # ret = file.read(2)
              print(ret)
              # ne
              file.close()
              """
              new 一个对象
              <b>   加粗
              "<br>"  换行
              <li></li>  加标注的换行
              """  
              ```
        + **readline(self, limit: int = -1) -> AnyStr**
            
            + 每次读取一行，自动换行并在每一行末尾添加(\n)
                ```python
              file = open('../../../js_note.txt', encoding="utf-8")
              ret = file.readline()
              print(len(ret))     # 读取长度
              print(ret)      # 读取内容
              print(file.readline())  # 读取下一行
              print(file.readline(3)) # 每行固定读取字符数
              file.close()
              """
                9
                new 一个对象
                
                <b>   加粗
                
                "<b
              """
              ```
        + **readlines(self, hint: int = -1) -> List[AnyStr]**
            
            + 一次性以行的形式读取文件所有内容，返回一个 list, 自动换行并在每一行末尾添加(\n), 使用时可遍历读取
                ```python
              file = open('../../../js_note.txt', encoding="utf-8")
              ret = file.readlines()
              print(ret)
              file.close()
              """
              ['new 一个对象\n', '<b>   加粗\n', '"<br>"  换行\n']
              """
              ```
        + 循环读取 
            + file 是一个可迭代的对象，可以通过循环每次读取一行内容
                ```python
              files = open('../../../js_note.txt', encoding="utf-8")
              for file in files:
              print(files)
              files.close()
              ```
        
    + 写操作

        + **write(self, s: AnyStr) -> int**
            
          ```python
          files = open("test.txt", mode='w')
          files.write("1111")
          files.write("222")
          files.close()
          """
          1111222
          """
          ```
        + **writelines(self, lines: List[AnyStr]) -> None**
            
            + 将 列表中数据一次性多行写入
                ```python
              files = open("test.txt", mode='w')
              arr = ["test\n", "first", "second"]
              files.writelines(arr)
              files.close()
              """
              test
              firstsecond
              """
              ```
        
    + CSV 文件读写 `import csv` (reader 和 write 定义了 CSV 文件的读写)
      ```
      >>> import csv
      >>> dir(csv)
      ['Dialect', 'DictReader', 'DictWriter', 'Error', 'OrderedDict', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtin
      s__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects',
      're', 'reader', 'register_dialect', 'unix_dialect', 'unregister_dialect', 'writer']
      ```
        + 写入 CSV 文件 (必须先创建 CSV 模块对应的 writer 对象，通过 writer 对象实现对文件内容读写)
          + **writer(fileobj, dialect='excel', *args, \*\*kwargs)**

          + **writerow(self, row: Iterable[Any]) -> Any**

          + **writerows(self, rows: Iterable[Iterable[Any]])**

            ```python
            import csv
              
            with open("data.csv", mode='w', encoding="utf-8", newline="") as f:
                # 获取 writer 对象
                writer = csv.writer(f)
                # 写入 CSV 标题
                writer.writerow(
                    ["id", "姓名", "性别", "年龄"]
                )
                writer.writerows(
                    [
                        [1, "小二", "男", 18],
                        [2, "张三", "男", 19],
                        [3, "赵红", "女", 24]
                    ]
                )
            """
            id,姓名,性别,年龄
            1,小二,男,18
            2,张三,男,19
            3,赵红,女,24
            """
            ```

            

        + 读取 CSV 文件 (主要通过 reader 对象完成，加载文件数据到 reader 下，然后按照固定格式读取)
          + **reader(iterable, dialect='excel', *args, **kwargs)**

            ```python
            import csv
              
            with open("data.csv", mode="r", encoding="utf-8") as f:
                render = csv.reader(f)
                for row in render:
                    print(row)
            """
            ['id', '姓名', '性别', '年龄']
            ['1', '小二', '男', '18']
            ['2', '张三', '男', '19']
            ['3', '赵红', '女', '24']
            """
            ```

            

5. with (with 方法对文件操作，会自动关闭文件，不必特意关闭)
    + 格式 
        ```
      with open("file_path", mode="", encoding="") as f:
            ...
      ```

6. 乱码   (python 读写文件时默认为 GBK 编码格式，pycharm 创建的文件默认 utf-8)
    + 格式 ---- 设置读取格式为 UTF-8
        ```
      with open("file_path", mode="", encoding="utf-8") as f:
            ...
      ```

7. os模块: `import os`

    1. **os.rename(src, dst)** : 重命名文件, src 旧文件或目录名, dst 新文件或目录名
          
       ```python
       import os
        
       os.rename("test.txt", "test1.txt")
       ```
       
    2. **os.remove(path)** : 删除文件, Path 为文件路径

          ```python
       import os
            
       os.remove("test1.txt")
       ```
      
    3. **os.mkdir(path)** : 创建目录 (文件夹)

          ```python
       import os
            
       os.mkdir("../text.txt")
       ```

    4. **os.makedirs(name, mode=0o777, exist_ok=False)** : 递归创建多级目录，如果已存在则报错 (exist_ok=True 不报错)
       
        ```python
       import os
       # 在当前路径下创建, 没有 . 是在根路径下创建
       os.makedirs("./test/test1/test2", )
       ```
       
    5. **os.rmdir(path)** : 删除一层空目录, 仅删除路径底端的那个文件夹
        
       ```python
    import os
       
       os.rmdir("./test/test1/test2")
       ```
       
    6. **os.removedirs(name)** : 删除多级空目录，删除路径上的空文件夹 (若目录为空，删除，向上递归，如果是空，删除，直至上层目录不为空)
        
       ```python
       import os
        
       os.removedirs('./test/test1')
       ```
       
    7. **os.getcwd()** : 获取当前所在目录
        
       ```python
       import os
        
       print(os.getcwd())
       # E:\python_study\思维导图\python_zhonggong_study\Day_13
       ```
       
    8. **os.listdir(path)** : 获取目录列表，当前目录下所有文件
        
       ```python
       import os
        
       print(os.listdir(os.getcwd()))
       # ['data.csv', 'Day_13.md', 'Day_13.py', 'read_csv.py', 'test1.txt', '~$笔记.docx', '文本读取.py', '笔记.docx']
    ```
        
    9. **os.chdir(path)** : 切换所在目录, 常用于改变工作目录，脚本执行目录等
        
       ```
       >>> import os
       >>> os.getcwd()
       'E:\\python_study'
       >>> os.chdir("./思维导图/python_zhonggong_study/Day_13")
       >>> os.getcwd()
       'E:\\python_study\\思维导图\\python_zhonggong_study\\Day_13'
       ```
       
    10.  **os.path.exists(path: Text) -> bool** : 判断文件或文件夹是否存在

        ```python
        import os
                
        print(os.path.exists("./test"))
        print(os.path.exists("test1.txt"))
        """
        False
        True
        """
        ```

        

    11.  **os.path.isfile(path: AnyPath) -> bool** : 判断是否为文件
         ```python
         import os
             
         print(os.path.isfile("test1.txt"))
         print(os.path.isfile("../Day_13"))
         """
         True
         False
         """
         ```

         

    12.  **os.path.isdir()** : 判断是否为目录
         ```python
         import os
             
         print(os.path.isdir("test1.txt"))
         print(os.path.isdir("../Day_13"))
         """
         False
         True
         """
         ```

         

    13.  **os.path.isabs(s: AnyPath) -> bool** : 判断是否为绝对路径
         ```python
         import os
             
         print(os.path.isabs("../Day_13"))
         # False
         ```

         

    14.  **os.path.abspath(path: AnyStr) -> AnyStr** : 获取绝对路径
         ```python
         import os
             
         print(os.path.abspath("test1.txt"))
         # E:\python_study\思维导图\python_zhonggong_study\Day_13\test1.txt
         ```

         

    15.  **os.path.basename(p: AnyStr) -> AnyStr** : 获取路径中的最后文件名部分

         ```python
         import os
             
         print(os.path.basename("E:\python_study\思维导图\python_zhonggong_study\Day_13\\test1.txt"))
         # test1.txt
         ```

         

    16.  **os.path.dirname(p: AnyStr) -> AnyStr** : 获取路径中的路径部分 (路径部分 : 路径中不包含文件名的部分) (获取父目录部分)
         ```python
         import os
             
         print(os.path.dirname("E:\python_study\思维导图\python_zhonggong_study\Day_13\\test1.txt"))
         # E:\python_study\思维导图\python_zhonggong_study\Day_13
         ```

         

8. 异常

9. 异常捕获

10. 触发异常