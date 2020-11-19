### Golang 中的接口

#### 1. 接口的介绍

+ Golang 中的接口 (interface) 是一种抽象数据类型,Golang中接口定义了对象的行为规范,接口中定义的规范由具体对象实现
+ 接口就是一个标准,是对一个对象的行为和规范进行约定,约定实现接口的对象必须按照接口的规范

#### 2. Golang 接口的定义

+ Golang 中 接口是一种抽象类型，是一组函数 method 的集合,不能包含任何变量

+ Golang 中接口中所有方法都**没有方法体**,借口体现了程序设计的高内聚低耦合的思想

+ Golang中接口也是一种数据类型,不需要显示实现.只需要一个变量含有接口类型中的所有方法,那么这个变量就实现了接口

+ Golang 中每个接口由数个方法组成,接口定义格式为:

  ```go
  type 接口名 interface{
      方法名1(参数列表1) 返回值列表1
      方法名2(参数列表2) 返回值列表2
      ...
  }
  ```

  + 参数
    1. **接口名**: 使用 type 将接口定义为自定义的类型名.Go 语言在接口命名时,一般会在单词后加 **er** (写操作的借口叫 Writer等)
    2. **方法名**: 当方法名首字母大写且这个接口名首字母大写时,这个方法可以被接口所在的包 (package) 之外的代码访问
    3. **参数列表、返回值列表**: 参数列表和返回值列表中的参数变量名可以省略

+ 实例 : 如果接口里面有方法,必须通过**结构体**或者**自定义类型**实现接口

  ```go
  package main
  
  import "fmt"
  
  type Usber interface{
  	// 指定方法类型
  	start(string, string) string
  	// 不指定方法类型
  	stop()
  }
  
  // 如果接口里面有方法,必须通过**结构体**或者自定义类型实现接口
  
  type Phone struct {
  	Name string
  }
  
  // 结构体实现接口的话必须实现接口的所有方法
  func (p Phone) start(string, string) string {
  	fmt.Println(p.Name, "启动")
  	return "测试成功"
  }
  
  func (p Phone) stop() {
  	fmt.Println(p.Name, "关机")
  }
  
  func main() {
  	var p = Phone{
  		Name: "华为",
  	}
  	p.start("1", "2")
  	p.stop()
  
  	// Golang 中接口就是数据类型
  	var p1 Usber
  	p1 = p
  	p1.start("2", "2")
  	p1.stop()
  
  }
  /*
  华为 启动
  华为 关机
  华为 启动
  华为 关机
  */
  ```

+ 接口调用

  ```go
  package main
  
  import "fmt"
  
  type Usber interface {
  	start()
  	stop()
  }
  
  type Computer struct {
  }
  
  func (c Computer) work(usb Usber) {
  	usb.start()
  	usb.stop()
  }
  
  type Phone struct {
  	Name string
  }
  
  func (p Phone) start() {
  	fmt.Println(p.Name, "启动")
  }
  
  func (p Phone) stop() {
  	fmt.Println(p.Name, "停止")
  }
  
  type Camera struct {
  
  }
  
  func (c Camera) start() {
  	fmt.Println("相机开机")
  }
  
  func (c Camera) stop() {
  	fmt.Println("相机关机")
  }
  
  func main() {
  	
  	// 初始化结构体
  	computer:= Computer{}
  	phone := Phone{
  		Name: "小米",
  	}
  	camera := Camera{}
  
  	computer.work(camera)
  	computer.work(phone)
  
  }
  /*
  相机开机
  相机关机
  小米 启动
  小米 停止
  */
  ```

  

#### 3. 空接口

+ Golang 中的接口可以不定义任何方法,没有定义方法的接口就是空接口

+ **空接口** 表示没有任何约束,因此**任何类型变量**都可以实现空接口

  ```go
  package main
  
  import "fmt"
  
  // 空接口 和 类型断言
  type A interface {
  	// 空接口，没有任何约束,任意类型都可以实现空接口
  }
  
  func main() {
  	var a A
  	var str = "你好空接口"
  	a = str // 字符串实现 空接口
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  
  	// int 类型实现 a 接口
  	var num = 100
  	a = num
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  
  	// bool 类型实现 a 接口
  	var bb = false
  	a = bb
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  
  }
  /*
  值: 你好空接口, 类型: string
  值: 100, 类型: int
  值: false, 类型: bool
  */
  ```

  

+ 空接口在实际项目中可以表示任意数据类型

  ```go
  package main
  
  import "fmt"
  
  // 空接口 和 类型断言
  
  
  /*
  Golang 中空接口也可以当做类型来使用, 可以表示任意类型
   */
  
  func main() {
  	var a interface{}
  
  	a = 20
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  	
  	a = "空接口代表任意类型"
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  
  	a = true
  	fmt.Printf("值: %v, 类型: %T\n", a, a)
  
  }
  /*
  值: 20, 类型: int
  值: 空接口代表任意类型, 类型: string
  值: true, 类型: bool
  */
  ```

