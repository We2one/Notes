
## 多继承

+ 一个子类继承多个父类, 多继承模式下继承熟顺序,使用了广度优先的查询原则
    ```python
  class F:
      def say(self):
          print("Hello F")
    
    
  class A(F):
     def say(self):
        super().say()
        print("Hello A")
    
    
  class B(F):
      def say(self):
         super().say()
         print("Hello B")
    
    
  class C(A, B):
      def say(self):
          super().say()
          print("Hello C")
    
    
  c = C()
  print(C.mro())
  c.say()
  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.F'>, <class 'object'>]
  # Hello F
  # Hello B
  # Hello A
  # Hello C
    ```

## 属性(类属性和实例属性)

+ 属性是描述对象的特征的，通常对象的特征都是每个对象自己独有的数据，但是某些情况下也会出现一些对象 共有的数据
    + 属性声明语法
        + 实例属性的声明与访问
            + 声明 : 包含在类型中的 __init__() 初始化方法中，使用 self 关键字将属性绑定到当前对象上
                ```
              def __init__(self, name):
                  """实例属性"""
                  self.name = name
              ```
            + 访问 : 实例属性在类型内部可以通过 self.实例属性名 关键字引用，在类型外部可以通过 对象的引用变量 (实例化类名.实例属性名) 访问和修改
        + 类属性的声明和访问
            + 声明 : 类属性声明在类型的内部，方法的外部
                ```
              class Article:
                  # 类属性声明
                  content_max_size = 120
              ```
            + 访问 : 类属性能被当前类型的所有对象访问，或者能直接通过类名称访问
                ```
              # 类内部 直接访问
              content_max_size
              # 类外部 实例化类名.类属性名
              airtitle = Airtitlr()
              airtitle.content_max_size
              # 类外部 类名.类属性名
              Airticle.content_max_size
              ```
            + 修改 : 类属性不能被对象引用变量所修改，只能在类名称处修改
            + 属性拓展 : 类型外部，通过语法“ **变量.属性变量** ”直接添加的属性，是当前对象独有 ( 同类型其他对象没有 ) 的属性 (不推荐使用)

## 静态方法、类方法和实例方法 (本质是一个函数，用于描述对象的行为)

+ 实例方法 : 声明在类型内部的普通方法，第一个参数是当前对象本身；实例方法在执行过程中可以访问当前对象的所有属性 / 方法、当前类型的属性 / 方法等；实例方法在使用过程中只能被对象的变量调用执行

+ 类方法 : 声明在类内部，方法上使用装饰器 @classmethod 声明的方法，第一个参数是当前类本身，约定俗 成使用 cls 表示；类方法只能访问当前类型的类属性，不能访问任何对象的实例属性；类方法能被当前类型调用，也能被实例对象调用

+ 静态方法 : 声明在类的内部 (本质上是被统一管理在类中的函数) ，方法上使用装饰器 @staticmethod 声明的方法；静态方法是独立的方法，不能访问类的任何信息；静态方法可以被类名称直接调用，也可以被对象的变量调用执行



## 魔术方法

1. 构造和初始化

    魔术方法|描述
    :---:|:---:
    \_\_new__(cls, *args, **kwargs) | 创建对象的魔法方法
    \_\_init__(self) | 初始化对象数据的方法
    \_\_del__(self) | 析构,当对象被销毁执行
    \_\_call__(self) | 当对象被当做函数调用时执行

2. 比较运算符
    
    魔术方法|描述
    :---:|:---:
    \_\_eq__(self, other) | 定义符号 == 的操作 (self 当前对象, other 其他对象)
    \_\_ne__(self, other) | 定义符号 != 的操作 (self 当前对象, other 其他对象)
    \_\_lt__(self, other) | 定义符号 < 的操作 (self 当前对象, other 其他对象)
    \_\_gt__(self, other) | 定义符号 > 的操作 (self 当前对象, other 其他对象)
    \_\_le__(self, other) | 定义符号 <= 的操作 (self 当前对象, other 其他对象)
    \_\_ge__(self, other) | 定义符号 >= 的操作 (self 当前对象, other 其他对象)
    
3. 一元运算符
    
    魔术方法|描述
    :---:|:---:
    \_\_pos__(self) | 定义符号 + 的操作
    \_\_neg__(self) | 定义符号 - 的操作
    \_\_invert__(self) | 定义符号 ~ 取反 的操作

4. 算术运算符

    魔术方法|描述
    :---:|:---:
    \_\_add__(self, other) | 定义符号 + 的操作
    \_\_sub__(self, other) | 定义符号 - 的操作
    \_\_mul__(self, other) | 定义符号 * 的操作
    \_\_floordiv__(self, other) | 定义符号 // 的操作
    \_\_div__(self, other) | 定义符号 / 的操作
    \_\_pow__(self, other) |  定义符号 ** 的操作
    
5. 增量复制

    魔术方法|描述
    :---:|:---:
    \_\_iadd__(self, other) | 定义符号+=的操作
    \_\_isub__(self, other) | 定义符号-=的操作
    \_\_imul__(self, other) | 定义符号*=的操作
    \_\_ifloordiv__(self, other) | 定义符号//=的操作
    \_\_idiv__(self, other) | 定义符号/=的操作
    \_\_ipow__(self, other) | 定义符号**=的操作


6. 类型转换

    魔术方法|描述
    :---:|:---:
    \_\_int__(self) | int()
    \_\_float__(self) | float()
    
7. 对象打印

    魔术方法|描述
    :---:|:---:
    \_\_str__(self) | 打印对象的属性信息，返回的必须是字符串，方便我们调试代码。
    \_\_repr__(self) | 输出展示对象，当对象被放在列表时，打印的信息repr__的结果是让解释器用的,转化为供解释器读取的形式
    \_\_doc__(self) | 查看当前对象说明文档
    \_\_dict__(self) | 将对象中的属性以字典的形式返回
    
8. 反射方法

    魔术方法|描述
    :---:|:---:
    hasattr(obj, name) | 判断是否包含名称为name的属性
    setattr(obj, name, value) | 给名称为name的属性设置value数据
    getattr(obj, name) | 获取名称为name的属性的具体数据
    delattr(obj, name) | 删除名称为name的属性



## 生成随机验证码

```python
import random
import string

s= random.sample(population=string.ascii_letters + string.digits, k=6)
print(''.join(s))
```