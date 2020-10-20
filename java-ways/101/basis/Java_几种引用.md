```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-18 22:44:42
   Modified by: Gentleman.Hu
   Modified time: 2020-10-20 16:53:41
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Java中几种引用用例和区别
 ```

## Java中引用

> [source](https://stackoverflow.com/a/23519721)

- 强引用(Strong Reference)

- 弱引用(Weak Reference)
  - 软引用(Soft Reference)
  - 虚引用(Phantom Reference)

## 强引用(Strong Reference)

- 默认情况下,创建任意对象都是StrongReference

> StringBuilder builder = new StringBuilder();

当这个对象被强引用变量引用时,它处于可达状态,不可能被垃圾回收.(造成内存泄露主要原因之一)

## 弱引用(Weak Reference)

> WeakReference weak = new WeakReference(builder);

只要垃圾回收运行,不管JVM是否内存充足,就回收它.

## 软引用(Soft Reference)

> SoftReference soft = new SoftReference(builder);

当内存足够时,不会被回收.当不足时候,会回收.(常用于内存敏感程序)

## 虚引用(Phantom Reference)

> PhantomReference phantom = new PhantomReference(builder);

虚引用,不能单独使用,需要和[引用队列](https://www.baeldung.com/java-phantom-reference)结合使用.一般用于跟踪对象被垃圾回收的状态. 

## 其他,待补充