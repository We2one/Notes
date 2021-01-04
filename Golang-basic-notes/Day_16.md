### Golang 反射

#### 1. 反射的引子

+ 空接口可以存储任意类型的变量,判断空接口处理变量的两种方法

  1. 使用**类型断言**
  2. 使用**反射实现** (在程序运行时动态的获取一个变量的类型信息和值信息)

+ 把结构体序列化成 json 字符串,自定义结构体 Tab 标签的时候就用到了反射

  ```go
  package main
  
  import (
  	"encoding/json"
  	"fmt"
  )
  
  type Student struct {
  	ID int `json:"id"`
  	Gender string `json:"gender"`
  	Name string `json:"name"`
  	Sno string `json:"sno"`
  }
  
  func main() {
  	var s1 = Student{
  		ID: 1,
  		Gender: "男",
  		Name: "小王",
  		Sno: "z001",
  	}
  
  	fmt.Println(s1)
  	/*
  	{1 男 小王 z001}
  	 */
  
  	var s, _ = json.Marshal(s1)
  	jsonStr := string(s)
  	fmt.Println(jsonStr)
  	/*
  	{"id":1,"gender":"男","name":"小王","sno":"z001"}
  	 */
  }
  ```

+ ORM 框架用到了反射技术

  + **ORM**: 对象关系映射(Object Relational Mapping) 通过使用描述对象和数据库之间映射的元数据,将面向对象语言程序中的对象自动持久化到关系数据库中

#### 2. 反射的基本介绍

+ 反射 : 在程序运行期间对程序本身进行访问和修改的**能力**
+ **不支持反射的语言** : 程序在编译时,变量被转化为内存地址,变量名不会被编译器写入到可执行部分,在程序运行时,无法获取到自身的信息
+ **支持反射的语言** : 可以在程序编译期间将变量的反射信息,如字段名称,类型信息、结构体信息等整合到可执行文件中,并给程序提供接口访问反射信息，这样就可以在程序运行期间执行获取类型的反射信息,并且有能力修改.

#### 3. Go语言中的反射

+ Go可以实现的功能
  1. 反射可以在程序运行期间动态的获取变量的各种信息,比如变量的类型、类别
  2. 如果是结构体,通过反射还可以获取结构体本身的信息,比如结构体的字段、结构体的方法
  3. 通过反射可以修改变量的值,可以调用关联方法
+ Go 语言中的变量分为两部分
  + **类型信息** : 预先定义好的元信息
  + **值信息** : 程序运行过程中可动态变化的
+ 在 Go 语言的反射机制中, 任何接口都是由一个 **具体类型** 和 **具体类型的值** 两部分组成
+ 在 Go 语言中的反射的相关功能由内置的 reflect 包提供,任意接口值在反射中都可以理解为由 **reflect.Type** 和 **reflect.Value** 两部分组成,并且 reflect 包提供了 **reflect.TypeOf** 和 **reflect.ValueOf** 两个重要的函数来获取任意对象的 Value 和 Type

#### 4. reflect.TypeOf() 获取任意值的类型对象

+ **reflect.TypeOf()** 可以接收任意 interface{} 参数,可以获得任意值的类型对象,程序通过类型对象可以访问任意值的类型信息

