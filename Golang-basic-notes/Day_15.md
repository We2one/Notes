### Golang goroutine channel 实现并发和并行

#### 1. goroute 使用原因

+ 加快程序计算、运行方法
  + 传统方法 : for 循环判断
  + 使用 并发或并行,使用 **goroutine** (goroutine 结合 channel)

#### 2. 进程、线程以及并行、并发

##### 2.1 关于进程和线程

1. **进程 (Process)** : 程序在操作系统的一次执行过程,是系统进行资源分配和调度的基本单位,进程是一个动态概念,是程序在执行过程中分配和管理资源的基本单位,每一个进程都有自己的地址空间
   + 进程的 5 种基本状态: 初始态、执行态、等待状态、就绪状态、终止状态
2. **线程** : 进程的一个执行实例,程序执行的最小单元,比进程更小的能独立运行的基本单位
   + 一个进程可以创建多个线程,同一个进程中多个线程可以并发执行,一个程序要运行的话至少有一个进程

##### 2.2 关于并发和并行

1. **并发** : 多个线程同时竞争一个位置,竞争到的才可以执行,每一个时间只有一个线程再执行
2. **并行** : 多个进程可以同时执行,每一个时间段,可以有多个线程同时执行
3. **通俗讲** : 多线程程序在 **单核 CPU** 上面执行就是**并发**;在**多核 CPU** 上执行就是**并行**;如果线程数量大于 CPU 核数,则多线程在多个 CPU 上运行既有并行又有并发

#### 3. Golang 中的协程 (goroutine) 以及主线程

+ **golang 中主线程** : 在一个 Golang 程序的**主线程**上可以起**多个协程**.**Golang中的多协程**可以实现**并行或并发**
+ **协程** (用户级线程) : 系统不知道有协程的存在,完全由用户自己的程序进行调度.
+ 由于 Golang 的语言层面具有原生协程,在函数或者方法前加 **go 关键字** 就可以创建一个协程.
+ Golang 中的协程就是 goroutine 
+ **多协程和多线程** : Golang 中每个 goroutine (协程) 默认占用内存远比 Java、C 的线程少.
  + OS 线程 (操作系统线程) 一般具有固定的栈内存 (常为 2MB 左右),一个 goroutine (协程)占用内存非常少,只有 

#### 4. Goroutine KB 左右的使用以及 svnc.WaitGrouo

+ **并行执行需求** : 在主线程中,开启一个 goroutine 

+ 开启一个协程 : `go 方法名`

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  // 在主线程中开启一个 goroutine,与主线程并行执行，每50ms s输出一次
  
  func test() {
  	for i := 0; i < 10; i++ {
  		fmt.Println("协程")
  		time.Sleep(time.Microsecond * 50)
  	}
  }
  
  func main() {
  	//test() 直接调用,顺序执行
  	go test() //开启协程
  	for i := 0; i < 10; i++ {
  		fmt.Println("hello Golang")
  		time.Sleep(time.Microsecond * 50)
  	}
  }
  /*
  协程
  协程
  hello Golang
  hello Golang
  协程
  hello Golang
  协程
  hello Golang
  协程
  hello Golang
  协程
  协程
  hello Golang
  hello Golang
  协程
  hello Golang
  协程
  协程
  hello Golang
  */
  ```

+ **存在问题** : 当主进程执行过快时,容易出现协程未执行结束主进程就退出的问题

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  // 在主线程中开启一个 goroutine,与主线程并行执行，每50ms s输出一次
  
  func test() {
  	for i := 0; i < 10; i++ {
  		fmt.Println("协程---", i)
  		time.Sleep(time.Microsecond * 1000)
  	}
  }
  
  func main() {
  	//test() 直接调用,顺序执行
  	go test() //开启协程
  	for i := 0; i < 10; i++ {
  		fmt.Println("hello Golang---", i)
  		time.Sleep(time.Microsecond * 10)
  	}
  }
  /*
  hello Golang--- 0
  协程--- 0
  hello Golang--- 1
  hello Golang--- 2
  协程--- 1
  hello Golang--- 3
  hello Golang--- 4
  协程--- 2
  hello Golang--- 5
  协程--- 3
  hello Golang--- 6
  hello Golang--- 7
  hello Golang--- 8
  协程--- 4
  hello Golang--- 9
  协程--- 5
  */
  ```

