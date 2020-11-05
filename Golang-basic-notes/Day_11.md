### GoLang 中的结构体

#### 1. 关于 GoLang 结构体

+ GoLang 中没有 **类** 的概念。GoLang 中的结构体 类似于 其他语言的类，并且有更高的**拓展性**和**灵活性**
+ 当为我们需要表达一个事务的全部或部分属性时, 单一的基础数据类型无法满足需求.就需要使用 GoLang 的自定义数据类型,可以封装多个基本数据类型 ---- 结构体 (struct)

#### 2. GoLang type 关键词自定义类型和类型别名

##### 2.1 自定义类型

+ 使用 type 关键字定义自定义类型 : `type myint int`
  + 将 myint 定义为 int 类型,通过 type 关键字定义, myint 是一种新的类型 具有 int 的特性

##### 2.2 类型别名 (Golang 1.9 之后添加)

+ **类型别名规定** : TypeAlias 只是 Type 的别名 `type TypeAlias = Type`

+ 例如 rune、byte 就是类型别名,底层定义:

  ```go
  type byte = uint8
  type rune = int32
  ```

##### 2.3 自定义类型和类型别名的区别

+ 区别
  + 自定义类型 : `type myInt int` 将定义变量的类型转换为 定义类型名的类型
  + 类型别名 : `type MyFloat = float32` 定义变量的类型仍是 定义的类型

+ 区别示例

  ```go
  package main
  
  import "fmt"
  
  type myInt int
  
  type myFloat = float64
  
  func main() {
      
  	var a myInt = 10
  
  	fmt.Printf("%v %T\n", a, a)
  
  	var b myFloat = 12.33
  
  	fmt.Printf("%v  %T\n", b, b)
  
  }
  /*
  10 main.myInt
  12.33  float64
  */
  ```

  

#### 3. 结构体定义和初始化的几种方法

##### 3.1 结构体的定义

+ 使用 type 和 struct 关键字来定义结构体

  ```go
  type 类型名 struct {
      字段名 字段类型
      字段名 字段类型
      ...
  }
  ```

  + 类型名 : 表示自定义结构体的名称,在同一个包内不可重复 (**首字母小写**表示为私有结构体 仅在此包内有用,**首字母大写**表示为公有结构体,在其他包内也有用)
  + 字段名 : 结构体内字段名必须唯一
  + 字段类型 : 结构体字段的具体类型

##### 3.2 实例化结构体 (只有实例化后才能分配内存,不赋值则默认为空)

1. 使用 var 关键字 声明结构体类型 : `var 结构体实例 结构体类型`

   ```go
   package main
   
   import "fmt"
   
   type Person struct {
   	name string
   	age int
   	gender string
   }
   
   func main() {
   
   	/*
   	第一种实例化结构体方法
   	 */
   
   	var person Person
   
   	person.name = "张三"
   	person.age = 18
   	person.gender = "男"
   	fmt.Printf("person=%v\n", person)
   	fmt.Printf("person=%#v\n", person)
   }
   /*
   person={张三 18 男}
   person=main.Person{name:"张三", age:18, gender:"男"}
   */
   ```

   

2. 通过 **new** 关键字 对结构体进行实例化 --> 得到的是 结构体的地址 (&结构体 : 可以对结构体指针直接使用结构体变量设置结构体属性) 

   ```go
   package main
   
   import "fmt"
   
   type Person struct {
   	name string
   	age int
   	gender string
   }
   
   func main() {
   
   	/*
   	第二种实例化结构体方法
   	 */
   
   	var person = new(Person)
   	person.name = "李四"
   	person.gender = "男"
   	(*person).age = 22
   	fmt.Printf("person=%v\n", *person)
   	fmt.Printf("person=%#v\n", *person)
   	
   }
   /*
   person={李四 22 男}
   person=main.Person{name:"李四", age:22, gender:"男"}
   */
   ```