+ **type Name** 与 **type Kind**

  + 反射中的两种类型
    1. **类型 Type** : 打印出结构体的类型名称
    2. **种类 Kind** : 底层的类型 (结构体)，在反射中区分指针、结构体时需要使用
  + Go 语言反射中像数组、切片、Map、指针等类型的变量,**.Name()** 都为空

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"reflect"
  )
  
  //反射获取变量类型
  
  type myInt int
  type Person struct {
  	Name string
  	Age myInt
  }
  
  func reflectFn(x interface{}){
  	v := reflect.TypeOf(x)
  	fmt.Printf("%v 的类型为 %v 类型名称为%v 类型种类为%v\n", x, v, v.Name(), v.Kind())
  }
  
  func main() {
  	a := 11
  	b := 23.44
  	c := true
  	d := "hello word"
  	var e myInt = 34
  	f := Person{
  		Name: "李",
  		Age: 12,
  	}
  	g := 12
  	h := [3]int{1, 2, 3}
  	i := []int{11, 23, 45}
  	reflectFn(a) // 11 的类型为 int 类型名称为int 类型种类为int
  	reflectFn(b) // 23.44 的类型为 float64 类型名称为float64 类型种类为float64
  	reflectFn(c) // true 的类型为 bool 类型名称为bool 类型种类为bool
  	reflectFn(d) // hello word 的类型为 string 类型名称为string 类型种类为string
  	reflectFn(e) // 34 的类型为 main.myInt 类型名称为myInt 类型种类为int
  	reflectFn(f) // {李 12} 的类型为 main.Person 类型名称为Person 类型种类为struct
  	reflectFn(&g) // 0xc0000a2058 的类型为 *int 类型名称为 类型种类为ptr
  	reflectFn(h) // [1 2 3] 的类型为 [3]int 类型名称为 类型种类为array
  	reflectFn(i) // [11 23 45] 的类型为 []int 类型名称为 类型种类为slice
  }
  ```

#### 5. reflect.ValueOf() 返回 reflect.Value 类型

+ reflect.Value 类型提供的获取原始值的方法如下

  | 方法                                | 描述                                                         |
  | ----------------------------------- | ------------------------------------------------------------ |
  | **interface()**<br>**interface {}** | 将值以 **interface {} **类型返回,可以通过类型断言转化为指定类型 |
  | **int() int64**                     | 将值以 **int** 类型返回,所有有符号整数均可以以此方式返回     |
  | **Uint() uint64**                   | 将值以 **unit**类型返回,所有的无符号整数均可以此方式返回     |
  | **Float() float64**                 | 将值以 **双精度(float64)** 类型返回,所有的浮点数 (float32、float64) 均以此方式返回 |
  | **Bool() bool**                     | 以 bool 类型返回值                                           |
  | **Bytes() []bytes**                 | 将值以字节数组 []bytes 类型返回                              |
  | **String() string**                 | 将值以字符串类型返回                                         |

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"reflect"
  )
  
  func reflectFn(x interface{}){
  	//var num = 10 + x  // (mismatched types int and interface {}) 类型不同
  	// 类型断言转换空接口类型为 int 类型
  	//b, _ := x.(int)
  	//var num = 10 + b
  	//fmt.Println(num)
  	// 反射实现
  	//var v = reflect.ValueOf(x)
  	//fmt.Printf("%v 的类型为 %T", x, v)  // 13 的类型为 reflect.Value
  	//var num = v + 12 // (mismatched types reflect.Value and int) 类型不同
  
  	// 反射获取变量的原始值
  	v := reflect.ValueOf(x)
  	var m = v.Int() + 12
  	fmt.Println(m) // 25
  }
  
  func main() {
  	var a = 13
  	reflectFn(a)
  }
  ```

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"reflect"
  )
  
  /*
  获取不同类型的原始值
   */
  
  func reflectValue(x interface{})  {
  	v := reflect.ValueOf(x) // 返回了kind 种类信息
  
  	kind := v.Kind()
  
  	switch kind {
  	case reflect.Int64:
  		fmt.Printf("int 类型的原始值计算后为 %v\n", v.Int() + 10)
  	case reflect.Float32:
  		fmt.Printf("Float32 类型的原始值计算后为 %v\n", v.Float() + 12.12)
  	case reflect.Float64:
  		fmt.Printf("Float64 类型的原始值计算后为 %v\n", v.Float() + 131.2)
  	case reflect.String:
  		fmt.Printf("String 类型的原始值计算后为 %v\n", v.String() + "!")
  	default:
  		fmt.Println("未判断")
  	}
  
  }
  
  func main() {
  	var a float32 = 122.121
  	var b int64 = 100
  	var c string = "Hello word"
  	reflectValue(a) // Float32 类型的原始值计算后为 134.24100219726563
  	reflectValue(b) // int 类型的原始值计算后为 110
  	reflectValue(c) // String 类型的原始值计算后为 Hello word!
  }
  ```

#### 6. 通过反射设置变量的值

+ 通过 **reflect.Value** 获取值, **.Elem().Setint()** 修改副本值,reflect 包会引发 panic

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"reflect"
  )
  
  /*
  通过反射设置变量的值
   */
  
  //func reflectSetValue1(x interface{}) {
  //	var v = reflect.ValueOf(x)
  //	if v.Kind() == reflect.Int64 {
  //		v.SetInt(200) // 报错 使用的是值类型，不是引用类型
  //	}
  //}
  
  func reflectSetValue2(x interface{})  {
  	var v = reflect.ValueOf(x)
  	fmt.Println(v.Kind()) // ptr ptr 指针类型
  	fmt.Println(v.Elem().Kind()) // int64 string 获取到具体类型
  	if v.Elem().Kind() == reflect.Int64 {
  		v.Elem().SetInt(200)
  	}else if v.Elem().Kind() == reflect.String {
  		v.Elem().SetString("已经修改")
  	}
  }
  
  func main() {
  	var a int64 = 100
  	var b string = "hello"
  	//reflectSetValue1(a)
  	reflectSetValue2(&a)
  	reflectSetValue2(&b)
  	fmt.Println(a) // 200
  	fmt.Println(b) // 已经修改
  }
  ```

