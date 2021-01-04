### Golang 函数详解

#### 1. 函数定义

1. 函数定义 : 函数是组织好的、可重复使用的、用于执行指定任务的代码块

2. Go 语言中支持 : 函数、匿名函数、闭包

3. Go 语言中定义函数使用 func 关键字,具体格式:

   ```go
   func 函数名(参数及参数类型)(返回值类型){
       函数体
   }
   ```

   + 函数名 : 由字母、数字、下划线组成.函数名第一个字母不能是数字.同一个包内,函数名也不可重复.
   + 函数参数及参数类型 : 多个参数之前用 **,** 分隔
   + 返回值变量和变量类型 : 多个返回值必须由 () 包裹 并用 **,** 分隔
   + 函数体 : 实现指定功能的代码块

#### 2. 函数的调用

1. 没有参数没有返回值

   ```go
   func test() {
       fmt.println("无参数和返回值,调用时输出固定值")
   }
   ```

   

2. 有参数没有返回值

   ```go
   func test(a, b int) {
       if a == b {
           fmt.Println('a==b')
       }
   }
   ```

   

3. 有参数和返回值

   ```go
   func 函数名(参数及参数类型)(返回值类型){
       函数体
   }
   ```

   

#### 3. 函数参数

1. 传入参数类型相同 : 参数的简写如果 x, y 类型相同 可以 只输入 y 的类型 (只能简写前面的，无法简写后面的) `func subFn(x, y int)`

   ```go
   func subFn(x int, y int) int  {
   	sub := x - y
   	return sub
   }
   func subFn1(x, y int) int  {
   	sub := x - y
   	return sub
   }
   ```

2. 可变参数 : 函数的可变参数 (可变参数: 函数的参数数量不固定, 必需放在最后),传入多个参数, x 为一个切片,循环遍历求和

   ```go
   func sumFn1(x ... int) int {
   	fmt.Printf("%v -- %T\n",x,x) // [1 2 3] -- []int
   	sum2 := 0
   	for _,v := range x{
   		sum2 += v
   	}
   	return sum2
   }
   ```

   

3. 可变参数与 固定参数 混合编写: 第一个参数赋值给 x， 后面其他参数赋值给 y

   ```go
   func sumFn2(x int, y ... int) int {
   	fmt.Printf("x = %v, y= %v --- %T\n", x, y, y) // x = 2, y= [6 7 4] --- []int
   	sum3 := x
   	for _, v := range y {
   		sum3 += v
   	}
   	return sum3
   }
   ```

#### 4. 函数的返回值

1. 只有一个返回值 : 返回值类型可以不在 括号内

   ```go
   func sumFn(x int, y int)(int)  {
   	sum := x + y
   	return sum
   }
   ```

2. return 关键词一次可以返回多个值 : 返回类型需要括起来,并且与括号内对应类型相同

   ```go
   package main
   
   import "fmt"
   
   // return 关键词一次可以返回多个值, 返回类型需要括起来,并且与括号内对应类型相同
   func calc(x, y int) (int, int) {
   	sum := x + y
   	sub := x - y
   	return sum, sub
   }
   
   func main()  {
   	fmt.Println(calc(34, 12)) // 46 22
   }
   
   ```

3. 返回值命名法: (return 关键词一次返回多个值的另一种写法) 函数定义时直接给返回值命名,在函数体中直接使用这些变量,最后 return 返回

   ```go
   package main
   
   import "fmt"
   
   // return 关键词一次返回对个值的另一种写法: 返回值命名法: 函数定义时直接给返回值命名,在函数体中直接使用这些变量,最后 return 返回
   func calc1(x, y int) (sum int, sub int) {
   	sum = x + y
   	sub = x - y
   	return
   }
   
   func main()  {
   	a, b := calc1(34, 12)
   	fmt.Println(a, b)  // 46 22
   }
   ```

4. 第三种写法 : 返回值类型相同时只写最后一个返回值的类型

   ```go
   package main
   
   import "fmt"
   
   // 第三种写法 : 返回值类型相同时只写最后一个返回值的类型
   func calc2(x, y int) (sum, sub int) {
   	sum = x + y
   	sub = x - y
   	return
   }
   
   func main()  {
   	a, b := calc2(34, 12)
   	fmt.Println(a, b)  // 46 22
   }
   ```


#### 5. 函数变量作用域

1. 仅获取需要的返回值,不需要的用 **_** 代替

   ```go
   package main
   
   import "fmt"
   
   // 第三种写法 : 返回值类型相同时只写最后一个返回值的类型
   func calc2(x, y int) (sum, sub int) {
   	sum = x + y
   	sub = x - y
   	return
   }
   
   func main()  {
   	// 仅获取需要的返回值,不需要的用 _ 代替
   	a, _ := calc2(34, 12)
   	fmt.Println(a)  // 46
   }
   ```


#### 6. 函数类型与变量

