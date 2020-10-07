```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-07 12:47:15
   Modified by: Gentleman.Hu
   Modified time: 2020-10-07 14:03:01
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: 一些RxJava的基础
 ```

## RxJava概览

> [官方文档](http://reactivex.io/documentation/observable.html')
> [QuickStart](https://www.tutorialspoint.com/rxjava/rxjava_quick_guide.htm)
> [ObserverDesign](https://www.vogella.com/tutorials/DesignPatternObserver/article.html#:~:text=The%20observer%20pattern%20defines%20a,are%20called%20observers%20or%20listeners.)

RxJava是专门为Java编写的一个拓展.它就是用Java实现了[`ReactiveX`](#reactive)项目.
特点(characteristics)

- 应用观察者模式(Observer Pattern)
- 数据/事件序列
- 可用运算符以声明方式组合序列
- 内置针对线程,同步,线程安全,并发等的数据结构

<details id="reactive">
<summary id="nice"><span style="color:blue">ReactiveX</span></summary>

- ReactiveX
  - ReactiveX is a project which aims to provide reactive programming concept to various programming languages. Reactive Programming refers to the scenario where program reacts as and when data appears. It is a event based programming concept and events can propagate to registers observers.

  - As per the Reactive, they have combined the best of Observer pattern, Iterator pattern and functional pattern.

  - The Observer pattern done right. ReactiveX is a combination of the best ideas from the Observer pattern, the Iterator pattern, and functional programming.
  
- Functional Programming
Functional programming revolves around building the software using pure functions. A pure function do not depends upon previous state and always returns the same result for the same parameters passed. Pure functions helps avoiding problems associated with shared objects, mutable data and side effects often prevalent in multi-threading environments.

- Reactive Programming
Reactive programming refers to event driven programming where data streams comes in asynchronous fashion and get processed when they are arrived.

- Functional Reactive Programming
RxJava implements both the concepts together, where data of streams changes over time and consumer function reacts accordingly.

- The Reactive Manifesto
  - Reactive Manifesto is an on-line document stating the high standard of application software systems. As per the manifesto, following are the key attributes of a reactive software −

  - Responsive − Should always respond in a timely fashion.

  - Message Driven − Should use asynchronous message-passing between components so that they maintain loose coupling.

  - Elastic − Should stay responsive even under high load.

  - Resilient − Should stay responsive even if any component(s) fail.
  
- Key components of RxJava
RxJava have two key components: Observables and Observer.

  - Observable − It represents an object similar to Stream which can emit zero or more data, can send error message, whose speed can be controlled while emitting a set of data, can send finite as well as infinite data.

  - Observer − It subscribes to Observable's data of sequence and reacts per item of the observables. Observers are notified whenever Observable emits a data. An Observer handles data one by one.

 An observer is never notified if items are not present or a callback is not returned for a previous item.

</details>

## HelloWorld

```java
import io.reactivex.Flowable;
public class HelloWorld{
	public static void main(String[] args) {
		Flowbale.just("Hello World")
			.subscribe(System.out::println);
 }
}
```

## RxJava的观察者模式原理

![](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/20201007133613.gif)

### 基本组件

#### Observables

- Observable提供数据给Observer(Subscriber)监听
- Observable可以有任意多个子项目
- Observable也可以只给信号而不提供任何项目
- Observable可以成功终止
- Observable或许永远不会终止,比如按钮可以一直点击.
- Observable会抛出异常

#### Subscriber

- Observable可以有任意多个Observer(Subscriber)
- 当Observable发出项目,每个Subscriber的`onNext()`方法都会触发(invoked).
- 当Observable发出的项目完成时,每个Subscriber的`onComplete`方法都会触发.
- 如果Observable错误(error),每个Subscriber的`onError()`方法都会触发.

### 组件创建

- 下边是创建Observables的基本类

  - `Flowable` − 0..N flows, Emits 0 or n items. Supports Reactive-Streams and back-pressure.

  - `Observable` − 0..N flows ,but no back-pressure.

  - `Single` − 1 item or error. Can be treated as a reactive version of method call.

  - `Completable` − No item emitted. Used as a signal for completion or error. Can be treated as a reactive version of Runnable.

  - `MayBe` − Either No item or 1 item emitted. Can be treated as a reactive version of Optional.

- 下边是一些从方法创建Observables对象的方便方法
  - `just(T item)` − Returns an Observable that signals the given (constant reference) item and then completes.

  - `fromIterable(Iterable source)` − Converts an Iterable sequence into an ObservableSource that emits the items in the sequence.

  - `fromArray(T... items)` − Converts an Array into an ObservableSource that emits the items in the Array.

  - `fromCallable(Callable supplier)` − Returns an Observable that, when an observer subscribes to it, invokes a function you specify and then emits the value returned from that function.

  - `fromFuture(Future future)` − Converts a Future into an ObservableSource.

  - `interval(long initialDelay, long period, TimeUnit unit)` − Returns an Observable that emits a 0L after the initialDelay and ever increasing numbers after each period of time thereafter.

---

break on 2020-10-07 14:02:56

---
continue
> [Single Observable](https://www.tutorialspoint.com/rxjava/rxjava_quick_guide.htm)