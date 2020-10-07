```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-03 21:25:02
   Modified by: Gentleman.Hu
   Modified time: 2020-10-07 16:39:55
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Spring框架基础

### AOP 概念

- Target
- Proxy
- JoinPoint
- PointCut
- Advice
- Aspect
- Weaving

### XML配置AOP

写法
> `execution([修饰符] 返回值类型 包名.类名.方法名 (参数))`

- 修饰符可以省略
- 返回类型,包名,类名,方法名可以用`*`代替任意
- 包名和类名之间有一个点`.`代表当前包的类,两个点`..`代表当前包及其子包下的类.
- 参数列表可以使用两个点`..`表示任意个数,任意类型的参数列表

```java
execution(public void god.hu.aop.target.method())
execution(void god.hu.aop.target.*(..))
execution(* god.hu.aop.*.*(..))
execution(* god.hu.aop..*.*(..))
execution(* *..*.*(..))
```

使用xml和注解都可配置

注解开发aop步骤

1. 使用`@aspect`表明注解类
2. 使用`@before ,@after,etc`等通知注解标注通知方法
3. 在配置文件中配置aop自动代理

- 注解表

| 名称     | 表达              | 含义                   |
| -------- | ----------------- | ---------------------- |
| 前置     | `@Before`         | 切入点之前执行         |
| 后置     | `@AfterReturning` | 切入点之后执行         |
| 环绕     | `@Around`         | 之前和之后都执行       |
| 异常抛出 | `@AfterThrowing`  | 在抛出异常后执行       |
| 最终通知 | `@After`          | 都会执行，无论是否异常 |


---

break on 2020-10-07 16:39:27

---

continue at [OwnJavaWay](https://github.com/GentlemanHu/Java-Way/issues/15)