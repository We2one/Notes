```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 14:33:44
   Modified by: Gentleman.Hu
   Modified time: 2020-10-17 15:09:13
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Leetcode of concurrency,print foobar alternately
 ```

## Print FooBar Alternately

> [source](https://leetcode.com/problems/print-foobar-alternately/)

- Problem

Suppose you are given the following code;

```java
class FooBar{
	public void foo(){
		for(int i = 0; i < n;i++){
			print("foo");
		}
	}
	public void bar(){ 
		for(int i = 0; i< n; i++){
			print("bar");
		}
	}
}

```

The same instance of `FooBar` will be passed to two different threads.
Thread A will call `foo()` while thread B will call `bar()` . Mofify the given program to output "foobar" n times.

- Examples

```yaml
Input: n = 1
Output: "foobar"
```

```yaml
Input: n = 2
Outpt: "foobarfoobar"
```

## Solution

### Java

- 1.

> using `Semaphore`

```java
class FooBar {
    private int n;
    private Semaphore r1,r2;

    public FooBar(int n) {
        this.n = n;
        this.r1 = new Semaphore(0);
        this.r2 = new Semaphore(1);
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            r2.acquire();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            r1.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            r1.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            r2.release();
        }
    }
}
```

- 2.

> using `Object lock`

```java
class FooBar {
    private int n;
    private boolean oneDone,twoDone;
    private Object lock;

    public FooBar(int n) {
        this.n = n;
        this.lock = new Object();
        this.oneDone = false;
        this.twoDone = true;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(lock){
                while(!twoDone){
                    lock.wait();
                }
            // printBar.run() outputs "bar". Do not change or remove this line.
                printFoo.run();
                oneDone = true;
                twoDone = false;
                lock.notifyAll();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            synchronized(lock){
                while(!oneDone){
                    lock.wait();
                }
            // printBar.run() outputs "bar". Do not change or remove this line.
                printBar.run();
                twoDone = true;
                oneDone = false;
                lock.notifyAll();
            }
        }
    }
}
```