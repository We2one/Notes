```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 22:33:03
   Modified by: Gentleman.Hu
   Modified time: 2020-10-26 22:13:55
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: ThreadLocal介绍和一些用例
 ```

## ThreadLocal

- 介绍

`ThreadLocal` in Java in another way to achieve [Thread-safe](https://javarevisited.blogspot.com/2012/01/how-to-write-thread-safe-code-in-java.html). afart from writing immutable classes. If you have been writing muti-threaded or concurrent code in Java then you must be familiar with the cost of synchronization or locking which can greatly affect the Scalability of application, but there is no choice other than synchronizing if you are sharing objects between
multiple threads. `ThreadLocal` in Java is a different way to achieve thread-safety, it doesn't address synchronization requirement, instead, it eliminates sharing by providing explicitly copy of object to each thread. Since Object is no more shared there is no requirement of Synchronization which can improve scalability and performance of the application.

## Samples

## Resources

- [ThreadLocal](https://javarevisited.blogspot.com/2012/05/how-to-use-threadlocal-in-java-benefits.html#ixzz2XltgbHTK)
- [GeeksforGeeks_ThreadLocal](https://www.geeksforgeeks.org/java-lang-threadlocal-class-java/)