+ 使用 **svnc.WaitGrouo** 使主进程执行结束后等待协程执行 (结合使用 Add(计数器增加数目); Done() 计数器减一)

  ```go
  package main
  
  import (
  	"fmt"
  	"sync"
  	"time"
  )
  
  /*
  使用 sync.WaitGroup 使主线程等待协程执行结束
   */
  
  // 定义一个 sync.WaitGroup 对象
  var wg sync.WaitGroup
  
  func test() {
  	for i := 0; i < 10; i++ {
  		fmt.Println("协程---", i)
  		time.Sleep(time.Microsecond * 1000)
  	}
  	wg.Done() // 协程计数器 减一
  }
  
  func main() {
  	// 协程计数器 加一
  	wg.Add(1)
  	go test() //开启协程
  	for i := 0; i < 10; i++ {
  		fmt.Println("hello Golang---", i)
  		time.Sleep(time.Microsecond * 10)
  	}
  	wg.Wait() // 等待
  	fmt.Println("主线程退出")
  }
  /*
  hello Golang--- 0
  协程--- 0
  hello Golang--- 1
  协程--- 1
  hello Golang--- 2
  协程--- 2
  hello Golang--- 3
  hello Golang--- 4
  协程--- 3
  hello Golang--- 5
  hello Golang--- 6
  hello Golang--- 7
  协程--- 4
  协程--- 5
  hello Golang--- 8
  hello Golang--- 9
  协程--- 6
  协程--- 7
  协程--- 8
  协程--- 9
  主线程退出
  */
  ```

#### 5. 启动多个 Goroutine

+ for 循环开启多个 Goroutine

  ```go
  package main
  
  import (
  	"fmt"
  	"sync"
  	"time"
  )
  
  /*
  for 循环开启多个 Goroutine
  // 开启5个协程分别打印0-4
   */
  
  var wg sync.WaitGroup
  
  func test(num int)  {
  	defer wg.Done()
  	for i := 0; i < 5; i ++ {
  		fmt.Printf("协程(%v) 打印的 %v\n", num, i)
  		time.Sleep(time.Microsecond * 100)
  	}
  }
  
  func main() {
  
  	for i := 1; i < 5; i++ {
  		wg.Add(1)
  		go test(i)
  	}
  	wg.Wait()
  	fmt.Println("主线程执行结束")
  }
  /*
  协程(4) 打印的 0
  协程(2) 打印的 0
  协程(3) 打印的 0
  协程(1) 打印的 0
  协程(2) 打印的 1
  协程(3) 打印的 1
  协程(4) 打印的 1
  协程(1) 打印的 1
  协程(4) 打印的 2
  协程(2) 打印的 2
  协程(3) 打印的 2
  协程(1) 打印的 2
  协程(1) 打印的 3
  协程(2) 打印的 3
  协程(3) 打印的 3
  协程(4) 打印的 3
  协程(4) 打印的 4
  协程(3) 打印的 4
  协程(2) 打印的 4
  协程(1) 打印的 4
  主线程执行结束
  */
  ```

  

+ 开启多个 goroutine 使主线程等待

  ```go
  package main
  
  import (
  	"fmt"
  	"sync"
  	"time"
  )
  
  /*
  开启多个 goroutine
   */
  
  // 定义一个 sync.WaitGroup 对象
  var wg sync.WaitGroup
  
  func test1() {
  	for i := 0; i < 10; i++ {
  		fmt.Println("协程1---", i)
  		time.Sleep(time.Microsecond * 1000)
  	}
  	wg.Done() // 协程计数器 减一
  }
  
  func test2() {
  	for i := 0; i < 10; i++ {
  		fmt.Println("协程2---", i)
  		time.Sleep(time.Microsecond * 500)
  	}
  	wg.Done() // 协程计数器 减一
  }
  
  func main() {
  	// 协程计数器 加一
  	wg.Add(1)
  	go test1() //开启协程
  	wg.Add(1)
  	go test2() //开启协程
  	for i := 0; i < 10; i++ {
  		fmt.Println("hello Golang---", i)
  		time.Sleep(time.Microsecond * 10)
  	}
  	wg.Wait() // 等待
  	fmt.Println("主线程退出")
  }
  /*
  协程2--- 0
  hello Golang--- 0
  协程1--- 0
  hello Golang--- 1
  协程2--- 1
  协程2--- 2
  hello Golang--- 2
  协程1--- 1
  协程1--- 2
  hello Golang--- 3
  协程2--- 3
  协程2--- 4
  hello Golang--- 4
  协程1--- 3
  hello Golang--- 5
  协程2--- 5
  协程2--- 6
  hello Golang--- 6
  协程1--- 4
  协程2--- 7
  hello Golang--- 7
  协程2--- 8
  hello Golang--- 8
  hello Golang--- 9
  协程2--- 9
  协程1--- 5
  协程1--- 6
  协程1--- 7
  协程1--- 8
  协程1--- 9
  主线程退出
  */
  ```

