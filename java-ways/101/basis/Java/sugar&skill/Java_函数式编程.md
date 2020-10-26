```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-02 21:50:33
   Modified by: Gentleman.Hu
   Modified time: 2020-10-18 21:56:22
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Java 函数式编程

> [youtube_functional_programming](https://www.youtube.com/watch?v=rPSL1alFIjI)
> [source_github](https://github.com/amigoscode/java-functional-programming)

```yaml
Skills covered:
• Java
• Functional Programming
• Combinator Design Pattern
• Optionals
• Streams
```

### Lambda表达式

- 格式: `(形参)->{代码块}`
  - `()`,`(String x)`,etc,形参
  - `->` :箭头
  - 代码块: {}具体实现
- 省略模式
  - 无参数有返回值:`()-> "hello"` ,`() -> String.valueOf(1234)`;
  - 只有一个参数: 可省略括号,`x->x*3`;
- 上下文推断可省略参数类型声明;必须有且只有一个抽象方法.
  
### 接口特性

- 常量: `public static final`
- 抽象方法: `public abstract`
- 默认方法: `default T method(){some code }`
- 静态方法: `static T method(){some code}`
- 私有方法: `private static,private T method(){some code}`

### 方法引用

- 方法引用符号: `::`
- 上下文推断: 跟lambda类似,编译器同样进行上下文推断
- 引用方法: 
  - 静态方法: `System.out::print` 类名::静态方法
  - 实例方法: `"HelloWorld"::toUpperCase`  对象::成员方法
- 类的实例方法
  - 创建类的新对象: `String::new` 类名::new
  - `String::substring` 类名::成员方法

### 函数式接口

> 有且只有一个抽象方法的接口

- 可作为方法参数,也可作为返回值
  `public Function<Integer,String> reFunction (Function<String,Integer> function){ return ...}`
- Supplier
  - T get() 返回指定的泛型类型
  - 通过指定lambda表达式具体实现
- Consumer
  - void accept(T t)对指定的泛型参数消费,进行处理
  - andThen(Consumer after)返回一个组合式Consumer,然后执行after操作
- Predicate
  - boolean test(T t)谓词判断,通过指定lambda表达式,测试参数是否满足某个特点进行筛选
  - default Predicate<T> negate() ,返回逻辑否,对应逻辑非
  - default Predicate<T> and(Predicate other)返回一个组合判断,对应短路与
  - default Predicate<T> or(Predicate other)返回一个组合判断,对应短路或
- Function
  - Function<T,R> 通常用于转换,给定T类型,返回R类型.
  - R apply(T t)
  - default <V> Function andThen(Function after)返回一个组合函数,先将函数应用输入,然后将after函数应用与结果

### Stream流操作

> 流水线式的处理数据

- 生产流的方式
  - Collection集合
  - Map集合
  - 数组
- 中间操作
  - Stream<T> filter(Predicate predicate)利用谓词接口进行过滤筛选.
  - Stream<T> limit(long n)截断流中数据,n为返回个数
  - Stream<T> skip(long n)指定跳过n个数据,返回剩下的流
  - static <T> Stream<T> concat(Stream a,Stream b)组合两个流成一个流
  - Stream<T> distinct()返回流中独特的元素组成的流
  - Stream<T> sorted()返回自然排序后的流
  - Stream<T> sorted(Comparator comparator)返回经过自定义比较器的排序流
  - <R> Stream<R> map(Function mapper)返回经过指定函数处理的结果的流
  - IntStream mapToInt(ToIntFunction mapper)返回IntStream,源流映射成Int流
- 终结操作
  - 一般操作
    - void forEach(Consumer action)指定消费器,对每个流中元素进行消费
    - long count()返回流中元素个数
  - 收集操作
    - R collect(Collector collector)把结果收集到集合中
    - Collectors
      - public static <T> Collector toList() 收集流到List集合中
      - public static <T> Collector toSet() 收集流得到Set集合中
      - public static Collector toMap(Function keyMapper,Function valueMapper) 收集元素到Map集合中
      - 此工具类返回的都是包含所有元素的Collector

#### 实例操作Stream

- Collection生成Stream

```java
List<String> list = new ArrayList<String>();
Stream<String> listStream = list.stream();