+ 空接口作为 **函数参数** : 使用空接口可以接收任意类型的函数类型

  ```go
  package main
  
  import "fmt"
  
  // 空接口 和 类型断言
  
  /*
  空接口作为函数的参数
   */
  
  func show(a interface{})  {
  	fmt.Printf("类型: %T, 值: %v\n", a, a)
  }
  
  func main() {
  	show("你好")
  	show(200)
  	show([]int{1,2,3})
  }
  /*
  类型: string, 值: 你好
  类型: int, 值: 200
  类型: []int, 值: [1 2 3]
  */
  ```

  

+ **map的值**实现空接口 : 使用空接口可以保存任意值的字典

  ```go
  var studentinfo = make(map[string]interface{})
  studentinfo["age"] = 19
  studentinfo["name"] = "张三"
  fmt.Ptintln(studentinfo)
  ```

+ **切片**实现空接口

  ```go
  var slice = []interface{}{"张三", 20, true, 24.424}
  fmt.Println(slice)
  ```

  

#### 4. 类型断言

+ 一个接口的值是由一个具体类型和具体类型的值两部分组成,这两部分分别称为**接口的动态类型**和**动态值**

+ 如果想要得到一个空接口值的类型就需要用到类型断言

  + 格式

    ```go
    x.(T)
    ```

  + 参数

    + **X**: 表示类型为 interface{} 的变量
    + **T**: 断言x可能的类型

  + 返回值

    1. 第一个返回值: x 转化为 T 类型后的变量
    2. 第二个返回值: 布尔值,若为 true 则断言成功,false 则断言失败

+ 接口通过判断传入结构体类型决定使用方法

  ```go
  package main
  
  // 空接口 和 类型断言
  
  /*
  空接口判断传入结构体类型决定使用方法
   */
  
  import "fmt"
  
  type Usber interface {
  	start()
  	stop()
  }
  
  type Computer struct {
  }
  
  func (c Computer) work(usb Usber) {
  	switch usb.(type) {
  	case Camera:
  		usb.stop()
  	case Phone:
  		usb.start()
  	default:
  		usb.start()
  		usb.stop()
  	}
  	//usb.start()
  	//usb.stop()
  }
  
  type Phone struct {
  	Name string
  }
  
  func (p Phone) start() {
  	fmt.Println(p.Name, "启动")
  }
  
  func (p Phone) stop() {
  	fmt.Println(p.Name, "停止")
  }
  
  type Camera struct {
  
  }
  
  func (c Camera) start() {
  	fmt.Println("相机开机")
  }
  
  func (c Camera) stop() {
  	fmt.Println("相机关机")
  }
  
  func main() {
  
  	// 初始化结构体
  	computer:= Computer{}
  	phone := Phone{
  		Name: "小米",
  	}
  	camera := Camera{}
  
  	computer.work(camera)
  	computer.work(phone)
  
  }
  /*
  相机关机
  小米 启动
  */
  ```

  

+ 使用 switch ... case 对 不同接口类型进行不同操作

  ```go
  package main
  
  import "fmt"
  
  // 空接口 和 类型断言
  
  // 定义一个方法可以传入任意数据类型,然后根据不同类型执行不同方法
  
  func MyPrint(x interface{}) {
  	// x.(type) 只可以使用 switch case
  	switch x.(type) {
  	case int:
  		fmt.Println("int 类型")
  	case string:
  		fmt.Println("字符串 类型")
  	case bool:
  		fmt.Println("bool 类型")
  	case float64:
  		fmt.Println("浮点数类型")
  	default:
  		fmt.Println("未判断出类型")
  	}
  
  	//if _, ok := x.(string); ok {
  	//	fmt.Println("string 类型")
  	//}else if _, ok := x.(int); ok {
  	//	fmt.Println("int 类型")
  	//}else if _, ok := x.(float64); ok {
  	//	fmt.Println("float64 类型")
  	//}else if _, ok := x.(bool); ok {
  	//		fmt.Println("bool 类型")
  	//	}elif {
  	//		fmt.Println("传入错误")
  	//}
  }
  
  func main() {
  	MyPrint("你好")
  }
  /*
  字符串 类型
  */
  ```

  

+ 实例

  ```go
  package main
  
  import "fmt"
  
  // 空接口 和 类型断言
  
  /*
  类型断言
   */
  
  func main() {
  	var a interface{}
  
  	a = "空接口"
  	_, ok := a.(string)
  	if ok {
  		fmt.Printf("判断成功 a 的类型为 string, a 的值是 %v", a)
  	}else {
  		fmt.Println("断言失败")
  	}
  }
  ```

  

