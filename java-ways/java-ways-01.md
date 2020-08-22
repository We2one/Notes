---
description: Way to be Java God.
---

# Java Ways 01

## `线程`并行，同一时刻

* To start the threads at `exactly` the same time \(at least as good as possible\), you can use a [CyclicBarrier](http://download.oracle.com/javase/1.5.0/docs/api/java/util/concurrent/CyclicBarrier.html) :
* Codes are as follows:

```java
// We want to start just 2 threads at the same time, but let's control that 
// timing from the main thread. That's why we have 3 "parties" instead of 2.
final CyclicBarrier gate = new CyclicBarrier(3);

Thread t1 = new Thread(){
    public void run(){
        gate.await();
        //do stuff    
    }};
Thread t2 = new Thread(){
    public void run(){
        gate.await();
        //do stuff    
    }};

t1.start();
t2.start();

// At this point, t1 and t2 are blocking on the gate. 
// Since we gave "3" as the argument, gate is not opened yet.
// Now if we block on the gate from the main thread, it will open
// and all threads will start to do stuff!

gate.await();
System.out.println("all threads started");
```

> This doesn't have to be a `CyclicBarrier`, you could also use a `CountDownLatch` or even a lock.

* This still can't make sure that they are started exactly at the same time on standard JVMs, but you can get pretty close. Getting pretty close is still useful when you do for example performance tests. E.g., if you are trying to measure throughput of a data structure with different number of threads hitting it, you want to use this kind of construct to get the most accurate result possible.

  On other platforms, starting threads exactly can be a very valid requirement btw.

`From` [StackOverFlow](https://stackoverflow.com/questions/3376586/how-to-start-two-threads-at-exactly-the-same-time)

