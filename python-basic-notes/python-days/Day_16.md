# 多任务，并发编程

### 多任务 (目的 : 提高任务执行效率; 解释: 同一时间段/同一时间执行多个任务)

+ 单核处理器实现多任务 : 调度算法、时间片轮转

+ 并发 : 多个任务交替执行

+ 并行 : 多个任务同时执行

+ 执行时间 : 耗时最长的任务决定

+ python 实现多任务

    + 开启进程的数目最大不能大于 cpu 核心的两倍，超过此限制提升很低
    
    + 单核处理器无法发挥多进程优势

### 同步和异步
    
+ 同步 : 协同、配合完成，描述的是串行执行，多个任务按照顺序依次执行

+ 异步 : 描述并发和并行，多任务在同一个时间内同时执行，任务间不会等待其他任务结束再执行,通过异步执行的任务执行结束后我们可以通过回调函数获得结果

+ 同步和异步的区别 : 请求发出后，是否需要等待结果，才能继续执行其他操作


### 进程和线程 (进程 : 线程 <==> 1 : N)

+ 进程
    + ***正在运行的一个程序就是一个进程***，是系统进行***资源分配的最小单位***
    + 每一个进程都有自己独立的内存和资源
    + 在进程入口执行的第一个线程被视为这个进程的主线程
    + 程序只有一个，进程可以有多个
    + 进程于进程相互独立，资源不可共享
    + 适用于计算密集型操作
    
+ 线程 
    + 线程是***进程中***的一个执行线路或流程，***程序执行的最小单位***，线程是***任务调度的最小单位***
    + 线程可以看做是轻量级的进程，进程是资源的拥有者，进程的 创建、撤销、切换，对内存大量消耗
    + 进程是资源分配的最小单位，线程是程序调度的最小单位，程序真正执行时，调用的是线程
    + 适用于 I/O 密集型操作
    
+ 进程和线程的区别
    + 一个程序至少有一个进程,一个进程至少有一个线程
    + 线程的划分尺度小于进程，使得多线程程序的并发性高
    + 进程在执行过程中拥有独立的内存单元，一个进程崩溃后，在保护模式下不会对其它进程产生影响,而多个线程共享内存，从而极大地提高了程序的运行效率
    + 一个线程死掉就等于整个进程死掉，所以多进程的程序要比多线程的程序健壮，但在进程切换时，耗费资源较大，效率要差一些
    + 线程在执行过程中与进程还是有区别的. 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口. 但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制
    + 从逻辑角度来看，多线程的意义在于一个应用程序中，有多个执行部分可以同时执行. 但操作系统并没有将多个线程看做多个独立的应用，来实现进程的调度和管理以及资源分配.这就是进程和线程的重要区别

### 线程实现多任务
    
+ 使用 threading 模块创建线程 `import threading`

    ```
  import threading
  
  thrading.Thread(target=任务)
  threading.Thread(self, group=None, target=任务, name=函数名,
                 args=(参数), kwargs=None, *, daemon=None)
  ```
    
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
    ```
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
  ```
  
+ 线程之间共享全局变量
    + 共享全局变量导致的 "线程不安全" 问题
    
+ 同步和异步