#### 5. 结构体值接收者和指针接收者实现接口区别

+ **结构体值接收者**

  + 如果结构体中的**方法**是**值接收者**,那么实例化后的结构体**值类型**和结构体**指针类型**都可以赋值给**接口变量**

  + 实例

    ```go
    package main
    
    // 空接口 和 类型断言
    
    /*
    空接口判断传入结构体类型决定使用方法
    */
    
    import "fmt"
    
    type Usber interface {
    	start()
    	stop()
    }
    
    type Computer struct {
    }
    
    func (c Computer) work(usb Usber) {
    	switch usb.(type) {
    	case Camera:
    		usb.stop()
    	case Phone:
    		usb.start()
    	default:
    		usb.start()
    		usb.stop()
    	}
    	//usb.start()
    	//usb.stop()
    }
    
    type Phone struct {
    	Name string
    }
    
    func (p Phone) start() {  // 值接收者
    	fmt.Println(p.Name, "启动")
    }
    
    func (p Phone) stop() {
    	fmt.Println(p.Name, "停止")
    }
    
    type Camera struct {
    
    }
    
    func (c Camera) start() {
    	fmt.Println("相机开机")
    }
    
    func (c Camera) stop() {
    	fmt.Println("相机关机")
    }
    
    func main() {
    
    	// 初始化结构体, 结构体值接收者实例化之后的结构体值类型和结构体指针类型都可以赋值给接口变量
    	var p1 = Phone{
    		Name: "小米手机",
    	}
    	var p2 Usber = p1  // 表示让 Phone 实现 Usb 接口
    	p2.start()
    
    	var p3 = &Phone{  // 指针类型
    		Name: "1+手机",
    	}
    	var p4 Usber = p3  // 表示让 Phone 实现 Usb 接口
    	p4.start()
    
    }
    /*
    小米手机 启动
    1+手机 启动
    */
    ```

    

+ **指针接收者**

  + 如果结构体中的方法是**指针接收者**,那么实例化后结构体**指针类型**可以赋值给**接口变量**,结构体值类型无法赋值给接口变量

  + 实例

    ```go
    package main
    
    
    /*
    指针接收者
    */
    
    import "fmt"
    
    type Usber interface {
    	start()
    	stop()
    }
    
    type Computer struct {
    }
    
    func (c Computer) work(usb Usber) {
    	switch usb.(type) {
    	case Camera:
    		usb.stop()
    	case *Phone:
    		usb.start()
    	default:
    		usb.start()
    		usb.stop()
    	}
    	//usb.start()
    	//usb.stop()
    }
    
    type Phone struct {
    	Name string
    }
    
    func (p *Phone) start() {  // 指针接收者
    	fmt.Println(p.Name, "启动")
    }
    
    func (p *Phone) stop() {
    	fmt.Println(p.Name, "停止")
    }
    
    type Camera struct {
    
    }
    
    func (c Camera) start() {
    	fmt.Println("相机开机")
    }
    
    func (c Camera) stop() {
    	fmt.Println("相机关机")
    }
    
    func main() {
    
    	// 初始化结构体, 结构体值接收者实例化之后的结构体值类型和结构体指针类型都可以赋值给接口变量
    	//var p1 = Phone{
    	//	Name: "小米手机",
    	//}
    	//var p2 Usber = p1  // 表示让 Phone 实现 Usb 接口
    	//p2.start()
    	// 报错
    
    	var p3 = &Phone{  // 指针类型
    		Name: "1+手机",
    	}
    	var p4 Usber = p3  // 表示让 Phone 实现 Usb 接口
    	p4.start()
    
    }
    /*
    1+手机 启动
    */
    ```

#### 6. 一个结构体实现多个接口

+ 有 **返回值** 与 **接收值** 的 结构体方法
  + 实例

    ```go
    package main
    
    import "fmt"
    
    // 定义一个 Animal 的接口,Animal 中定义两个方法,分别是 SetName 和 GetName ,分别让 Dog 结构体和 Cat 结构体实现此方法
    
    type Animaler interface {
    	SetName(string)
    	GetName() string
    }
    
    type Dog struct {
    	Name string
    }
    
    // 想要改变 结构体属性, 必须是指针接收者
    func (d *Dog) SetName(name string) {
    	d.Name = name
    }
    func (d Dog) GetName() string {
    	return d.Name
    }
    
    type Cat struct {
    	Name string
    }
    
    func (c *Cat) SetName(name string) {
    	c.Name = name
    }
    func (c Cat) GetName() string {
    	return c.Name
    }
    
    func main() {
    	// Dog 结构体实现 Animaler 接口
    	d := &Dog{
    		Name: "哈士奇",
    	}
    	var d1 Animaler = d
    	fmt.Println(d1.GetName())
    	d1.SetName("二哈")
    	fmt.Println(d1.GetName())
    	// Cat 结构体实现 Animaler 接口
    	c := &Cat{
    		Name: "田园猫",
    	}
    	var c1 Animaler = c
    	fmt.Println(c1.GetName())
    	c1.SetName("小奶猫")
    	fmt.Println(c1.GetName())
    }
    /*
    哈士奇
    二哈
    田园猫
    小奶猫
    */
    ```

