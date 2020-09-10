### 线程实现多任务

+ 使用 threading 模块创建线程 `import threading`

  ````
  import threading
  
  thrading.Thread(target=任务)
  threading.Thread(self, group=None, target=任务, name=函数名,
                 args=(参数), kwargs=None, *, daemon=None)
  ````
  
    1. 传递参数 (线程关键字 args=() 传递参数)    `threading.Thread(target=函数名, args=())`
    
    2. join() 方法 : 当前线程执行完后其他线程才会继续执行
    
    3. setDaemon() 方法 : 将当前线程设置为守护线程来守护主线程 (需要在子线程开启的时候设置成守护线程，否则无效) `线程名.setDaemon(True)`

        + 当主线程结束后，守护线程也随之结束，无论是否执行完成

        + eg: QQ 多个聊天窗口
        
    4. 实例方法

        + getName() : 获取当前线程名称

        + setName() : 设置当前线程名称

        + is_alive() : 判断的当前线程存活状态  (曾经使用 isAlive() 判断)
        
    5. threading 模块提供的方法

        + threading.currentThread() <==> threading.current_thread() : 返回当前线程变量

        + threading.enumerate() : 返回一个 包含正在运行线程的 list 。(正在运行: 线程启动后结束前, 不包括启动前与结束后)

        + threading.activeCount() <==> threading.active_count() : 返回正在运行线程的数量, 与 len(threading.enumerate()) 结果相同
  
+ 使用继承方式开启线程 (定义一个类 继承 threading.Thread 类，复写父类的 run() 方法)
+ 
    ````
  import threading
  import time
    
    
  class MyThread(threading.Thread):
    
      def __init__(self, num):
          super(MyThread, self).__init__()
          self.num = num
    
      def run(self):
          for i in range(self.num):
              print(f"---run\t{i}---")
    
    
  if __name__ == "__main__":
      my_thread = MyThread(3)
      my_thread.run()
  ````
  
+ 线程之间共享全局变量

    + 共享全局变量导致的 "线程不安全" 问题

        + 加锁

        + 延迟加载
    
+ 同步和异步

    + 同步 : 协同步调，按预定的先后次序进行运行
    
### 互斥锁 GIL

+ 互斥锁 : 多个线程几乎同时修改一个共享数据时，同步控制，保证多个线程安全的访问竞争资源(全局内容),

    + 在线程需要更改共享数据时，先将其锁定，仅有此线程可对数据进行操作，直到该线程将资源状态更改为非锁定状态 (释放资源)，其他进程才可以再次锁定。

    + 保证每次只有一个线程进行写入操作，保证多线程下数据的安全性

+ threading 模块中的 Lock 类，方便的处理锁定

    + `threading.Lock()` : 创建锁

    + `acquire(self, blocking: bool = ..., timeout: float = ...) -> bool` : 锁定

        + blocking  : True 当前线程堵塞，直到获取到这个锁为止 (默认为 True)，设定为 False 当前线程不会堵塞

            ````
            import threading
            import time
            
            
            def func1():
                print('t1开始执行')
                if t1_lock.acquire():
                    time.sleep(1)
                    print('t1 获取 t1 锁')
                    if t2_lock.acquire(blocking=False):
                        print('t1 获取 t2 锁')
                        t2_lock.release()
                        print('t1 释放 t2 锁')
                    t1_lock.release()
                    print('t1 释放 t1 锁')
            
            def func2():
                print('t2开始执行')
                if t2_lock.acquire():
                    time.sleep(1)
                    print('t2 获取 t2 锁')
                    if t1_lock.acquire(blocking=False):
                        print('t2 获取 t1 锁')
                        t1_lock.release()
                        print('t2 释放 t1 锁')
                    t2_lock.release()
                    print('t2 释放 t2 锁')
            
            if __name__ == "__main__":
                t1_lock = threading.Lock()
                t2_lock = threading.Lock()
            
                t1 = threading.Thread(target=func1)
                t2 = threading.Thread(target=func2)
            
                t1.start()
                t2.start()
          """
          t1开始执行
          t2开始执行
          t2 获取 t2 锁t1 获取 t1 锁
          t2 释放 t2 锁
          t1 获取 t2 锁
            
          t1 释放 t2 锁
          t1 释放 t1 锁
          """
          ````
    
