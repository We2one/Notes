### Golang time 包 以及日期函数

#### 1. time 包

+ Golang 中所有与时间有关的都在 time 保中,time 包提供了时间的显示和测量用的函数

#### 2. time.Now() 获取当前时间

+ `timeObj := time.Now()` 方法

  | 方法               | 描述       |
  | ------------------ | ---------- |
  | `timeObj.Year()`   | 获取年份   |
  | `timeObj.Month()`  | 获取月份   |
  | `timeObj.Day()`    | 获取日期   |
  | `timeObj.Hour()`   | 获取小时   |
  | `timeObj.Minute()` | 获取分     |
  | `timeObj.Second()` | 获取秒数   |
  | `timeObj.Data()`   | 获取年月日 |

  

+ 获取当前时间 (02d 表示 不满两列前边用 0 填充)

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  	/*
  	获取当前时间
  	 */
  	now := time.Now()
  	fmt.Printf("当前时间为: %v\n", now)
  	/*
  	获取当前年月日
  
  	fmt.Println("年: ", now.Year())
  	fmt.Println("月: ", now.Month())
  	fmt.Println("日: ", now.Day())
  	fmt.Println("小时: ", now.Hour())
  	fmt.Println("分: ", now.Minute())
  	fmt.Println("秒: ", now.Second())
  	fmt.Println(now.Date())
  
  	 */
  	year := now.Year()
  	month := now.Month()
  	day := now.Day()
  	hour := now.Hour()
  	minute := now.Minute()
  	second := now.Second()
  	fmt.Printf("%d-%02d-%02d %02d:%02d:%02d", year, month, day, hour, minute, second)
      // 2020-10-27 19:35:18
  }
  
  
  // 当前时间为: 2020-10-27 19:10:47.2054201 +0800 CST m=+0.001994201
  // 年:  2020
  // 月:  October
  // 日:  27
  // 小时:  19
  // 分:  15
  // 秒:  26
  ```

  

#### 3. now.Format 格式化输出日期字符串

+ 时间类型有自带的 Format 方法进行格式化.
+ Go 语言中格式化时间模板不是常见的 Y-m-d H:M:S, 而是使用Go 的诞生时间 2006 年 1 月 2 日 15 点 04 分 ， 所以时间格式为 (2006 代表年、01 代表月、02代表日、03代表十二小时制的时 (15 代表 二十四小时制的时) 、04代表分、05代表秒)

+ 格式化输出

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  	/*
  	获取当前时间
  	 */
  	now := time.Now()
  	fmt.Printf("当前时间为: %v\n", now)
  	fmt.Println(now.Format("2006-01-02 03:04:05"))
      fmt.Println(now.Format("2006/01/02 03:04:05"))
  	fmt.Println(now.Format("2006/01/02 15:04:05"))
  }
  // 2020-10-27 07:45:20
  // 2020/10/27 07:45:20
  // 2020/10/27 19:45:20
  ```

  

#### 4. time.Now().Unix() 获取当前时间戳

+ 时间戳: 自 1970 年 1 月 1 日 (08:00:00 GMT) 至当前时间的秒数,也被称为 Unix 时间戳

+ 获取当前时间戳

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  	/*
  	获取当前时间
  	 */
  	now := time.Now()
  	fmt.Printf("当前时间为: %v\n", now)
  
  	/*
  	获取当前时间戳
  	 */
  	unixtime := now.Unix()  // 获取当前时间戳
  	unixNatime := now.UnixNano()  // 获取纳秒时间戳
  	fmt.Println(unixtime)
  	fmt.Println(unixNatime)
  }
  /*
  当前时间为: 2020-10-27 19:56:43.0952132 +0800 CST m=+0.002989601
  1603799803
  1603799803095213200
  */
  ```

  

#### 5. 时间戳转换为日期字符串 (年-月-日 时:分:秒)

+ 使用函数 
  1. 时间戳转 秒数 : `time.Unix(int64(时间戳), 0)`
  2. 时间戳转纳秒数 : `time.Unix(0, int64(时间戳))`

+ 时间戳转换

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  
  	/*
  	时间戳转换为日期对象
  	 */
  
  	unixTime := 1603799803  // 时间戳
  	timeObj := time.Unix(int64(unixTime), 0)
  	var str = timeObj.Format("2006-01-02 15:04:05")
  	fmt.Println(str)
  }
  // 2020-10-27 19:56:43
  ```

  

#### 6. 日期字符串转换成时间戳

+ 使用函数

  1. 使用 `ParseInLocation()` 将 时间类型后添加时区等，转化为日期对象
  2. 使用 `Unix()` 将日起对象转化为时间戳