3. 使用 **&** 对结构体进行**取地址**操作相当于对该结构体进行了一次 new 实例化操作 --> 得到的是 结构体的地址

   ```go
   package main
   
   import "fmt"
   
   type Person struct {
   	name string
   	age int
   	gender string
   }
   
   func main() {
   
   	/*
   	第三种实例化结构体方法
   	 */
   
   	person := &Person{name: "王二", age: 19, gender: "男"}
   	person.age = 57
   	fmt.Printf("person=%v\n", *person)
   	fmt.Printf("person=%#v\n", *person)
   
   }
   /*
   person={王二 57 男}
   person=main.Person{name:"王二", age:57, gender:"男"}
   */
   ```

4. **键值对初始化**实例结构体

   ```go
   package main
   
   import "fmt"
   
   type Person struct {
   	name string
   	age int
   	gender string
   }
   
   func main() {
   
   	/*
   	第四种实例化结构体方法
   	 */
   
   	var person = Person{
   		name: "宋玲",
   		age: 19,
   		gender: "女",
   	}
   	fmt.Printf("person=%v\n", person)
   	fmt.Printf("person=%#v\n", person)
   
   }
   /*
   person={宋玲 19 女}
   person=main.Person{name:"宋玲", age:19, gender:"女"}
   */
   ```

5. 初始化时不写键直接传值 (**传入值会与定义中一一对应**)  --> 得到的是 结构体的地址

   ```go
   package main
   
   import "fmt"
   
   type Person struct {
   	name string
   	age int
   	gender string
   }
   
   func main() {
   
   	/*
   	第五种实例化结构体方法
   	*/
   
   	person := &Person{
   		"孙二",
   		78,
   		"男",
   	}
   
   	fmt.Printf("person=%v\n", person)
   	fmt.Printf("person=%#v\n", person)
   	fmt.Printf("person=%v\n", *person)
   	fmt.Printf("person=%#v\n", *person)
   }
   /*
   person=&{孙二 78 男}
   person=&main.Person{name:"孙二", age:78, gender:"男"}
   person={孙二 78 男}
   person=main.Person{name:"孙二", age:78, gender:"男"}
   */
   ```

#### 4. 结构体方法和接收者

+ Go 语言中 没有类的概念 但是看可以给类型 (结构体、自定义类型) 定义方法。方法就是定义了接收者的函数,接收者的概念类似于其他语言中的 self 和 this

+ 方法的定义格式

  ```go
  func (接收者变量 接收者类型) 方法名(参数列表)(返回参数){
      函数体
  }
  ```

  + **接收者变量** : 接收者中的参数变量名命名时,官方建议使用接收者类型名的第一个小写字母,而不是 self 或 this .例如 Person 类型的接收者变量命名为 p
  + **接收者类型** : 接收者类型和参数类似,可以是**指针类型**和**非指针类型**
    + 指针类型的接收者 : 表示要修改结构体类型的属性
    + 非指针类型的接收者 : 表示获取结构体内数据
  + **方法名、参数列表、返回参数** : 与函数定义相同

+ 实例

  ```go
  package main
  
  import "fmt"
  
  type Person struct {
  	Name string
  	age int
  	gender string
  }
  
  func (p Person) printName()  {
  	fmt.Println("姓名: ", p.Name)
  }
  
  func (p Person) printAge()  {
  	fmt.Println("Age: ", p.age)
  }
  
  // 指针类型的接收者
  func (p *Person) setInfo(name string, age int, gender string) {
  	p.Name = name
  	p.age = age
  	p.gender = gender
  }
  
  func main() {
  	var person = Person{
  		Name: "张三",
  		age: 18,
  		gender: "男",
  	}
  	person.printName()
  	person.printAge()
  
  	ps := new(Person)
  	ps.Name = "王文武"
  	ps.age = 18
  	ps.gender = "男"
  	fmt.Println(ps)  // &{王文武 18 男}  指针类型
  	ps.printAge()
  	ps.printName()
  
  	ps.setInfo("孙思", 78, "男")
  	ps.printName()
  
  }
  
  /*
  姓名:  张三
  Age:  18
  &{王文武 18 男}
  Age:  18
  姓名:  王文武
  姓名:  孙思
  */
  ```

#### 5. 给任意类型添加方法

+ Go 语言中 接收者的类型可以是任何类型,不仅仅是结构体,任何类型都可以拥有方法.

