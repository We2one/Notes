```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 16:43:32
   Modified by: Gentleman.Hu
   Modified time: 2020-10-17 17:12:19
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Leetcode of concurrency,Building H2O
 ```

## Building H2O

> [source](https://leetcode.com/problems/building-h2o/)

## Question

There are two kinds of threads, `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given `releaseHydrogen` and `releaseOxygen` methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

- If an oxygen thread arrives ata the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
- If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
  
We don't have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

- Example

```yaml
Input: "HOH"
Output: "HHO"
```

```yaml
Input: "OOHHHH"
Output: "HHOHHO"
```

- Constraints:
  - Total length of input string will be 3n, where 1<=n <=20.
  - Total number of `H` will be 2n in the input string.
  - Total number of `O` will be n in the input string.

## Solution

### Java

- 1.

> locking current instance

```java
class H2O {
    private int count = 0;
    public H2O() {
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		synchronized(this){
            while(count==2){
                wait();
            }
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
            releaseHydrogen.run();
            count++;
            notifyAll();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        synchronized(this){
            while(count!=2){
                wait();
            }
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		    releaseOxygen.run();
            count = 0;
            notifyAll();
        }
    }
}
```