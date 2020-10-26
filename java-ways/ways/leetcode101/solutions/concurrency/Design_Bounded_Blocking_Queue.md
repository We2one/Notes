```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-18 11:09:55
   Modified by: Gentleman.Hu
   Modified time: 2020-10-18 22:19:06
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Design Bounded Blocking Queue

> [source](https://leetcode.com/problems/design-bounded-blocking-queue) `require premium`
> [alternative](https://leetcode.jp/problemdetail.php?id=1188)
> [alternative_cn](https://leetcode.jp/leetcode-1188-design-bounded-blocking-queue-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/)

## Question

Implement a thread safe bounded blocking queue that has the following methods:

- `BoundedBlockingQueue(int capacity)` The constructor initializes the queue with a `capacity`. 
- `void enqueue(int element)` Add an `element` to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
- `int dequeue()` Return the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
- `int size()` Returns the number of elements currently in the queue.

Your implementation will be tested using multiple threads at the same time. Each Thread will either be a producer thread that only makes calls to the `enqueue` method or a consumer thread that only makes calls to the `dequeue` method. The `size` method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.

## Examples

- Example1:

```yaml
Input:
1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

Output:
[1,0,2,2]

Explanation:
Number of producer threads = 1
Number of consumer threads = 1

BoundedBlockingQueue queue = new BoundedBlockingQueue(2);   // initialize the queue with capacity = 2.

queue.enqueue(1);   // The producer thread enqueues 1 to the queue.
queue.dequeue();    // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue();    // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0);   // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2);   // The producer thread enqueues 2 to the queue.
queue.enqueue(3);   // The producer thread enqueues 3 to the queue.
queue.enqueue(4);   // The producer thread is blocked because the queue's capacity (2) is reached.
queue.dequeue();    // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size();       // 2 elements remaining in the queue. size() is always called at the end of each test case.
```

- Example2:

```yaml
Input:
3
4
["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
[[3],[1],[0],[2],[],[],[],[3]]

Output:
[1,0,2,1]

Explanation:
Number of producer threads = 3
Number of consumer threads = 4

BoundedBlockingQueue queue = new BoundedBlockingQueue(3);   // initialize the queue with capacity = 3.

queue.enqueue(1);   // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0);   // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2);   // Producer thread P3 enqueues 2 to the queue.
queue.dequeue();    // Consumer thread C1 calls dequeue.
queue.dequeue();    // Consumer thread C2 calls dequeue.
queue.dequeue();    // Consumer thread C3 calls dequeue.
queue.enqueue(3);   // One of the producer threads enqueues 3 to the queue.
queue.size();       // 1 element remaining in the queue.

Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.
```

## Solution

### Java

- 1:

> using `synchronized` lock queue

```java
Queue<Integer> q = new LinkedList<>(); // 队列Queue
public BoundedBlockingQueue(int capacity) {
    size = capacity; // 队列上限
}

public void enqueue(int element) throws InterruptedException {
    synchronized(q){ // 保证Queue不会同时被多个线程操作
        // 如果已经达到存储上限，阻塞当前线程
        while(q.size()==size){
            q.wait();
        }
        // 将元素添加至队列
        q.offer(element);
        // 通知所有线程队列已经被更新
        q.notifyAll();
    }
}

public int dequeue() throws InterruptedException {
    synchronized(q){ // 保证Queue不会同时被多个线程操作
        // 如果队列为空，阻塞当前线程
        while(q.size()==0){
            q.wait();
        }
        // 删除队列一个元素
        int num = q.poll();
        // 通知所有线程队列已经被更新
        q.notifyAll();
        // 返回删除元素
        return num;
    }
}

public int size() {
    return q.size();
}
```

- 2:

> using `semaphore` ,(not accepted in interview)

```java
Semaphore se;
Semaphore sd;
int size;
Queue<Integer> q = new LinkedList<>();
public BoundedBlockingQueue(int capacity) {
    size = capacity;
    se = new Semaphore(size);
    sd = new Semaphore(0);
}

public void enqueue(int element) throws InterruptedException {
    se.acquire();
    q.offer(element);
    sd.release();
}

public int dequeue() throws InterruptedException {
    sd.acquire();
    int num = q.poll();
    se.release();
    return num;
}

public int size() {
    return q.size();
}
```