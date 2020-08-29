# 程序异常

+ 异常
    + 在语法正确的前提下，再运行程序报错
    + 异常会导致程序直接崩溃退出，不向后执行，所以对于可能出现的异常要进行处理，保障出错后程序仍能正常运行
    + 编写的代码要有容错性
        + 允许用户操作时出现的错误
        
+ 异常捕获
    + 捕获单个异常
        + 基本语法
            ```
          try:
            ...代码1...
            ...代码2...
          except 异常类型:
            ...处理异常代码...
          ```
            + 从上到下运行，遇到错误不执行之后代码，执行 except 中的代码，如果没错，except 中代码不执行
            + 如果异常类型与捕获异常类型不同，则无法捕获，程序崩溃
                ```
              num1 = int(input("1 :"))
              num2 = int(input("2 :"))
            
              try:
                  print("start")
                  print(num1/num2)
                  print("end")
              except ZeroDivisionError as error:
                  print(error, "被除数不能为 0")
              print("结束")
              """
              1 :3
              2 :0
              start
              division by zero 被除数不能为 0
              结束
              """
              ```
    + 捕获多个异常
        + 语法
    
            + 多分支结构 : 对于错误从上到下依次捕获
               ```
              try:
                执行的的代码
              except 异常类型:
                捕获异常1
              except 异常类型:
                捕获异常
              ...
              ```
            + 元组结构 : 无论发生什么异常，统一处理
                ```
              try:
                执行的代码
              except(异常类型1,异常类型2,...):
                捕获异常
              ```
    + 捕获所有异常
        + 语法
            + except 后不加异常类型，可以捕获所有异常类型
                ```
              try:
                ...代码...
              except:
                捕获异常
              ```
            + Except 是所有异常的父异常, try 中所有异常都能捕获
                ```
              try:
                ...代码...
              except Exception:
                 捕获异常
              ```
    + 获取异常信息描述
        + 语法 (变量名也可以叫异常的对象, 一般使用 e 表示，e 对象中包含异常信息的描述，可以做不同处理)
            ```
          try:
            ...代码...
          except 异常类型 as 变量名 :
            执行异常...
          ```
    + else 格式
        + 语法 (try 中没有抛出异常则执行 else 中的代码, try 出了异常便不执行)
           ```
          try:
            ...代码...
          except 异常类型1 as 变量名:
            执行异常...
          else:
            ...代码...
          ```
    + try ... finally
        + 语法 (try 是否抛出异常, finally 中代码都执行)
            ```
          try:
            ...代码...
          except 异常类型1 as 变量名:
            执行异常...
          finally:
            ...代码...
          ```
+ 触发异常

    + 抛出系统异常
    
        格式 | 描述
        :---: | :---:
        raise 异常类型("描述信息") | 程序执行到 raise 时, 会自动触发异常,结束程序
        
        + 实例
            ```python
          import string
            
          while True:
              name = input("请输入你的英文名字 (不得少于三个单词):")
            
              try:
                  if len(name) == len([i for i in name if i in string.ascii_letters]):
                      if len(name) > 3:
                          print(f"{name}")
                      else:
                          raise Exception("名称少于三个单词，请重新输入!")
                  else:
                      raise Exception("名称不合规范!")
              except Exception as e:
                print(e)
            ```
    
    + 抛出自定义异常
        + 继承、重写 Exception 类
            ```python
          import string
            
            
          class MyError(Exception):
              def __init__(self, name):
                  self.name = name
            
              def __str__(self):
                  if len(name) != len([i for i in name if i in string.ascii_letters]):
                      return f'字符串不合法, 含有非法字符\t{", ".join([i for i in name if i not in string.ascii_letters])}'
            
            
          while True:
              name = input("请输入你的英文名字 (不得少于三个单词):")
            
              try:
                  if len(name) == len([i for i in name if i in string.ascii_letters]):
                      if len(name) > 3:
                          print(f"{name}")
                      else:
                          raise Exception("名称少于三个单词，请重新输入!")
                  else:
                      raise MyError(name)
              except Exception as e:
                  print(e)
            ```
  
# pygame 坦克大战, 面向对象测试

+ pygame
    +  