+ 上锁解锁过程

    + 当一个线程调用锁的 acquire() 方法获得锁时，锁就进入 locked 状态

    + 每次只有一个线程可以获得锁，此时另一个线程试图获得这个锁，该线程就会变成 blocked 阻塞状态，直到有用锁的线程调用 release() 方法释放锁，锁进入 unlocked 状态

    + 线程调度程序从处于同步阻塞状态的线程中选择一个获得锁，并使得该线程进入运行 (running) 状态

    ````
    import threading
    import time
    
    tickes = 1000
    
    
    def fun1(window):
        global tickes
        # mutexFlag = mutex.acquire(True)
        # if mutexFlag:
        while tickes > 1:
            # 创建锁
            if mutex.acquire():
                tickes -= 1
                time.sleep(0.01)
    
                print(f'{window}卖出一张票,剩余{tickes}')
                # 释放锁
                mutex.release()
    
    
    if __name__ == "__main__":
        # 添加锁
        mutex = threading.Lock()
    
        t1 = threading.Thread(target=fun1, args=('窗口1', ))
        t2 = threading.Thread(target=fun1, args=("窗口2", ))
    
        t1.start()
        t2.start()
  ````
  
+ 锁的好处
  
    + 确保了某段关键代码只能有一个线程从头到尾完整的运行
    
+ 锁的缺点

    + 阻止了多线程并发执行，包含锁的代码只能以单线程模式运行，效率大大下降

    + 存在多个锁，不同线程持有不用锁，并试图获取其他线程的锁，可能死锁
    
### 死锁

+ 多个线程共享资源时，如果两个线程分别占有一部分资源，并且同时等待对方资源，会造成死锁。

+ 锁之间相互嵌套，可能出现死锁

+ 解决

    + 添加休眠时间

    + 使用 blocking 

### 非共享数据 (全局变量在多线程中，容易被多个线程调用修改，容易发生数据错乱)

+ 非全局变量加锁 (私有变量与锁无关)

+ 局部变量属于各自线程的，非共享

### 生产者和消费者模式

