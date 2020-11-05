### Golang 中的指针

#### 1. 关于指针

+ 指针 : 也是一个变量 (**引用数据类型**,必须有存储空间) ,是一种特殊的变量,它存储的数据不是一个普通的值,而是另一个变量的内存地址
+ 指针指向内存存储的数据指向变量所存储的数据的位置，指针的值是变量的地址
+ 指针类型 `*int`

#### 2. 指针地址和指针类型

+ Go 语言中使用 `&` 字符放在变量前面对变量进行 **取地址** 操作.

+ Go 语言中值的类型 (`int`、`float`、`bool`、`string`、`array`、`struct`) 以及其对应的指针类型(`*int`、`*float、`*string`)

+ 取变量指针的语法 : `ptr := &v`

  + **v** : 代表被取地址的变量
  + **ptr** : 用于接收地址的变量,ptr 的类型为 `*T`，称作 T 的指针类型 , `*` 代表指针

+ 实例

  ```go
  /*
  指针地址以及指针地址
  */
  
  var a float64 = 23.32
  var p = &a
  
  fmt.Printf("a的值: %v, a 的类型: %T, a 的地址: %v\n", a, a, p)
  
  fmt.Printf("p的值: %v, p 的类型: %T", p, p)
  fmt.Println(*p)
  
  /*
  a的值: 23.32, a 的类型: float64, a 的地址: 0xc00000a0a0
  p的值: 0xc00000a0a0, p 的类型: *float64
  23.32
  */
  ```

  

#### 3. 指针取值

+ 指针取值语法 : `*ptr` 取出指针指向的变量的值

+ 变量、指针地址、指针变量、取地址、取值的相互关系和特性

  + 取地址 (`&`) : 对变量进行取地址操作,可以获得这个变量的指针变量
  + 指针变量的值是指针地址
  + 取值 (`*`) : 对指针变量进行取值操作,可以获得指针变量指向的原变量的值 

+ `*ptr = value` : 可以直接改变指针指向变量的值

  ```go
  package main
  
  import "fmt"
  
  func main()  {
  
  	var a float64 = 23.32
  	var p = &a
  
  	fmt.Println(*p) // 23.32
  	*p = 55.555
  	fmt.Println(a)  // 55.555
  }
  
  ```

+ 改变指针对应地址的值

  ```go
  package main
  
  import "fmt"
  
  func fn1(x int) {
  	x = 10
  }
  
  func fn2(x *int)  {
  	*x = 40
  }
  
  func main() {
  	var a = 5
  	fn1(a)
  	fmt.Println(a)  // 5
  	fn2(&a)
  	fmt.Println(a)  // 40
  }
  ```

  

#### 4. 指针传值

#### 5. new 和 make

1. 对于 **map/切片** 数据类型必须使用 make() **创建内存空间**才可进行操作 (切片可以通过 append 扩容)

   ```go
   package main
   
   import "fmt"
   
   func main() {
   	var userinfo = make(map[string]string)
   	userinfo["username"] = "张三"
   	fmt.Println(userinfo)
   	var a = make([]int, 4, 4)
   	a[1] = 12
   	fmt.Println(a)
   }
   /*
   map[username:张三]
   [0 12 0 0]
   */
   ```

2. new 函数分配内存

   + 函数签名为 : `func new(Type) *Type`

     1. `Type` 表示类型,new 函数中接收一个参数,这个参数是一个类型
     2. `*Type` 表示类型指针, new 函数返回一个指向该类型内存地址的指针
     3. 使用 new 函数得到的是一个类型的指针,该指针对应的值为该类型的0值

   + 函数实例

     ```go
     package main
     
     import "fmt"
     
     func main() {
     	/*
     	new 函数 分配内存
     	 */
     
     	a := new(int)  // a 是一个int指针类型,并且分配存储空间
     	b := new(bool)  // b 是一个 bool 指针类型,并且分配存储空间
     	fmt.Printf("a的类型为: %T, a 的存储空间为: %v, a指向的值为: %v\n", a, a, *a)
     	fmt.Printf("b的类型为: %T, b 的存储空间为: %v, b指向的值为: %v", b, b, *b)
         /*
     	new 方法给指针变量分配存储空间
     	 */
     	//var a *int
     	var b = new(int)
     	*b = 100
     	fmt.Println(*b)  // 100
     
     }
     /*
     a的类型为: *int, a 的存储空间为: 0xc00000a0a0, a指向的值为: 0
     b的类型为: *bool, b 的存储空间为: 0xc00000a0a8, b指向的值为: false
     */
     ```

3. make 函数分配内存

   + make 函数 只用于 slice(切片), map (类似于字典), channel (通道) 的内存创建,而且返回的类型是三个**类型本身**,不是指针类型,因为三种类型就是引用类型,所以不必返回指针
   + make 函数签名 : `func make(t Type, size ...integerType) Type {}`
   + make 在创建 slice, map, channel 时是不可替代的

4. make 与 new 的区别

   1. 二者都是用来分配内存的
   2. make 只适用于 slice、map、channel 的初始化,还是返回这三个引用的本身
   3. new 用于类型内存的引用,并且内存对应的值为类型 零 值,返回的是指向类型的指针.