#### 6. 设置 Golang 并行运行时占用 cpu 数目

+ Golang 运行时调度器调用 **GOMAXPROCS 参数**来确定需要使用多少个 OS 线程 来同时执行 Go 代码, 默认值是机器上的 CPU 核心数

+ Go 语言可以通过 **`runtime.GOMAXPROCS()`** 函数设置当前程序并发时占用 CPU 逻辑核心数

+ Go 1.5 版本之前,默认使用单核心执行, Go 1.5 版本之后， 默认使用 全部的 CPU 逻辑核心数

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"runtime"
  )
  
  /*
  自定义使用 CPU 核心数
   */
  
  func main() {
  	// 获取当前 CPU 核心数
  	cpuNum := runtime.NumCPU()
  	fmt.Println(cpuNum)
  
  	// 自定义使用核心数
  	runtime.GOMAXPROCS(8)
  }
  /*
  12
  */
  ```

#### 7. Goroutine 统计素数

1. for 循环统计素数用时 

   ```go
   package main
   
   import (
   	"fmt"
   	"time"
   )
   
   // 计算 1-200000 的数字中那些是素数
   
   func main() {
   	start := time.Now().Unix()
   	for num := 2; num <= 200000; num++ {
   		var flag = true
   		for i := 2; i < num; i ++ {
   			if num % i == 0 {
   				flag = false
   				break
   			}
   		}
   		if flag {
   			//fmt.Println(num, "是素数")
   		}
   	}
   	end := time.Now().Unix()
   	fmt.Println(end-start) // 23 秒
   }
   
   ```

2. 使用 goroutine 统计素数用时

   ```go
   package main
   
   import (
   	"fmt"
   	"sync"
   	"time"
   )
   
   /*
   goroutine 计算 1-200000 的数字中那些是素数
    */
   
   // 1 协程 统计 1-50000
   // 2 协程 统计 50001-100000
   // 3 协程 统计 100001-150000
   // 4 协程 统计 150001-200000
   // (n-1)*30000+1
   
   var wg sync.WaitGroup
   
   func test(n int) {
   	for num := (n-1)*50000+1; num <= n*50000; num++ {
   		var flag = true
   		for i := 2; i < num; i++ {
   			if num%i == 0 {
   				flag = false
   				break
   			}
   		}
   		if flag {
   			//fmt.Println(num, "是素数")
   		}
   	}
   	wg.Done()
   }
   
   func main() {
   	start := time.Now().Unix()
   	for i := 1; i < 4; i ++ {
   		wg.Add(1)
   		go test(i)
   	}
   	wg.Wait()
   	end := time.Now().Unix()
   	fmt.Println(end-start)  // 8 s
   }
   ```

   

#### 8. Channel 管道

+ **管道 (channel)** : 是 Go 语言在语言级别上提供的 goroutine 间的通讯方式,可以使用 channel 在多个 goroutine 之间传递消息
+ channel 是一个可以让 goroutine 发送特定值到另一个 goroutine 的通信机制
+ Go 语言的并发模型 是 **CSP (Communicating Sequential Processes) **, 提倡 **通过通信共享内存**而不是 **通过共享内存而实现通信**
+ Go 语言 的 管道 (channel) 是一种**特殊类型**.管道像一个传送带或队列,遵循**先进先出** 的原则,保证收发数据的顺序
+ 声明 channel 时需要为其指定元素类型

##### 8.1 channel 类型

+ channel 是一种**引用类型**,

  ```go
  // 4. 管道的类型 (引用数据类型,改变副本会影响本身)
  ch1 := make(chan int, 4)
  ch1 <- 34
  ch1 <- 232 	
  ch2 := ch1
  <-ch2
  fmt.Printf("%v 长度: %v\n", ch1, len(ch1)) // 0xc00007c080 长度: 1 ,会影响 ch1 的值
  ```

+ 当管道内数据存满时发送**管道的阻塞** (存储超限,取出超限)

  + **无缓冲管道 (阻塞管道)** : 创建管道时没有指定容量

  ```go
  // 6. 管道阻塞
  ch4 := make(chan int, 4)
  for _, i2 := range []int{123, 24, 655, 64} {
      ch4 <- i2
  }
  //ch4 <- 242  // fatal error: all goroutines are asleep - deadlock!  死锁
  m1 := <- ch4
  m2 := <- ch4
  m3 := <- ch4
  m4 := <- ch4
  fmt.Println(m1, m2, m3, m4) // 123 24 655 64
  m5 := <- ch4
  fmt.Println(m5) // fatal error: all goroutines are asleep - deadlock!  死锁
  ```

  

+ 声明格式:

  ```go
  var 变量 chan 元素类型
  eg:
var ch1 chan int // 传递整数类型的管道
  var ch2 chan bool  // 传递布尔类型的管道
  var ch3 chan []int  // 传递 int 切片类型的管道
  ```
  
  

##### 8.2 创建 channel

+ 声明管道后需要使用 make 函数 初始化之后才可以使用

+ 管道内容量存满后,只有当管道内容量被取出时才可以再次存入

+ 创建 channel 的格式如下

  ```go
  make(chan 元素类型, 容量)
  ```

  

##### 8.3 channel 操作 

+ 管道有**发送 (send)**、**接收 (receive)** 和 **关闭 (close)** 三种操作

+ 发送和接收都使用 **<-** 符号

+ 先定义一个管道

  ```go
  ch := make(chan int, 3)
  ```

+ 三种操作

  1. **发送 (将数据放入管道内)**

     ```go
     ch <- 10 // 将 10 发送到 ch 管道内
     ```

  2. **接收 (从管道内取值)**

     ```go
     x := <- ch  // 从 ch 中接收值并赋值给变量 x
     <-ch  // 从 ch 中接收值，忽略结果
     ```

  3. **关闭管道**

     + 只有在通知接收方 goroutine 所有的数据都已经发送完毕的时候才需要关闭管道
     + 管道是可以被垃圾回收机制回收的

     ```go
     close(ch)
     ```

  4. **for range 循环遍历管道**

     + 循环遍历管道需要在遍历结束后关闭管道,否则取完管道内值之后报错死锁 `fatal error: all goroutines are asleep - deadlock!`

     + 如果用 for range 读取数据,写入完成后,一定要关闭管道 `close(ch)`

     + 循环遍历管道没有 key 值

       ```go
       /*
       管道的循环遍历以及关闭
       */
       
       ch := make(chan int, 10)
       
       for _, i2 := range []int{12,34,54,235,23,3,12,41,42,332} {
           ch <- i2
       }
       close(ch)
       for val := range ch {
           fmt.Println(val)
           //if len(ch) == 0 {
           //	close(ch)
           //}
       }
       /*
       12
       34
       54
       235
       23
       3
       12
       41
       42
       332
       */
       ```

     + 实例

       ```go
       	package main
       
       import "fmt"
       
       func main() {
       	// 1. 创建 channel
       	ch := make(chan int, 3)
       	// 2. 将数据存入管道
       	ch <- 20
       	ch <- 100
       	ch <- 123
       	// 3. 获取管道内容
       	a := <-ch
       	fmt.Println(a)
       	fmt.Println(<-ch)
       	c := <-ch
       	fmt.Println(c)
       	// 4. 管道的类型
       
       	// 5. 管道的容量和长度
       
       	// 6. 管道阻塞
       
       }
       ```

       

#### 9. Goroutine 结合 Channel 管道

+ 通过 goroutine 让 管道数据的读取和写入同步进行

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"sync"
  	"time"
  )
  
  var wg sync.WaitGroup
  
  func fn1(ch chan int)  {
  	// 将数据写入管道
  	for i:=1;i<=10;i++ {
  		ch <- i
  		fmt.Printf("写入数据 %v\n", i)
  		time.Sleep(time.Millisecond * 50)
  	}
  	close(ch)
  	wg.Done()
  }
  
  func fn2(ch chan int)  {
  	// 读取数据
  	for val := range ch {
  		fmt.Printf("读取数据 %v\n", val)
  		time.Sleep(time.Millisecond * 50)
  	}
  	wg.Done()
  }
  
  func main() {
  	ch := make(chan int, 10)
  	wg.Add(1)
  	go fn1(ch)
  	wg.Add(1)
  	go fn2(ch)
  	wg.Wait()
  	fmt.Println("退出")
  }
  /*
  写入数据 1
  读取数据 1
  写入数据 2
  读取数据 2
  写入数据 3
  读取数据 3
  写入数据 4
  读取数据 4
  写入数据 5
  读取数据 5
  写入数据 6
  读取数据 6
  写入数据 7
  读取数据 7
  写入数据 8
  读取数据 8
  写入数据 9
  读取数据 9
  写入数据 10
  读取数据 10
  退出
  */
  ```

  