#### 7. 结构体反射

##### 7.1 与结构体相关的方法

+ 任意值通过 reflect.TypeOf() **获得反射对象信息**后,如果它的类型是结**构体**,可以通过反射值对象 (reflect.Type) 的 **NumField()** 和 **Field()** 方法获得结构体成员的详细信息

+ reflect 中获取结构体成员相关的方法

  | 参数                                                         | 描述                                           |
  | ------------------------------------------------------------ | ---------------------------------------------- |
  | **Field(i int) StructField**                                 | 根据索引,返回索引对应的结构体字段的信息        |
  | **NumField() int**                                           | 返回结构体成员字段数量                         |
  | **FieldByName(name string) (StructField, bool)**             | 根据给定字符串返回字符串对应的结构体字段的信息 |
  | **FieldByIndex(index []int) StructField**                    | 多层成员访问时,根据 []int 提供的每个结构体     |
  | **FieldByNameFunc(match func(string) bool) (StructField, bool)** | 根据传入的匹配函数匹配需要的字段               |
  | **NumMethod() int**                                          | 返回该类型方法的数目                           |
  | **Method(int) Method**                                       | 返回该类型方法的第 i 种方法                    |
  | **MethodByName(string)(Method, bool)**                       | 根据方法名返回该类型方法集中的方法             |

##### 7.2 StructField 类型

+ StructField 类型 用来描述结构体中的一个字段的信息

  ```go
  type StructField struct {
      Name string // 字段名
      PkgPath string // 非导出字段的包路径,对导出字段该字段为""
      Type Type // 字段的类型
      Tag StructTag // 字段的标签
      Offset uintptr // 字段在结构体中的字节偏移量
      Index []int // 用于 Type.FieldByIndex 时的索引切片
      Anonymous bool // 是否匿名字段
  }
  ```

