```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 11:05:42
   Modified by: Gentleman.Hu
   Modified time: 2020-10-17 15:08:46
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Concurrency problem,print in order
 ```

## Print in order

> [source](https://leetcode.com/problems/print-in-order/)

- Problem

Suppose we have a class;

```java
public class Foo{
	public void first() { print("first")}
	public void second() { print("second")}
	public void third() { print("third")}
}
```
The same instance of `Foo` will be passed to three dirrenent threads.
Thread A will call `first()`,thread B will call `second()`, thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`,and `third` is executed after `second()`. 

- Example

- 1.

```yaml
Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three thread being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(),and thread C calls third()."firstsecondthird" is the correct output.
```

- 2.

```yaml
Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second. "firstsecondthird" is the correct output.
```

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness(广泛的,全面的).


## Solution

### Java

- 1

> using `synchronized`

```java
class Foo{
	private boolean oneDone;
	private boolean twoDone;

	public Foo(){
		oneDone = false;
		twoDone = false;
	}
	
	public synchronized void first(Runnable printFirst) throws InterruptedException{
		printFirst.run();
		oneDone = true;
		notifyAll();
	}

	public synchronized void second(Runnable printSecond) throws InterruptedException{
		while(!oneDone){
			wait();
		}
		printSecond.run();
		twoDone = true;
		notifyAll();
	}

	public synchronized void third(Runnable printThird) throws InterruptedException{
		while(!tweDone){
			wait();
		}
		printThird.run();
	}
}
```

- 2.

> using lock on Object

```java
class Foo{
	private Object lock;
	private boolean oneDone;
	private boolean twoDone;

	public Foo(){ 
		lock = new Object();
		oneDone = false;
		twoDone = false;
	}

	public void first(Runnable printFirst) throws InterruptedException{
		synchronized(lock){
			printFirst.run();
			oneDone = true;
			lock.notifyAll();
		}
	}
	
	public void second(Runnable printSecond) throws InterruptedException{
		synchronized(lock){
			while(!oneDone){
				lock.wait();
			}
			printSecond.run();
			twoDone = true;
			lock.notifyAll();
		}
	}

	public void third(Runnable printThird) throws InterruptedException{
		synchronized(lock){ 
			while(!tweDone){
				lock.wait();
			}
			printThird.run();
		}
	}
}
```

- 3.
  
> using `Semaphore`

```java
public Foo{
	private Semaphore s2;// 
	private Semaphore s3;

	public Foo{
		s2 = new Semaphore(0);
		s3 = new Semaphore(0);
	}
	
	public void first(Runnable printFirst) throws InterruptedException{
		printFirst.run();
		s2.release();
	}
	
	public void second(Runnable printSecond) throws InterruptedException{
		s2.acquire();
		printSecond.run();
		s3.release();
	}

	public void third(Runnable printThird) throws InterruptedException{
		s3.acquire();
		printSecond.run();
	}
}
```

- 4.

> `condition variable`

```java
class Foo{
	private Lock lock;
	private boolean oneDone;
	private boolean twoDone;
	private Condition one;
	private Condition two;

	public Foo{
		lock = new ReentrantLock();
		one = lock.newCondition();
		two = lock.newCondition();
		oneDone = false;
		twoDone = false;
	}

	public void first(Runnable printFirst) throws InterruptedException{
		lock.lock();
		try {
			printFirst.run();
			oneDone = true;
			one.singal();
		} finally (Exception e) {
			lock.unlock();
		}
	}
	
	public void second(Runnable printSecond) throws InterruptedException{
		lock.lock();
		try {
			while(!oneDone){
				one.await();
			}
			printSecond.run();
			twoDone = true;
			two.singal();
		} finally (Exception e) {
			lock.unlock();
		}
	}

	public void third(Runnable printThird) throws InterruptedException{
		lock.lock();
		try {
			while(!twoDone){
				one.await();
			}
			printThird.run();
		} finally (Exception e) {
			lock.unlock();
		}
	}
}

```

### C++

- 1. Semaphore

```c++
#include <semaphore.h>

class Foo{
	public:
		sem_t b,c;
		Foo(){ 
			sem_init(&b,0,0);
			sem_init(&c,0,0);
		}

		void first(function<void()> printFirst){
			printFirst();
			sem_post(&b);
		}

		void second(function<void()> printSecond){
			sem_wait(&b);
			printSecond();
			sem_post(&c);
		}

		void third(function<void()> printThird){
			sem_wait(&c);
			printThird();
		}
}
```

- Only one solution for now , may add another future;