#### 10. 单向管道

+ Golang 中默认管到为双向管道 (可读可写) `var chan1 chan int`

+ 定义只写管道 : `var chan2 chan <- int` 或 `ch2 := make(chan <- int, 2)`

  ```go
  // 定义只写管道
  ch2 := make(chan <- int, 2)
  ch2 <- 77
  ch2 <- 78
  //<-ch2  报错 <-ch2 (receive from send-only type chan<- int)
  ```

  

+ 定义只读管道 : `var chan3 <- chan int`

  ```go
  // 定义只读管道
  ch3 := make(<- chan int, 2)
  //ch3 <- 33  报错 ch3 <- 33 (send to receive-only type <-chan int) 只读管道
  fmt.Println(ch3)  // 0xc00001a150
  ```

  

#### 11. select 多路复用 

+ 多个通道接收数据 (如果没有数据可以接收就会发生阻塞)

+ **select** 类似于 switch 语句，它有一系列 case 分支 和一个默认的分支.每个 case 对应一个 管道的通信 (接收或发送) 过程. select 会一直等待, 直到某个 case 的通信操作完成后,就会执行 case 分支对应的语句

+ 结合 for 循环实现,使用 select 多路复用获取 chan 数据时不需要关闭 chan

+ 基本语法

  ```go
  select{
      case <- ch1:
      	...
      case data := <- ch2:
      	...
      case ch3 <- data:
      	...
      default:
      	默认操作
  }
  ```