+ 日期字符串转换

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  
  	/*
  	日期字符串转换为时间戳
  	 */
  	t1 := "2020-10-27 19:56:43"  // 字符串
  	timeTemplate := "2006-01-02 15:04:05"  // 常规类型
  	stamp,_ := time.ParseInLocation(timeTemplate, t1, time.Local)
  
  	fmt.Println(stamp)  // 2020-10-27 19:56:43 +0800 CST
  	fmt.Println(stamp.Unix())  // 1603799803
  }
  ```

  

#### 7. 时间间隔

+ 使用函数

  1. `time.Duration` : 代表两个时间点之间的经过时间,单位为 **纳秒**, 

  2. 表示一段时间间隔,可表示最长时间段大约 290 年

  3. time 包中定义的时间间隔类型的常量为

     ​	

     | 常量                             | 描述    |
     | -------------------------------- | ------- |
     | `Nanosecond	Duration	= 1`  | // 纳秒 |
     | `Microsecond = 1000 *Nanosecond` | // 微秒 |
     | `Millisecond = 1000*Microsecond` | // 毫秒 |
     | `Second	= 1000 * Millisecond` | // 秒   |
     | `Minute	= 60 * Second`        | // 分   |
     | `Hour = 60 * Minute`             | // 小时 |

+ 时间间隔

  ```go
  package main
  
  import (
  	"fmt"
  	"time"
  )
  
  func main() {
  
  	/*
  	time 包中定义的时间间隔类型的常量为
  		const (
  			Nanosecond	Duration	= 1  // 纳秒
  			Microsecond 			= 1000 * Nanosecond   // 微秒
  			Millisecond				= 1000 * Microsecond  // 毫秒
  			Second					= 1000 * Millisecond  // 秒
  			Minute					= 60 * Second  // 分
  			Hour					= 60 * Minute  // 小时
  		)
  	 */
  
  	fmt.Println(time.Millisecond)  // 毫秒 1ms
  	fmt.Println(time.Microsecond)  // 微秒 1µs
  	fmt.Println(time.Second)  // 秒 1s
  ```

  

#### 8. 时间操作函数

1. Add 方法 : 时间 + 时间间隔操作, 也可以直接通过 "+" 实现

   + 定义格式 : `func (t time) Add(d Duration) Time`

   + 实例

     ```go
     package main
     
     import (
     	"fmt"
     	"time"
     )
     
     func main() {
     
     	var timeObj = time.Now()
     
     	fmt.Println(timeObj)
     
     	timeObj = timeObj.Add(time.Hour)
     
     	fmt.Println(timeObj)
     }
     /*
     2020-10-27 20:29:47.6802421 +0800 CST m=+0.004998701
     2020-10-27 21:29:47.6802421 +0800 CST m=+3600.004998701
     */
     ```

     

2. Sub 方法 : 求两个时间的差值

   + 定义格式 : `func (t time) Sub(u Time) Duration`
   + 返回一个时间段 t-u,如果结果超出了 Duration 可以表示的最大值或最小值,将返回最大值/最小值.获取时间点 t-d 可以使用 t.Add(-d)

3. Equal 方法 : 判断两个时间是否相同,受时区影响

   + 定义格式 : `func (t Time) Equal(u Time) bool`
   +  方法类似于 直接对两段时间进行 "==" 对比，但是此方法会儿额外比对地点和时区

4. `time.Sleep(间隔时间)` : 休眠指定时间1

#### 9. 定时器

1. 使用 `time.NewwTicker(时间间隔)` 来设定定时器

   ```go
   package main
   
   import (
   	"fmt"
   	"time"
   )
   
   func main() {
   
   	/*
   	time.NewwTicker(时间间隔) 设置定时器
   	 */
   
   	ticker := time.NewTicker(time.Second)  // 定义间隔为1s 的定时器
   
   	n := 0
   
   	for i := range ticker.C {
   		fmt.Println(i)
   		n++
   		if n > 5 {
   			ticker.Stop()
   			return
   		}
   	}
   }
   /*
   2020-10-27 20:35:36.3778328 +0800 CST m=+1.003519601
   2020-10-27 20:35:37.3915592 +0800 CST m=+2.017246001
   2020-10-27 20:35:38.3775131 +0800 CST m=+3.003199901
   2020-10-27 20:35:39.3890244 +0800 CST m=+4.014711201
   2020-10-27 20:35:40.3780016 +0800 CST m=+5.003688401
   2020-10-27 20:35:41.3904777 +0800 CST m=+6.016164501
   */
   ```

   

2. 使用 `time.Sleep(time.Second)` 在死循环中来实现定时器

   ```go
   package main
   
   import (
   	"fmt"
   	"time"
   )
   
   func main() {
   
   	/*
   	time.Sleep(time.Second) 实现定时器
   	 */
   	for {
   		time.Sleep(time.Second)
   		fmt.Println("死循环执行任务")
   	}
       fmt.Println("第一秒")
   	time.Sleep(time.Second)
   	fmt.Println("第二秒")
   	time.Sleep(time.Second)
   	fmt.Println("第三秒")
   	time.Sleep(time.Second)
   	fmt.Println("第四秒")
   	time.Sleep(time.Second)
   }
   /*
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   死循环执行任务
   ...
   */
   ```

   