+ 不能给其他包的类型定义方法

+ 例如 : 使用 type 定义 myInt 类型，然后给其添加方法

  ```go
  package main
  
  import "fmt"
  
  type myInt int
  
  func (m myInt) printType()  {
  	fmt.Println("myInt 类型是 int")
  }
  
  func main() {
  	var a myInt
  	a.printType()
  }
  /*
  myInt 类型是 int
  */
  ```

 #### 6. 结构体的匿名字段

+ 结构体允许其他成员字段在声明时没有字段名而**只有类型** (类型必须为唯一的),这种没有没名字的字段称为匿名字段

+ 实例

  ```go
  import "fmt"
  
  type Person struct {
  	string
  	int
  }
  
  func main() {
  	person := Person{
  		"张三",
  		78,
  	}
  	fmt.Println(person)
  }
  /*
  {张三 78}
  */
  ```

  

#### 7. 嵌套结构体

+ 结构体的字段类型可以是: 基本数据类型、切片、Map、结构体

+ 如果结构体的字段类型是: 指针、slice、map这类零值为 nil 的使用前需要先 make

+ 为结构体内部 切片、Map 赋值

  1. 直接赋值

     ```go
     package main
     
     import "fmt"
     
     type Person struct {
     	name string
     	age int
     	hobby []string
     	map1 map[string]string
     }
     
     func main() {
     	var p = Person{
     		name: "张三",
     		age: 20,
     		hobby: []string{"足球", "篮球"},
     		map1: map[string]string{
     			"打招呼": "你好",
     		},
     	}
     	fmt.Println(p)
     	for i := 0; i < len(p.hobby); i++ {
     		fmt.Println(p.hobby[i])
     	}
     	for _, v := range p.map1 {
     		fmt.Println(v)
     	}
     }
     /*
     {张三 20 [足球 篮球] map[打招呼:你好]}
     足球
     篮球
     你好
     1*/
     ```

  2. Make 初始化存储空间后复制

     ```go
     package main
     
import (
     	"fmt"
   	"strconv"
     )
     
     type Person struct {
     	name string
     	age int
     	hobby []string
     	map1 map[string]string
     }
     
     /*
     Make 分配内存空间后赋值
      */
     
     func main() {
     	var p  Person
     	p.name = "李四"
     	p.age = 52
     	p.hobby = make([]string, 6, 6)
     	hob := "篮球"
     	for i := 0; i < 6; i ++ {
     		p.hobby[i] = hob + strconv.FormatInt(int64(i), 10)
     	}
     	p.map1 = make(map[string]string)
     	p.map1["address"] = "北京"
     	p.map1["tel"] = "1212124541"
     	fmt.Println(p)
     }
     
     /*
     {李四 52 [篮球0 篮球1 篮球2 篮球3 篮球4 篮球5] map[address:北京 tel:1212124541]}
      */
     ```
     
  
+ 嵌套结构体

  1. 命名嵌套

     ```go
     package main
     
     import "fmt"
     
     type User struct {
     	Username string
     	Password string
     	Gender string
     	Age int
     	Address Address  // 表示 User 结构体嵌套 Address 结构体
     }
     
     type Address struct {
     	Name string
     	Phone string
     	City string
     }
     
     func main() {
     	var u User
     	u.Username = "榴榴"
     	u.Password = "124578369"
     	u.Gender = "男"
     	u.Age = 22
     	u.Address.Name = "牧羊人"
     	u.Address.Phone = "142536456"
     	u.Address.City = "北京"
     	fmt.Printf("%#v", u)
     }
     //  main.User{Username:"榴榴", Password:"124578369", Gender:"男", Age:22, Address:main.Address{Name:"牧羊人", Phone:"142536456", City:"北京"}}
     ```

     

  2. 匿名嵌套

     ```go
     package main
     
     import "fmt"
     
     type User struct {
     	Username string
     	Password string
     	Gender string
     	Age int
     	Address // 表示 User 结构体匿名嵌套 Address 结构体
     }
     
     type Address struct {
     	Name string
     	Phone string
     	City string
     }
     
     func main() {
     	var u User
     	u.Username = "榴榴"
     	u.Password = "124578369"
     	u.Gender = "男"
     	u.Age = 22
     	u.Address.Name = "牧羊人"
     	u.Address.Phone = "142536456"
     	u.Address.City = "北京"
     	fmt.Printf("%#v", u)
     }
     // main.User{Username:"榴榴", Password:"124578369", Gender:"男", Age:22, Address:main.Address{Name:"牧羊人", Phone:"142536456", City:"北京"}}
     
     ```

  3. 前套内可以直接调用嵌套结构体的字段赋值、查找

     ```go
     package main
     
     import "fmt"
     
     type User struct {
     	Username string
     	Password string
     	Gender string
     	Age int
     	Address // 表示 User 结构体匿名嵌套 Address 结构体
     }
     
     type Address struct {
     	Name string
     	Phone string
     	City string
     }
     
     func main() {
     	var u User
     	u.City = "上海"
     }
     ```

     

  