+ 多接口

  ```go
  package main
  
  import "fmt"
  
  /*
  一个结构体多个接口
   */
  type Animaler1 interface {
  	SetName(string)
  }
  
  type Animaler2 interface {
  	GetName() string
  }
  
  type Dog struct {
  	Name string
  }
  
  // 想要改变 结构体属性, 必须是指针接收者
  func (d *Dog) SetName(name string) {
  	d.Name = name
  }
  func (d Dog) GetName() string {
  	return d.Name
  }
  
  type Cat struct {
  	Name string
  }
  
  func (c *Cat) SetName(name string) {
  	c.Name = name
  }
  func (c Cat) GetName() string {
  	return c.Name
  }
  
  func main() {
  	// Dog 结构体实现 Animaler 接口
  	d := &Dog{
  		Name: "哈士奇",
  	}
  	var d1 Animaler1 = d
  	var d2 Animaler2 = d
  	fmt.Println(d2.GetName())
  	d1.SetName("二哈")
  	fmt.Println(d2.GetName())
  	// Cat 结构体实现 Animaler 接口
  	c := &Cat{
  		Name: "田园猫",
  	}
  	var c1 Animaler1 = c
  	var c2 Animaler2 = c
  	fmt.Println(c2.GetName())
  	c1.SetName("小奶猫")
  	fmt.Println(c2.GetName())
  }
  /*
  哈士奇
  二哈
  田园猫
  小奶猫
  */
  ```

  

#### 7. 接口嵌套

+ 接口与接口之间可以通过嵌套创建出新的接口 (接口嵌套后可以通过实例化顶层接口直接使用)

  ```go
  package main
  
  import "fmt"
  
  /*
  接口嵌套
   */
  type Ainterface interface {
  	SetName(string)
  }
  
  type Binterface interface {
  	GetName() string
  }
  
  type Animaler interface {
  	Ainterface
  	Binterface
  }
  
  type Dog struct {
  	Name string
  }
  
  // 想要改变 结构体属性, 必须是指针接收者
  func (d *Dog) SetName(name string) {
  	d.Name = name
  }
  func (d Dog) GetName() string {
  	return d.Name
  }
  
  func main() {
  	// Dog 结构体实现 Animaler 接口
  	d := &Dog{
  		Name: "哈士奇",
  	}
  	var d1 Animaler = d
  	fmt.Println(d1.GetName())
  	d1.SetName("二哈")
  	fmt.Println(d1.GetName())
  }
  /*
  哈士奇
  二哈
  */
  ```

#### 8. 空接口和类型断言使用

1. 空接口与切片类型断言使用

   ```go
   package main
   
   import "fmt"
   
   // Golang 中空接口和类型断言使用细节
   func main() {
   	var userinfo = make(map[string]interface{})
   	userinfo["username"] = "张三"
   	userinfo["age"] = 20
   	userinfo["hobby"] = []string{"打游戏", "打篮球"}
   
   	//fmt.Println(userinfo["hobby"][1]) // 空接口不可以直接获取切片类型的具体值
   
   	hobby2,_ := userinfo["hobby"].([]string)
   	fmt.Println(hobby2[1])
   
   }
   /*
   打篮球
   */
   ```

   

2. 空接口与结构体类型断言使用

   ```go
   package main
   
   import "fmt"
   
   type Address struct {
   	Name string
   	Phone int
   }
   
   // Golang 中空接口和类型断言使用细节
   func main() {
   	var userinfo = make(map[string]interface{})
   	userinfo["username"] = "张三"
   	userinfo["age"] = 20
   	userinfo["hobby"] = []string{"打游戏", "打篮球"}
   
   	//fmt.Println(userinfo["hobby"][1]) // 空接口不可以直接获取切片类型的具体值
   
   	var address = Address{
   		Name: "李四",
   		Phone: 12424282,
   	}
   
   	userinfo["address"] = address
   	fmt.Println(userinfo["address"])
   
   	hobby2,_ := userinfo["hobby"].([]string)
   	fmt.Println(hobby2[1])
   
   	address2,_ := userinfo["address"].(Address)
   	fmt.Println(address2.Phone)
   
   }
   /*
   {李四 12424282}
   打篮球
   12424282
   */
   ```

   