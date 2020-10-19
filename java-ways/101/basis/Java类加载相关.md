```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-12 15:51:03
   Modified by: Gentleman.Hu
   Modified time: 2020-10-12 20:00:30
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Java类加载器,反射,模块化
 ```

## Java类加载相关

## Java类加载器

> 将class文件读入内存,并为之创建一个`java.lang.Class`对象

![一般加载过程](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201012162619.png)

上图为一般加载过程,其中`加载,验证,准备,初始化和卸载`固定顺序,而`解析`不一定,有些情况在`初始化`阶段后开始,因为java支持运行时绑定.

- 类的连接
  - 验证阶段: 验证类内部结构是否正确,与其他类是否和谐一致
  - 准备阶段: 给类变量分配内存,并设置默认值
  - 解析阶段: 将符号引用转换为直接引用

- 类的初始化: 主要对对变量进行初始化.
  - 初始化步骤
    - 如果类未加载和连接,则先加载并连接
    - 如果`直接父类`未被初始化,则先初始化直接父类
    - 如果类中有初始化语句,则系统依次执行这些语句
    - 2步骤递归遵循1-3步骤
  
## Java反射

## 模块化

## References

- [JVM类加载过程](https://blog.csdn.net/zhaocuit/article/details/93038538)