+ 队列 (先进先出) `from queue import Queue`

    + python 的 Queue 模块提供了同步的、线程安全的队列类，都采用了锁原语 (要么不做，要么做完)，能在多线程直接使用，可以使用队列实现线程同步

        + FIFO : 先进先出

            + queue.Queue(self, maxsize=0)

            ````
            import queue

            # 先进后出
            q = queue.Queue()
            q.put(1)
            q.put(2)
            q.put(3)
            i = 0
            while i<q.qsize():
                print(q.get())
            """
            1
            2
            3
            """
          ````
          
        + LIFO : 后入先出

            + queue.LifoQueue()

            ````
            import queue

            # 先进后出
            q = queue.LifoQueue()
            q.put(1)
            q.put(2)
            q.put(3)
            i = 0
            while i<q.qsize():
                print(q.get())
            """
            3
            2
            1
            """
          ````
          
        + PriorityQueue : 优先级队列，数字越小优先级越高

            + q = queue.PriorityQueue()

            + q.put((优先级, "队列名"))

            ````
            import queue

            q = queue.PriorityQueue()
            q.put((1, "队列1"))
            q.put((-1, "队列2"))
            q.put((0, "队列3"))
            q.put((11, "队列4"))
            q.put((5, "队列5"))
            i = 0
            while i < q.qsize():
                print(q.get())
            """
            (-1, '队列2')
            (0, '队列3')
            (1, '队列1')
            (5, '队列5')
            (11, '队列4')
            """
          ````
    
    + 常用操作

        + q.empty() : 判断是否为空

        + q.full() : 判断队列是否已满

        + q.put() : 放入队列

        + q.get() : 取出队列

            + timeout = 1 : 阻塞，通过 timeout 参数解决阻塞问题，抛出 queue.Empty 异常

            + block = False : block 参数 False 也可以解决程序阻塞问题,抛出 queue.Empty 异常

        + q.qsize() : 判断当前队列内内容数

        + q.get_nowait() : 解决阻塞问题，可以设置不要等待，没有数据就抛出异常
        
        ````
        from queue import Queue

        # 先入先出
        q = Queue()
        # 判断是否为空，为空 TRUE
        print(q.empty())
        
        q.put('d1')
        q.put('d2')
        q.put('d3')
        q.put('d4')
        # 判断队列是否已满，满了返回 TRUE
        print(q.full())
        print(q.get())
        print(q.get())
        print(q.get())
        print(q.get())
        
        # 阻塞，通过 timeout 参数解决阻塞问题，抛出 queue.Empty 异常
        # print(q.get(timeout=1))
        
        # 接上一行的的例子，可以设置不要等待，没有数据就抛出异常
        # print(q.get_nowait())
        
        # 或者使用 if判断 qsize 是否等于 0
        print(q.qsize())
        
        # block 参数 False 也可以解决程序阻塞问题,抛出 queue.Empty 异常
        print(q.get(block=False))
      ````
      
    + 规定队列长度
      
    + queue.Queue(maxsize=30) : 设置有长度限制的队列
    
+ 生产者与消费者模式
  
    + 定义 : 通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度
    
    + 什么是生产者消费者模式

        + 通过一个容器来解决生产者和消费者的强耦合问题。

        + 生产者和消费者彼此不直接通讯，通过阻塞队列来通讯，阻塞队列相当于一个缓冲区，平衡供需关系
    
    + 简单 : 两个消费者一个生产者

        ````
        import threading
        import time
        import queue
        
        
        # 简单生产消费问题
        q = queue.Queue()
        
        
        def producer(name):
            """生产者"""
            count = 1
            while True:
                q.put(f'{count}')
                print(f'生产了{count}个包子')
                count += 1
                time.sleep(0.5)

        def consumer(name):
            """消费者"""
            while True:
                print(f'{name}取出了第{q.get()}个包子')
                time.sleep(2)

        if __name__ == "__main__":
            p = threading.Thread(target=producer, args=("厨师", ))
        
            c1 = threading.Thread(target=consumer, args=("消费者1", ))
            c2 = threading.Thread(target=consumer, args=("消费者2", ))
        
            p.start()
            c1.start()
            c2.start()
        """
        生产了1个包子
        消费者1取出了第1个包子
        生产了2个包子消费者2取出了第2个包子
        
        生产了3个包子
        生产了4个包子
        消费者1取出了第3个包子
        生产了5个包子
        ...
        """
      ````
    
    + 复杂 : 多对多

        ```
        import threading
        import time
        import queue
        import random
        
        # 多对多
        q = queue.Queue(maxsize=10)
        count = 1
        
        def producer(name):
            """生产者"""
            global count
            while True:
                q.put(f'{count}')
                print(f'生产了{count}个包子')
                count += 1
                time.sleep(random.random()*12)
        
        def consumer(name):
            """消费者"""
            while True:
                print(f'{name}取出了第{q.get()}个包子')
                time.sleep(random.random()*12)
        
        if __name__ == "__main__":
            p1 = threading.Thread(target=producer, args=("厨师1", ))
            p2 = threading.Thread(target=producer, args=("厨师2",))
        
            c1 = threading.Thread(target=consumer, args=("消费者1", ))
            c2 = threading.Thread(target=consumer, args=("消费者2", ))
            c3 = threading.Thread(target=consumer, args=("消费者3",))
            c4 = threading.Thread(target=consumer, args=("消费者4",))
        
            p1.start()
            p2.start()
            c1.start()
            c2.start()
            c3.start()
            c4.start()
        """
        生产了1个包子
        生产了2个包子
        消费者1取出了第1个包子
        消费者2取出了第2个包子
        生产了3个包子
        消费者3取出了第3个包子
        生产了4个包子
        消费者4取出了第4个包子
        生产了5个包子消费者2取出了第5个包子
        
        生产了6个包子
        """
      ```

