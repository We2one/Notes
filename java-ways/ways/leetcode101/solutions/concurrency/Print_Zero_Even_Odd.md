```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 15:01:32
   Modified by: Gentleman.Hu
   Modified time: 2020-10-21 17:50:29
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Leetcode of concurrency,Pirnt zero Even odd
 ```

## Print Zero Even Odd

> [source](https://leetcode.com/problems/print-zero-even-odd/)

- Problem

Suppose you are given the following code:

```java
class ZeroEvenOdd{
	public ZeroEvenOdd(int n){...} // 

	public void zero(printNumber){}// only output 0's
	public void even(printNumber){}// only output even numbers
	public void odd(printNumber){} // only output odd numbers
}
```

The same instance of `ZeroEvenOdd` will be passed to three different threads:

1. Thread A will call `zero()` which should only output 0's.
2. Thread B will call `zero()` which should only output even numbers.
3. Thread C will call `zero()` which should only output odd numbers.

Each of the threads is given a `printNumber` method to output an integer. Modify the given program to output the `010203040506...`where the length of the series must be `2n`.

- Example

```yaml
Input: n = 2
Output: "0102"
```

```yaml
Input: n = 5
Output: "0102030405"
```

## Solution

### Java

- 1. 

> Answer below is not accepted! Correct it few later...

```java
class ZeroEvenOdd {
    private int n;
    private int number;
    private Object lock;
    private int next;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.lock = new Object();
        this.next = 1;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        synchronized(lock){
            for(int i=1;i<=this.n;i++){
                while(next!=0){
                    lock.wait();
                }
                next = i%2==0 ? 2: 1;
                lock.notifyAll();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        synchronized(lock){
            for(int i=2;i<=this.n;i+=2){
                while(next!=2){
                    lock.wait();
                }
                next = 0;
                printNumber.accept(i);
                lock.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        synchronized(lock){
            for(int i=1;i<=this.n;i+=2){
                while(next!=1){
                    lock.wait()
                }
                next = 0;
                printNumber.accept(i);
                lock.notifyAll();
            }
        }
    }
}

```

- Solution below is accepted, but not optimized.

```java
class ZeroEvenOdd {
    private int n;
    private Semaphore zero;
    private Semaphore odd; 
    private Semaphore even;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
        this.zero = new Semaphore(1);
        this.odd = new Semaphore(1);
        this.even = new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for(int i =1; i<=n; i++){
            zero.acquire();
            printNumber.accept(0);
            odd.release(1);
            even.release(1);
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for( int i =2; i<=n; i+=2){
            even.acquire(2);
            printNumber.accept(i);
            zero.release(1);
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for( int i =1; i<=n; i+=2){
            odd.acquire(2);
            printNumber.accept(i);
            zero.release(1);
        }
    }
}

```