+ 实例, 并行读取数据

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  /*
  多路复用 select
   */
  
  func main() {
  	// 定义一个管道 10 个 int 数据
  	intChan := make(chan int, 10)
  	for i := 0; i < 10; i ++ {
  		intChan <- i
  	}
  	// 定义一个管道 5 个数据 string
  	strChan := make(chan string, 5)
  	for i := 0; i < 5; i ++ {
  		strChan <- "Hello" + fmt.Sprintf("%d", i)
  	}
  
  	// 并行读取数据
  	// 1. 开多个协程
  	// 2. 使用多路复用 select
  
  	for {
  		select {
  		case ch1 := <- intChan:
  			fmt.Printf("从 intChan 中读取 %v\n", ch1)
  			time.Sleep(time.Millisecond*50)
  		case ch2 := <- strChan:
  			fmt.Printf("从 strChan 中读取 %v\n", ch2)
  			time.Sleep(time.Millisecond*50)
  		default:
  			fmt.Printf("数据读取完毕\n")
  			return
  		}
  	}
  
  }
  ```

  

#### 12. Golang 并发安全和锁

1. **互斥锁** : Golang 中互斥锁由标准库 **sync** 中的 **Mutex结构体类型** 表示

   1. `sync.Mutex` 类型只有两个公开的指针方法,**Lock** 和 **Unlock**.

      + **Lock** : 锁定当前的共享资源
      + **Unlock** : 进行解锁

   2. 对编写好的多协程进行编译并查看是否有竞争关系

      ```
      // 编译 go build -race main.go 查看是否有竞争关系
      报错,有两个竞争关系
      Found 2 data race(s)
      ```

   3. 对于有竞争关系的需要进行加锁 (互斥锁) 然后使其有序进行,加锁后就不会出现资源访问竞争问题

      ```go
      package main
      
      import (
      	"fmt"
      	"sync"
      	"time"
      )
      
      // 编译 go build -race main.go 查看是否有竞争关系
      
      var count = 0
      var wg sync.WaitGroup
      var mutex sync.Mutex
      
      func test()  {
      	// 有协程进行此程序后将资源锁住
      	mutex.Lock()
      	count ++
      	fmt.Println("count is : ", count)
      	time.Sleep(time.Millisecond * 50)
      	// 使用资源结束后将资源进行释放
      	mutex.Unlock()
      	wg.Done()
      }
      
      func main() {
      	for i := 0; i < 20 ; i ++ {
      		wg.Add(1)
      		go test()
      	}
      	wg.Wait()
      }
      ```

   4. 互斥锁**缺点** : 互斥锁的使用会降低程序的并发性能,使程序由并行执行变成了串行执行

2. **读写互斥锁** : 允许同时读数据，但是不允许同时写数据 (在 **写** 的时候进行互斥锁)

   1. **读写锁** : 可以让多个读操作并发,同时读取,但是对于写操作是完全互斥的。(当一个 协程 进行写操作时,其他协程即不可以进行读操作，也不可以进行写操作)

   2. Go 中读写锁 由 **结构体类型 sync.RWMutex** 表示，包含两种方法

      1. **写锁定 和 写解锁** : 对写操作进行锁定和解锁

         ```go
         func (*RWMutex)Lock()
         func (*RWMutex)Unlock()
         ```

         

      2. **读锁定 和 读解锁** : 对读操作进行锁定和解锁

         ```go
         func (*RWMutex)RLock()
         func (*RWMutex)RUnlock()
         ```

      3. 实例,读写操作

         ```go
         package main
         
         import (
         	"fmt"
         	"sync"
         	"time"
         )
         
         /*
         模拟操作数据库,设置读写锁
          */
         
         var wg sync.WaitGroup
         
         var mutex sync.RWMutex
         
         func write()  {
         	mutex.Lock()
         	fmt.Println("执行写操作")
         	time.Sleep(time.Second * 2)
         	mutex.Unlock()
         	wg.Done()
         }
         
         func read()  {
         	mutex.RLock()
         	fmt.Println("读操作")
         	time.Sleep(time.Second)
         	mutex.RUnlock()
         	wg.Done()
         }
         
         func main() {
         	// 10 个协程进行读
         	for i := 0; i < 10; i ++ {
         		wg.Add(1)
         		go read()
         	}
         	// 10 个协程进行写
         	for i := 0; i < 10; i ++ {
         		wg.Add(1)
         		go write()
         	}
         	wg.Wait()
         }
         ```

         

#### 13. Goroutine Recover 解决协程中出现的 Panic (恐慌)

+ 解决多协程中某一协程出现问题报错而影响其他协程的执行

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  /*
  Goroutine Recover 解决协程中出现的 Panic
  */
  
  func sayHello()  {
  	for i := 0; i < 10; i ++ {
  		time.Sleep(time.Millisecond * 50)
  		fmt.Println("hello, World.")
  	}
  }
  // 函数
  func test()  {
  	// 这里可以使用 defer + recover
  	defer func() {
  		// 定义一个匿名自执行函数
  		// 捕获 可能出现的 错误
  		if err := recover(); err != nil {
  			fmt.Println("test() 发生错误", err)
  		}
  	}()
  	// 定义一个 map
  	var myMap map[int]string
  	myMap[0] = "golang"  // error (panic: assignment to entry in nil map) 恐慌：分配到零映射中的条目
  }
  
  func main() {
  
  	go sayHello()
  	go test()
  
  	time.Sleep(time.Second)
  
  }
  /*
  test() 发生错误 assignment to entry in nil map
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  hello, World.
  */
  ```

  

