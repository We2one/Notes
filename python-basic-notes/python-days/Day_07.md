# Day_07

### 函数 `一段具有与特定功能的代码段`

+ 函数的作用

+ 函数的优势
    
+ 方便使用
    
+ 函数的声明和调用
    + 格式 
        ```
      def 函数名(形参):
        """注释说明"""
        函数中代码
        [return]
      ```
        + 函数名: 标识符 可以自定义，遵循标识符的命名规则
        + () : 固定语法
        + 注释 : 规范要求要写函数的注释说明 (函数的功能、返回值、参数)
    + 调用函数格式 : 函数名([实参])

+ 函数的参数
    + **位置参数** (实参和形参一一对应)
        + **形参**: 定义函数时，函数能用到的参数，
        + **实参**: 调用函数时，传入的参数
    + **关键字参数** : 执行函数传参时通过 形参名 = 实参 传递参数，不受参数位置影响，根据关键字一一对应传参
    + **默认值参数** : 形参可以设置默认值 (需要写在参数最后)，在没有传参时默认参数的值
    + **可变参数** (*args, **kwargs)
        + `*args` : 以元组类型传参 (非关键字收集参数)
            + 调用函数时，将传递多余的参数进行收集，传到 arags 中
            + 形参顺序 : 位置参数、非关键字收集参数、关键字收集参数、默认值参数
        + `**kwargs` : 以字典形式传参  (关键字收集参数)
            + 将多余的关键字参数，收集到 kwargs 参数以字典形式存储
            + 形参顺序 : 位置参数、元组参数、关键字参数、默认值参数、字典参数

+ 函数的返回值
    + return 返回函数结果、结束函数
    + 没有返回值的函数，默认返回 None
    + return 后将多个元组以逗号隔开，返回一个元组

+ 函数的相互调用
    + 函数不调用不执行、先声明后调用
    + 函数名([实参])
    + **可以调用自己 (递归函数)**

+ 递归函数 : 函数自己调用自己
    + 实质 : **压栈操作 (先进后出)**
        + 函数调用时,在栈中压入栈帧,当函数执行结束,栈帧去除
        + 函数可以进行多次多调用,调用次数没有限制, **递归会导致内存溢出**
    + 缺点 : 消耗内存,效率比较低
    + 优点 : 逻辑直观