1. 定义函数类型

   + 我们可以使用 type 关键字来定义一个函数类型

   + 定义一个 **calulation** 函数类型,接受两个 int 类型的参数 并且返回一个 int 类型的返回值 (凡是满足这个条件的函数都是 calculation 类型的函数 ); 具体格式

     ```go
     type calculation func(int, int) int
     ```

2. 自定义函数类型

   ```go
   package main
   
   import "fmt"
   
   type calc func(int, int) int
   
   func add(x, y int) int {
   	return x+y
   }
   
   func main() {
   	var c calc
   	c = add  // add 必须满足 calc 类型才可以进行操作
   	fmt.Printf("c 的类型: %T\n", c)  // c 的类型: main.calc
   	var num = c(10, 5)
   	fmt.Println(num) // 15
   
   	f := add  // 不给 f 指定类型
   	fmt.Printf("f 的类型 %T\n", f)  // f 的类型 func(int, int) int
   	fmt.Println(f(10, 4)) // 14
   }
   ```

   

3. 自定义常量类型 (进行计算时 需要进行类型转换)

   ```go
   package main
   
   import "fmt"
   
   type myInt int
   
   func main() {
   	// 自定义类型
   	var a int = 10
   	var b myInt = 20
   	fmt.Printf("a 的类型 %T \t b 的类型 %T \n",a, b)  // a 的类型 int 	 b 的类型 main.myInt
   	fmt.Println(a + int(b))  // 30
   }
   ```

#### 7. 高阶函数

1. 函数作为另一个函数的参数 (也可以使用 匿名函数 传递)

   ```go
   package main
   
   import "fmt"
   
   func add(x, y int) int {
   	return x+y
   }
   
   func sub(x, y int) int {
   	return x - y
   }
   
   // 定义一个方法类型
   type calcType func(int, int) int
   
   func calc(x, y int, cb calcType) int {
   	return cb(x, y)
   }
   
   func main() {
       
   	// 传入函数作为参数
   	fmt.Println(calc(10, 5, add)) // 15
   	
       // 匿名函数运算
       fmt.Println(calc(2, 5, func(i int, i2 int) int {
   		return i * i2
   	}))  // 10
       
   }
   ```

2. 函数作为另一个函数返回值

   ```go
   package main
   
   import "fmt"
   
   type myInt int
   
   func add(x, y int) int {
   	return x+y
   }
   
   func sub(x, y int) int {
   	return x - y
   }
   
   type calcType func(int, int) int
   
   // 定义一个方法类型,返回此方法类型
   func do(o string) calcType {
   	switch o {
   	case "+":
   		return add
   	case "-":
   		return sub
   	case "*":
   		return func(i int, i2 int) int {
   			return i * i2
   		}
   	default:
   		return nil
   	}
   }
   
   func main() {
   
   	var a = do("+")
   	fmt.Println(a(10, 2)) // 12
   	var b = do("-")
   	fmt.Println(b(8, 4))  // 4
   	var c = do("*")
   	fmt.Println(c(2, 6))  // 12
   
   }
   ```

   

#### 8. 匿名函数和闭包

1. 匿名函数 : 没有函数名的函数, 匿名函数调用需要保存在某个 **变量** 或者 作为**立即执行的函数**

2. 定义格式 : 

   ```go
   func(参数) 返回值 {
       函数体
   }
   ```

3. 匿名自执行函数 : 将函数后添加 () 最为执行

   ```go
   package main
   
   import "fmt"
   
   func main() {
   	
       // 匿名自执行函数
   	func () {
   		fmt.Println("test ... ")
   	}()
       
       // 匿名自执行函数接收参数
       func (x, y int) {
   		fmt.Println(x + y)  // 39
   	}(10, 29)  
   
   }
   ```

4. 匿名函数: 保存在某个变量中

   ```go
   package main
   
   import "fmt"
   
   func main() {
   
   	var fn = func(x, y int) int {
   		return x + y
   	}
   
   	fmt.Println(fn(1,4))  // 5
   
   }
   ```

#### 9. defer 语句

+ defer 语句 会将其后面跟随的语句进行延迟处理.

+ 在 defer 归属的函数即将返回时,将延迟处理的语句按 defer 定义的逆序进行执行. <==>  先被 defer 的语句 最后被执行,最后被 defer 的语句最先被执行

+ defer 执行时机 (返回值赋值操作后, RET 指令执行前)

  + return 执行操作 (GO return 语句不是底层原子操作)分为两步
    1. 返回值赋值
    2. RET 指令

+ defer 使用演示

  ```go
  package main
  
  import "fmt"
  
  func main()  {
  	defer fmt.Println("你好")
  	defer fmt.Println("我很好")
  	/*
  	我很好
  	你好
  	 */
  }
  ```

