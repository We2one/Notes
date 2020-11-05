### Golang

#### Go 变量、变量命名规则

##### 变量声明

+ Go 语言中变量名由**字母**、**数字**、**下划线**组成,首个字符不能为数字.关键字和保留字都不能作为变量名.
+ Go 语言变量需要**声明后才可以使用**,同一作用域内不支持重复声明,并且 Go 语言变量声明后**必须使用** 

##### var 声明变量

+ 声明格式 : `var 变量名称 type = 变量值` 

+ type 可以省略 Go 将自动进行类型推导

  ```go
  var name string = "小王"
  fmt.Println(name)
  var isOk bool = true
  fmt.Println(isOk)
  var num int = 4
  fmt.Println(num)
  var test1 string
  fmt.Println(test1)
  var test2 bool
  fmt.Println(test2)
  var test3 int
  fmt.Println(test3)
  """
  小王
  true
  4
  
  false
  0
  """
  ```

+ 变量声明后没有赋值 `var 变量名称 type`

  + 字符串类型 为空
  + 整数类型 为 0
  + 布尔类型 为 false

+ 一次声明多个变量

  + 一次声明多个同类型变量

    ```go
    var a1, a2 string = "张三", "李四"
    fmt.Println(a1, a2)
    """
    张三 李四
    """
    ```

  + 一次声明多个不同类型变量

    ```go
    var (
    	name string
    	age int
    	sex string
    	live bool
    	)
    name = "老王"
    age = 10
    sex = "男"
    live = true
    fmt.Println(name, age, sex, live)
    """
    老王 10 男 true
    """
    var (
    	name string = "张三"
    	age int = 19
    	live bool = true
    	)
    	fmt.Println(name, age,  live)
    """
    张三 19 true
    """
    ```

    

##### 短变量声明法

+ `变量名 := 值` : 只能用于局部变量,在函数内部使用

  ```go
  name := "张三"
  fmt.Println(name)
  fmt.Printf("%T", name)
  """
  张三
  string
  """
  ```

  

+ 短变量一次声明多个变量

  ```go
  a,b,c := 12, true, "老张"
  fmt.Println(a, b, c)
  """
  12 true 老张
  """
  ```

##### 匿名变量

+ 匿名变量 : 在使用多重赋值时,如果想要忽略某个值,可以使用匿名变量 (anonymous variable)

+ 匿名变量不占用命名空间,不会分配内存,所以匿名变量之间不存在重复声明

+ 匿名变量格式 : `_变量名`

  ```go
  // 定义函数
  func getUserinfo() (string, int) {
  	return "张三", 10
  }
  func main()  {
  	// var username, age = getUserinfo()
  	// fmt.Println(username, age)
      var username, _ = getUserinfo()
  	fmt.Println(username)
  }
  /*
  //张三 10
  张三
  */
  ```

  

##### 变量赋值

+ `已定义变量名 = "新值"`

  ```
  var name string = "小王"
  name = "李四"
  fmt.Println(name)
  """
  李四
  """
  ```

#### Go 常量

+ Go 常量在整个程序运行期间都不会发生改变
+ 变量可以改变,常量不可以
+ 定义常量后必须赋值,不可以先定义后赋值

##### 常量声明

1. 使用 const 定义常量 `const 常量名 = 常量值`

2. 一次声明多个常量 (如果省略了值，则此变量名代表的值与上一行的相同)

   ```go
   const (
       username = "张三"
       password = 123456
       id
       uid
   )
   fmt.Println(username, password)
   fmt.Printf("username: %v\npassword: %v", username,password)
   /*
   张三 123456 123456 123456
   username: 张三
   password: 123456
   */
   ```

##### const 常量结合 iota 使用

+ iota 是 Golang 的常量计数器,只能在常量表达式中使用

+ iota 在 const 关键字出现时将被重置为 0 (const 内部第一行之前), const 中每新增一行常量声明将使 iota 技术一次 (乐意理解为 const 语句块中的行索引)

  ```go
  const a = iota // 0
  const(
  b = iota // 0
  c // 1
  )
  fmt.Println(a, b, c)
  ```

+ const iota 使用 `_` 跳过某些值

  ```go
  const a = iota // 0
  const(
      b = iota // 0
      c // 1
      _
      d // 3
  )
  fmt.Println(a, b, c, d)
  ```

+ iota 声明中插队

  ```go
  const(
      n1 = iota // 0
      n2 = 100 // 100
      n3 = iota // 2
      n4 // 3
  )
  const n5 = iota // 0
  fmt.Println(n1, n2, n3, n4, n5)	
  ```

+ 多个 iota 可以定义在一行

  ```go
  const (
      a, b = iota + 1, iota + 2 // 1, 2
      c, d // 2, 3
      e, f // 3, 4
  )
  fmt.Println(a,b,c,d,e,f)
  ```

#### Go 语言变量、常量命名规则

1. 变量名称必须由**数字**、**字母**、**下划线**组成
2. 标识符(变量名称)开头**不能是数字**
3. 标识符(变量名称)**不能是保留字和关键字**
4. 变量命名是区分大小写的,即使如此仍不建议用一个单词大小写区分两个变量
5. 常量建议全部大写 (建议)
6. 标识符(变量名称) 一定要见名知意 : 变量名建议使用名词,方法名称建议使用动词
7. 变量名称一般采用驼峰式 (变量名一个单词全小写,多个单词单词与单词首字母大写),当遇到特有名词 (缩写或简称, DNS) 的时候,特有名称根据是否私有全部大写或小写
   + 字母小写表示私有
   + 字母大写表示公有

#### Go 语言代码风格

1. 代码每一行结束后不用写分号 ";"

2. 运算符左右建议各加一个空格

3. Go 语言推荐使用驼峰命名法 (当命名由多个单词组成的时候优先使用大小写隔离)

   + 大驼峰 : 多个单词 (包括首单词的首字母) 的首字母都大写,在 Go 中代表公有
   + 小驼峰 : 多个单词 (不包括首单词的首字母) 的首字母大写,在 Go 中代表私有

4. 强制的代码风格

   + 左括号必须紧贴着语句不换行

5. `go fmt` : 格式化代码,让代码风格保持一致

   ```
   go fmt main.go
   ```

   

