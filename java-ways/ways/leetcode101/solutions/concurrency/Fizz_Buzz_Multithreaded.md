```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-21 10:11:56
   Modified by: Gentleman.Hu
   Modified time: 2020-10-21 10:53:46
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: #1195 Fizz Buzz Multithreaded
 ```

## Fizz Buzz Multithreaded

> [source](https://leetcode.com/problems/fizz-buzz-multithreaded/)

## Problem

Write a program that outputs the string representation of numbers from 1 to n, however:

- If the number is divisible by 3, output "fizz".
- If the number is divisible by 5, output "buzz".
- If the number is divisible by both 3 and 5, output "fizzbuzz".

For example, for `n=15`, we output: `1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz`.

Suppose you are given the following code:

```java
class FizzBuzz{
	public FizzBuzz(int n ){...}// constructor
	public void fizz(printFizz){...}// only output "fizz"
	public void buzz(printBuzz){...}// only output "buzz"
	public void fizzbuzz(printFizzBuzz){...}//only output "fizzbuzz"
	public void number(printNumber){...}//only output the numbers
}
```

Implement a multithreaded version of FizzBuzz with four threads.
The same instance of `FizzBuzz` will be passed to four different threads:

1. Thread A will call `fizz()` to check for for divisibility of 3 and outputs `fizz`.
2. Thread B will call `buzz` to check for for divisibility of 5 and outputs `buzz`.
3. Thread C will call `fizzbuzz()` to check for for divisibility of 3 and outputs `fizzbuzz`.
4. Thread D will call `number` to check for for divisibility of 3 and outputs numbers.

## Solution

### Java

- 1.

> using Object lock

```java
class FizzBuzz {
    private int n;
    private int count;
    private Object lock;

    public FizzBuzz(int n) {
        this.n = n;
        this.count = 1;
        this.lock = new Object();
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while(count<=n) {
            synchronized (lock) {
                if (count<=n && count % 3 == 0 && count % 5 != 0) {
                    printFizz.run();
                    count++;
                }
            }

        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while(count<=n) {
            synchronized (lock) {
                if (count<=n && count % 5 == 0 && count % 3 != 0) {
                    printBuzz.run();
                    count++;
                }
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while(count<=n) {
            synchronized (lock) {
                if (count<=n && count % 5 == 0 && count % 3 == 0) {
                    printFizzBuzz.run();
                    count++;
                }
            }
        }

    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while(count<=n) {
            synchronized (lock) {
                if (count<=n && count % 3 != 0 && count % 5 != 0) {
                    printNumber.accept(count);
                    count++;
                }
            }
        }
    }
}
```

- 2.

> using `Semaphore`

```java
class FizzBuzz {
    private int n;
    private int counter;

    private Semaphore fizzSemaphore = new Semaphore(0);
    private Semaphore buzzSemaphore = new Semaphore(0);
    private Semaphore fizzBuzzSemaphore = new Semaphore(0);
    private Semaphore numberSemaphore = new Semaphore(1);

    public FizzBuzz(int n) {
        this.n = n;
        this.counter = n;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (counter > 0) {
            fizzSemaphore.acquire();
            if (counter == 0)
                break;
            counter--;
            printFizz.run();
            numberSemaphore.release();
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (counter > 0) {
            buzzSemaphore.acquire();
            if (counter == 0)
                break;
            counter--;
            printBuzz.run();
            numberSemaphore.release();
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (counter > 0) {
            fizzBuzzSemaphore.acquire();
            if (counter == 0)
                break;
            counter--;
            printFizzBuzz.run();
            numberSemaphore.release();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n ; i++) {
            boolean divisibleByThree = ((i % 3) == 0);
            boolean divisibleByFive = ((i % 5) == 0);
            boolean divisibleByBoth = divisibleByThree && divisibleByFive;

            if (!divisibleByThree && !divisibleByFive) {
                numberSemaphore.acquire();
                counter--;
                printNumber.accept(i);
                numberSemaphore.release();
                continue;
            } else {
                if (divisibleByBoth) {
                    numberSemaphore.acquire();
                    fizzBuzzSemaphore.release();
                    continue;
                }
                if (divisibleByThree) {
                    numberSemaphore.acquire();
                    fizzSemaphore.release();
                    continue;
                }
                if (divisibleByFive) {
                    numberSemaphore.acquire();
                    buzzSemaphore.release();
                    continue;
                }
            }
        }
        fizzSemaphore.release();
        buzzSemaphore.release();
        fizzBuzzSemaphore.release();
    }
}
```