+ 定义一系列的延迟执行函数时可以在 匿名函数内定义

  ```go
  package main
  
  import "fmt"
  
  func f1()  {
  	fmt.Println("开始")
  	
      // 匿名自执行方法
  	defer func() {
  		fmt.Println("aaaaa")
  		fmt.Println("bbbbb")
  		fmt.Println("cccccc")
  	}()
  
  	fmt.Println("结束")
  
  }
  
  func main()  {
  	f1()
  }
  /*
  开始
  结束
  aaaaa
  bbbbb
  cccccc
  */
  ```

  

+ defer 在命名返回值 (返回的是延迟执行前的值) 和匿名返回函数中变现不一样

  ```go
  package main
  
  import "fmt"
  
  func f2() int {
      // 命名返回值
  	var a int
  
  	defer func() {
  		a ++
  	}()
  
  	//fmt.Println("结束")
  	return a
  }
  
  func f3() (a int) {
      // 匿名返回值
  	defer func() {
  		a++
  	}()
  	return a
  }
  
  func f4() (a int) {
  	defer func() {
  		a++
  	}()
  	// 5 赋值给 a --> a ++ --> 返回 6
  	return 5
  }
  
  func main()  {
  	fmt.Println(f2())  // 0
      fmt.Println(f3())  // 1
      fmt.Println(f4())  // 6
  }
  ```

+ defer 注册要延时执行的函数时该函数的所有参数都需要确定其值

  ```go
  package main
  
  import "fmt"
  
  func f6() (x int) {
  	defer func(x int) {
          fmt.Println(x)  // 0
  		x++
  	}(x)
      fmt.Println(x)  // 0
  	return 5
  }
  
  func main()  {
  	fmt.Println(f6())  // 5
  }
  
  ```

+ defer 注册 (注册时已经计算好函数内使用的值) 与执行 (执行时倒序执行) 顺序分析

  ```go
  package main
  
  import "fmt"
  
  func calc(index string, a, b int) int {
  	ret := a + b
  	fmt.Println("calc:\t" + index, a, b, ret)
  	return ret
  }
  
  func main()  {
  	/*
  	注册顺序
  		defer calc("AA", x, calc("A", x, y))
  			
  		defer calc("BB", x, calc("B", x, y))
  			
  	执行顺序
  		1. 运行 calc("A", x, y)
  		2. 运行 calc("B", x, y)
  		3. defer calc("BB", x, calc("B", x, y))
  		4. defer calc("AA", x, calc("A", x, y))
  	 */
  
  	x := 1
  	y := 2
  	defer calc("AA", x, calc("A", x, y))
  	x = 10
  	defer calc("BB", x, calc("B", x, y))
  	y = 20
  }
  ```

#### 10. 内置函数 panic/recover

+ 内置函数

  | 内置函数         | 描述                                            |
  | ---------------- | ----------------------------------------------- |
  | close            | 主要用于关闭 channel                            |
  | len              | 用来求长度 (string, array, slice, map, channel) |
  | new              | 用来分配内存,主要用来分配值类型,返回的是指针    |
  | make             | 用来分配内存,主要用来分配引用类型               |
  | append           | 用来追加元素到数组                              |
  | panic 和 recover | 做错误处理                                      |

+ Go1.12 目前是没有异常机制的,但是使用 panic/recover 模式处理错误,结合使用

  1. panic : 可以在**任何地方**引用

     ```go
     package main
     
     import "fmt"
     
     func fn1()  {
     	fmt.Println("fn1...")
     }
     
     func fn2()  {
     	panic("掏出一个异常")
     }
     
     func main() {
     	/*
     	panic / recover
     	 */
     	fn1()
     	fn2()
     	fmt.Println("结束")
     }
     /*
     fn1...
     panic: 掏出一个异常
     
     goroutine 1 [running]:
     */
     ```

     

  2. recover : 只有在 **defer 调用的函数**中有效

     ```go
     package main
     
     import "fmt"
     
     func fn1()  {
     	fmt.Println("fn1...")
     }
     
     func fn2()  {
     	defer func() {
     		err := recover()
     		if err != nil {
     			fmt.Println("recover", err)
     		}
     
     	}()
     	panic("掏出一个异常")
     }
     
     func main() {
     	/*
     	panic / recover
     	 */
     	fn1()
     	fn2()
     	fmt.Println("结束")
     }
     /*
     fn1...
     recover 掏出一个异常
     结束
     */
     ```

+ GoLang 中异常捕获 (捕获异常后不再报错 而是继续执行)

  ```go
  package main
  
  import "fmt"
  
  func fn1(a, b int) int {
  	defer func() {
  		err := recover()
  		if err != nil{
  			fmt.Println("出现错误error: ", err)
  		}
  	}()
  	return a/b
  }
  
  func main() {
  	fmt.Println(fn1(10, 0))
  	fmt.Println("结束")
  }
  /*
  出现错误error:  runtime error: integer divide by zero
  0
  结束
  */
  ```

+ defer、panic、recover 结合使用抛出异常


  