##### 7.3 通过类型字段与值字段获取结构体属性的类型

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"reflect"
  )
  
  type Student struct {
  	Name string `json:"name"`
  	Age int `json:"age"`
  	Score int `json:"score"`
  }
  
  func (s Student) GetInfo() string {
  	var str = fmt.Sprintf("姓名: %v, 年龄: %v, 成绩: %v", s.Name, s.Age, s.Score)
  	return str
  }
  
  func (s *Student) SetInfo(name string, age int, score int) {
  	s.Name = name
  	s.Age = age
  	s.Score  = score
  }
  
  func (s Student) Print() {
  	fmt.Println("打印输出")
  }
  
  // 打印字段，结构体内字段
  func PrintStructField(s interface{})  {
  
  	// 判断参数是否是结构体类型
  	t := reflect.TypeOf(s)
  	v := reflect.ValueOf(s)
  	if t.Kind() != reflect.Struct && t.Elem().Kind() != reflect.Struct {
  		fmt.Println("传入的参数不是结构体")
  		return
  	}else {
  
  		// 1. 通过类型变量里面的 Field(n) 可以获取结构体第n个字段,反回一个结构体
  		field0 := t.Field(0)
  		fmt.Println(field0)  // {Name  string json:"name" 0 [0] false}
  		fmt.Println("字段名称：", field0.Name)  // Name
  		fmt.Println("字段类型：", field0.Type) // 字段类型 string
  		fmt.Println("字段 Tag：", field0.Tag.Get("json"))  // 字段 Tag： name
  		fmt.Println("字段 Tag：", field0.Tag.Get("form"))
  		fmt.Println("--------------------------------")
  		// 2. 通过类型变量里面的 FieldByName 可以获取结构体的字段
  		field1,ok := t.FieldByName("Age")
  		if ok {
  			fmt.Println(field1) // {Age  int json:"age" 16 [1] false}
  			fmt.Println("字段名称：", field1.Name)  // 字段名称： Age
  			fmt.Println("字段类型：", field1.Type) // 字段类型： int
  			fmt.Println("字段 Tag：", field1.Tag.Get("json")) // 字段 Tag： age
  		}
  		fmt.Println("--------------------------------")
  		// 3. 通过类型变量里面的 NumField 获取到该结构体内的字段数量
  		t_count := t.NumField()
  		fmt.Println("字段数量: ", t_count) // 字段数量:  3
  		// 4. 获取结构体属性对应的值
  		// fmt.Println(v.FieldByName("Name")) // 王二
  
  		for i:=0; i < t_count; i ++ {
  			fmt.Printf("属性名称: %v, 属性值: %v, 属性类型: %v, 属性 Tag: %v\n", t.Field(i), v.Field(i), t.Field(i).Type, t.Field(i).Tag.Get("json"))
  			// 属性名称: {Name  string json:"name" 0 [0] false}, 属性值: 王二, 属性类型: string, 属性 Tag: name
  			// 属性名称: {Age  int json:"age" 16 [1] false}, 属性值: 12, 属性类型: int, 属性 Tag: age
  			// 属性名称: {Score  int json:"score" 24 [2] false}, 属性值: 99, 属性类型: int, 属性 Tag: score
  		}
  
  	}
  }
  
  // 打印执行方法,结构体所关联的方法
  func PrintStructFn(s interface{})  {
  
  	// 判断参数是否是结构体类型
  	t := reflect.TypeOf(s)
  	v := reflect.ValueOf(s)
  	if t.Kind() != reflect.Struct && t.Elem().Kind() != reflect.Struct {
  		fmt.Println("传入的参数不是结构体")
  		return
  	}else {
  
  		// 1. 通过类型变量里面的 Method 可以获取结构体的方法
  		method0 := t.Method(0)  // 0 和结构体方法的顺与无关，与其的 Ascii 码有关
  		fmt.Println(method0) // {GetInfo  func(main.Student) string <func(main.Student) string Value> 0}
  		fmt.Println(method0.Name) // GetInfo
  		fmt.Println(method0.Type) // func(main.Student) string
  		method1, ok := t.MethodByName("Print")
  		if ok {
  			fmt.Println(method1) // {Print  func(main.Student) <func(main.Student) Value> 1}
  			fmt.Println(method1.Name) // Print
  			fmt.Println(method1.Type) // func(main.Student)
  		}
  		fmt.Println("--------------------------------")
  		// 2. 通过类型变量获取结构体内方法的数目,通过 valueOf 获取
  		method2 := v.NumMethod()
  		fmt.Println(method2) // 3
  		// 3. 通过 (值变量) 执行方法 v.Method(0).Call(nil) 或者 v.MethodByName().Call(nil)
  		// Call() 传参，不需要传参的传入 niu
  		// 调用 print 方法
  		//v.Method(1).Call(nil) // 打印输出
  		v.MethodByName("Print").Call(nil) // 打印输出
  		info := v.MethodByName("GetInfo").Call(nil)
  		fmt.Println(info)  // [姓名: 王二, 年龄: 12, 成绩: 99]
  		// 4. 执行方法传入参数 (使用值变量，注意使用参数，接受的参数是 []reflect.Value 的切片)
  		var params []reflect.Value
  		params = append(params, reflect.ValueOf("李四"))
  		params = append(params, reflect.ValueOf(12))
  		params = append(params, reflect.ValueOf(65))
  		// 执行方法传入参数
  		v.MethodByName("SetInfo").Call(params)
  		fmt.Println(v.MethodByName("GetInfo").Call(nil)) // [姓名: 李四, 年龄: 12, 成绩: 65]
  
  	}
  }
  
  // 反射修改结构体属性
  func reflectChangeStruct(s interface{}) {
  	// 判断参数是否是结构体类型
  	t := reflect.TypeOf(s)
  	v := reflect.ValueOf(s)
  	if t.Kind() != reflect.Ptr && t.Elem().Kind() != reflect.Struct {
  		fmt.Println("传入的参数不是结构体地址")
  		return
  	}else {
  		// 修改值
  		name := v.Elem().FieldByName("Name")
  		name.SetString("小李")
  		age := v.Elem().FieldByName("Age")
  		age.SetInt(34)
  		fmt.Printf("%#v", v)  // &main.Student{Name:"小李", Age:34, Score:99}
  	}
  }
  
  func main() {
  	stu1 := Student{
  		Name: "王二",
  		Age: 12,
  		Score: 99,
  	}
  	//PrintStructField(stu1)
  	//PrintStructFn(&stu1)
  	reflectChangeStruct(&stu1)
  }
  
  ```

  

#### 8. 反射的使用