### threadLocal

+ 多线程条件下，每个线程都有自己的数据，使用局部变量比全局变量好，不会影响其他线程，也不必加锁

+ 使用函数传参的方法 (局部变量在函数调用时传递比较麻烦, 层层传递)

    ````
    # threadLocal ① 函数传参
    def process_student(num):
        std = Student(name)
        # std 是局部变量，但是每个函数都会使用 
        do_task_1(std)
        do_task_2(std)
        
        
    def do_task_1(std):
        do_subtask_1(std)
        do_subtask_2(std)
        
    
    def do_task_2(std):
        do_subtask_2(std)
        do_subtask_2(std)
  ````

+ 全局字典的方法 (全局字典存储所有 对象 ，然后以 thread 自身作为 key 获得线程对应的 对象)

    + 优点 : 消除了局部定义中函数传递的问题

    + 缺点 : 每个函数获取的方式落后

    ```
    # threadLocal ② 全局字典
    global_dict = {}
    
    
    def std_thread(num):
        std = Student(name)
        # 把 std 放到全局变量 global_dict 内
        global_dict[threading.current_thread()] = std
        do_task_1()
        do_task_2()
        
    def do_task_1():
        # 不传入 std, 根据当前线程查找
        std = global_dict[threading_dict_thread()]
  ```
  
+ 使用 threadLocal 方法 (定义在全局，每个 thread 都可以对它进行读写，处理属于自己的副本，但是互不影响，互不干扰)

    + 常用地方是为每个线程绑定一个数据库连接,Http 请求，用户身份信息等

    ````
    import threading
    # threadLocal ③ threadLocal
    # 创建全局 threadLocal 对象
    local_school = threading.local()
    
    def process_student():
        # 获取当前线程相关 student
        std = local_school.student
        print(f'hello, {std} (in {threading.current_thread().name})')
    
    
    def process_thread(name):
        # 绑定 ThreadLocal 的 student
        local_school.student = name
        process_student()
    
    if __name__ == "__main__":
        t1 = threading.Thread(target=process_thread, args=("学生1", ), name="线程1")
        t2 = threading.Thread(target=process_thread, args=("学生2", ), name="线程2")
    
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    """
    hello, 学生1 (in 线程1)
    hello, 学生2 (in 线程2)
    """
  ````
  
### 全局解释器锁

+ python 的执行 : 由 Python 虚拟机 (解释器主循环) 控制。在主循环中同时只能有一个控制线程再执行；内存中可以有许多程序，但任意给定时刻只能有一个在运行

    + 因此 : python 解释器可以运行多个线程，但任意给定时刻只有一个线程会被解释器运行

+ GIL (全局解释器锁) : 保证同时只有一个线程运行

+ 多线程中, Python 虚拟机执行顺序

    1. 设置 GIL

    2. 切换一个线程执行

    3. 执行下边两个操作之一

        + 指定数量的字节码指令

        + 线程主动让出控制权 (可以调用 time.sleep(0) 完成)

    4. 把线程设置回睡眠 (切换出线程)

    5. 解锁 GIL

    6. 重复执行
    
+ 执行外部代码时, GIL 会保持锁定，直至执行结束

+ 避免使用 GIL 影响 --> 使用 multiprocess 代替 Thread

    + multiprocess 库 : 使用多进程，每个进程都由独立的 GIL，缺点是会增加程序实现时线程间数据通讯和同步的难度