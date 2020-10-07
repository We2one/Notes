```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-02 21:50:33
   Modified by: Gentleman.Hu
   Modified time: 2020-10-03 10:30:36
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Java 函数式编程

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