Set<String> set = new HashSet<String>();
Stream<String> setStream = set.stream();
```

- Map系列生成Stream
  
```java
Map<String,Integer> map = new HashMap<String,Integer>();
Stream<String> keyStream = map.keySet().stream();
Stream<Integer> valueStream = map.values().stream();
Stream<Map.Entry<String,Integer>> entryStream = map.entrySet().stream();
```

- 数组生成Stream

```java
String[] strArray = {"hell","world","niubi"};
Stream<String> strStream = Stream.of(strArray);
Stream<String> okStream = Stream.of("jjj","hahha","iii");
```

### Optional

> [quick_guide](https://www.tutorialspoint.com/java8/java8_optional_class.htm)
> [official_doc](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)

Optional is a container object used to contain not-null objects. Optional object is used to represent null with absent value. This class has various utility methods to facilitate code to handle values as 'available' or 'not available' instead of checking null values. It is introduced in Java 8 and is similar to what Optional is in Guava.

- Class Declaration
  > Following is the declaration for `java.util.Optional<T>` class - 
  `public final class Optional<T> extends Object`
  
Class Methods

| Sr.No. |                                                                                                 Method & Description                                                                                                 |
| ------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| 1      |                                                                        **static <T> Optional<T> empty()**Returns an empty Optional instance.                                                                         |
| 2      |                                                            **boolean equals(Object obj)**Indicates whether some other object is "equal to" this Optional.                                                            |
| 3      |       **Optional<T> filter(Predicate<? super <T> predicate)**If a value is present and the value matches a given predicate, it returns an Optional describing the value, otherwise returns an empty Optional.        |
| 4      | **<U> Optional<U> flatMap(Function<? super T,Optional<U>> mapper)**If a value is present, it applies the provided Optional-bearing mapping function to it, returns that result, otherwise returns an empty Optional. |
| 5      |                                                    **T get()**If a value is present in this Optional, returns the value, otherwise throws NoSuchElementException.                                                    |
| 6      |                                                   **int hashCode()**Returns the hash code value of the present value, if any, or 0 (zero) if no value is present.                                                    |
| 7      |                                   **void ifPresent(Consumer<? super T> consumer)**If a value is present, it invokes the specified consumer with the value, otherwise does nothing.                                   |
| 8      |                                                                  **boolean isPresent()**Returns true if there is a value present, otherwise false.                                                                   |
| 9      |     **<U>Optional<U> map(Function<? super T,? extends U> mapper)**If a value is present, applies the provided mapping function to it, and if the result is non-null, returns an Optional describing the result.      |
| 10     |                                                         **static <T> Optional<T> of(T value)**Returns an Optional with the specified present non-null value.                                                         |
| 11     |                                 **static <T> Optional<T> ofNullable(T value)**Returns an Optional describing the specified value, if non-null, otherwise returns an empty Optional.                                  |
| 12     |                                                                     **T orElse(T other)**Returns the value if present, otherwise returns other.                                                                      |
| 13     |                                     **T orElseGet(Supplier<? extends T> other)**Returns the value if present, otherwise invokes other and returns the result of that invocation.                                     |
| 14     |            **<X extends Throwable> T orElseThrow(Supplier<? extends X> exceptionSupplier)**Returns the contained value, if present, otherwise throws an exception to be created by the provided supplier.            |
| 15     |                                                       **String toString()**Returns a non-empty string representation of this Optional suitable for debugging.                                                        |

- Optional Example

```java
import java.util.Optional;

public class Test{
  public static void main(String[] args){
      Test test = new Test();
      Integer value1 = null;
      Integer value2 = new Integer(10);

      //Optional.ofNullable - allows passed parameter to be null.
      Optional<Integer> a = Optional.ofNullable(value1);

      //Optional.of - throws NullPointerException if passed parameter is null
      Optional<Integer> b = Optional.of(value2);
      System.out.println(test.sum(a,b));
      
  }

  public Integer sum(Optional<Integer> a, Optional<Integer> b){
    //Optional.isPresent - checks the value is present or not

    System.out.println("First parameter is present: "+ a.isPresent());
    System.out.println("Second parameter is present: "+ b.isPresent());
    
    //Optional.orElse - returns the value if present otherwise returns
    //the default value passed.
    Integer value1 = a.orElse(new Integer(0));

    //Optional.get - gets the value, value should be present
    Integer value2 = b.get();
    return value1 + value2;
  }
}
```

output:

```java
First parameter is present: false
Second parameter is present: true
10
```

### CallBack in Java

- Synchronous Callback
  - block and wait.
  
```java
interface OnEventListener{
  void onEvent();
}

class Consumer{
  private OnEventListener listener;

  public Consumer(OnEventListener listener){
    this.listener = listener;
  }

  public void registListener(OnEventListener listener) {
     this.listener = listener;
     }
  public void doOnEvent(){
    // callback before synchronous task
    if(this.listener!=null){
      // invoke callback of another class.
      listener.onEvent();
    }
  }
}
class Another implements OnEventListener{
  @Override
  public void onEvent(){
    System.out.println("callback from Another");
  }
}

class Main{
  public static void main(String[] args) {
    Consumer conn = new Consumer();
    conn.registListener(()->System.out.println("callback from lambda));
    conn.doOnEvent();
  }
}
```

- Asynchronous Callback
  - Non-Block and continue.

```java
interface OnEventListener{
  void onEvent();
}

class Consumer{
  private OnEventListener listener;

  public Consumer(OnEventListener listener){
    this.listener = listener;
  }

  public void registListener(OnEventListener listener) {
     this.listener = listener;
     }
  public void doOnEvent(){
    // callback before synchronous task
    if(this.listener!=null){
      // invoke callback of another class. asynchronous
      new Thread(()->listener.onEvent()).start();
    }
  }
}
class Another implements OnEventListener{
  @Override
  public void onEvent(){
    System.out.println("callback from Another");
  }
}

class Main{
  public static void main(String[] args) {
    Consumer conn = new Consumer();
    conn.registListener(()->System.out.println("callback from lambda););
    conn.doOnEvent();
  }
}
```

#### when to use synchronous ,asynchronous

Synchronous Callback : Any process having multiple tasks where the tasks must be executed in sequence and doesn’t occupy much time should use synchronous Callbacks.
For example : You’re in a movie queue for ticket you can’t get one until everyone in front of you gets one.

Asynchronous Callback : When the tasks are not dependent on each other and may take some time for execution we should use Asynchronous callbacks.
For example : When you order your food other people can also order their food in the restaurant. They don’t have to wait for your order to finish, If you’re downloading a song from internet, Getting an API response.

## References

[javaworld](https://www.javaworld.com/article/2077462/learn-java/java-tip-10–implement-callback-routines-in-java.html)

[wiki](https://en.wikipedia.org/wiki/Callback_(computer_programming))