#### 8. 关于嵌套结构体的字段名冲突

+ 嵌套体内部可能存在相同的字段名,为了避免歧义需要指定具体的内嵌结构体字段

+ 实例 : 更改 Address 前套内与 User 存在相同名称 Username 

  ```go
  package main
  
  import "fmt"
  
  type User struct {
  	Username string
  	Password string
  	Gender string
  	Age int
  	Address // 表示 User 结构体匿名嵌套 Address 结构体
  }
  
  type Address struct {
  	Username string
  	Phone string
  	City string
  }
  
  func main() {
  	var u User
  	u.Username = "榴榴"
  	u.Password = "124578369"
  	u.Gender = "男"
  	u.Age = 22
  	u.Username = "牧羊人"  // Address:main.Address{Username:"", Phone:"142536456", City:"上海"}
  	u.Address.Username = "牧羊人"  // Username:"牧羊人", Phone:"142536456", City:"上海"}
  	u.Address.Phone = "142536456"
  	u.Address.City = "北京"
  	u.City = "上海"
  	fmt.Printf("%#v", u)
  }
  ```

+ 如果一个结构体内部两个嵌套结构体有**相同命名字段**,直接定位不指定子结构体会出现报错

#### 9. 结构体的继承

+ Go 语言中结构体的继承是通过结构体的嵌套实现的

+ 实例

  ```go
  package main
  
  import "fmt"
  
  /*
  结构体的嵌套
   */
  
  // 父结构体
  type Animal struct {
  	Name string
  }
  
  func (a Animal) run()  {
  	fmt.Printf("%v 正在跑", a.Name)
  }
  
  // 子结构体
  type Dog struct {
  	Age string
  	Animal  // 结构体嵌套实现继承
  }
  
  func (d Dog) wang()  {
  	fmt.Printf("%v 正在汪汪叫\n", d.Name)
  }
  
  func main() {
  	var d Dog
  	d.Name = "柯基"
  	d.Age = "10"
  	fmt.Printf("%#v\n", d)
  	d.run()
  	d.wang()
  }
  /*
  main.Dog{Age:"10", Animal:main.Animal{Name:"柯基"}}
  柯基 正在跑柯基 正在汪汪叫
  */
  ```

+ 一个结构体内部可以包含另一个结构体的指针

  ```go
  package main
  
  import "fmt"
  
  // 父结构体
  type Animal struct {
  	Name string
  }
  
  func (a Animal) run()  {
  	fmt.Printf("%v 正在跑\n", a.Name)
  }
  
  // 子结构体
  type Dog struct {
  	Age string
  	*Animal  // 结构体嵌套实现继承
  }
  
  func (d Dog) wang()  {
  	fmt.Printf("%v 正在汪汪叫\n", d.Name)
  }
  
  func main() {
  	var d  = Dog{
  		Age: "10",
  		Animal: &Animal{
  			Name: "柯基",
  		},
  	}
  	fmt.Printf("%#v\n", d)
  	d.run()
  	d.wang()
  }
  /*
  main.Dog{Age:"10", Animal:(*main.Animal)(0xc0000481f0)}
  柯基 正在跑
  柯基 正在汪汪叫
  */
  ```

  