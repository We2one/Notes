# Day_09

## 函数

+ **闭包函数** : (在函数中定义的函数！通过闭包将不同功能模块分离)
    
    + 必要条件:
        + 函数的嵌套的定义
        + 内部函数使用外部函数的变量
        + 外部函数必须有返回值，返回内部函数名
    + 让函数内部的局部变量，在函数执行完成后，让外部能操作这个变量，延长函数内部局部变量的生命周期
    + 缺点: 占用内存高，存在内存溢出
    + 全局污染 : 全局变量大量出现容易导致重名现象，将独立的某个功能组件，单独在一个函数中实现，最终通过函数与函数之间局部变量的隔离，达到变量数据的隔离
    + 项目开发原则: 开闭原则
        + 对于程序拓展 -->  开放
        + 对程序修改  -->  关闭
    
+ **装饰器**
    
    + 语法: 必须是嵌套函数
        ```
      def 装饰器名称(fn):
        def wrapper(*args, **kwargs):
            目标函数执行前，要添加的代码功能
            res = fn(*args, **kwargs)
            目标函数执行后，要添加的代码
        return res
      return wrapper
      ```
      
    + 装饰器的应用 : 身份验证、授权验证、资源访问、日志记录、时间统计
        + 装饰器的添加
        
        + 目标函数的参数
            ```python
        def wrap(fn):
               def inner(name, age):
                   print(f"修改前年龄{age}")
                   age -= 2
                   fn(name, age)
               return inner
           
           @wrap      
           def func(name, age):
           	print(f"name: {name}, age: {age}")
           
           func("小明", 21)
           ```
           
           
        
        + 外函数接收功能
        + 内函数接收参数
        
        + 目标函数返回值
## 模块和包的引用方式
+ 模块的命名
    + 根据软件中不同功能命名
    + <span style="background: rgba(255, 255, 0, 0.7)">不能以中文命名</span>
    + <span style="background: rgba(255, 255, 0, 0.7)">不要与系统模块名冲突</span>

+ 模块中的代码
    + 文档注释 : 描述模块的版本、功能、开发者、修改日期
    
+ 引入模块
    + 绝对引入方式: `import 导入`
        + 导入三个路径
            1. 系统的 sys.path 路径
            2. 环境变量 PythonPATH 路径 [通常没有配置]
            3. 当前文件夹
        + 基本导入 [最常用]
            + 语法 : `import 模块`
        + 别名引入
            + 语法 : `import 模块 as 别名`
        + 直接引用模块内容 [不推荐]
            + 语法 : `from 模块 import 变量/函数`
    
    + 相对引入方式 (对于大型项目中，绝对路径引入可能出现错误，命名重复，相对引入更加精确)
        + 命令的路径表示
            + **. :** : 当前文件夹
            + **.. :** : 上一级文件夹
        + 模块的相对引入
            + 相对引入基本语法 [常用]
                + 当前文件下引用: `from . import 模块`
                + 相对引入别名语法 : `from . import 模块 as 别名`
                + 相对引入具体数据 [不推荐] : `from .模块 import 变量/函数`
                
## 包 
+ 包 (Package) : 程序包的简称，通过文件夹管理 Python 模块
    + 标准程序包 : 包含一个 \_\_init__.py 模块 (包声明模块,可以为空)                
    
    + 绝对引入
        + 绝对引入 [推荐]
            + 语法 : `from 包 import 具体模块`
        + 别名引入 [推荐]
            + 语法 : `from 包 import 具体模块 as 别名`
        + 直接引入 [了解] 自动执行指定包中 \_\_init__.py 文件
            + 语法 : `from . import 模块`
        + 偷懒引入
            + 语法 : `from 模块 import *`
    + 相对引入
        + 相对引入
            + `from . import 模块`
        + 相对引入 |
            + `from .包 import 模块`
    + \_\_name\_\_ (当前文件名) : 如果当前文件被当做模块使用，判断是否允许被执行
        `if __name__ == "main": 代码`
## 内置模块

+ **random 模块** (随机模块)
    
    + 随机小数
    
        + `random()` : 产生 0-1 之间的随机小数 
        + `uniform(a, b)` : 指定范围随机小数
        
    + 随机整数
        + `randint(a, b)` : 指定范围随机整数，包含开头结尾
          
        + `randrange(start, stop, [step])` : start, stop 范围内间隔指定步长 (step) 的整数，包含开头不包含结尾
          
        + 随机选择一个数据
            + `random.choice(lst)` : 随机返回可迭代序列的一个数据
                
              ```python
              # from random import choice
              import random
              lst = [1,2,3,4,5]
              random.choice(lst)
              # choice(lst)
          ```
            
    
    + 打乱
        
        + `random.shuffle(可迭代序列)` : 打乱列表顺序