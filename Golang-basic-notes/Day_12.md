### Golang 结构体和 Json 相互转化、序列化、反序列化

#### 1. 关于JSON 数据

+ JSON (JavaScript Object Notation) ; 轻量级数据交换格式,易于人阅读和编写,也易于机器解析和生成

+ RESTfull Api 接口中返回的都是 Json 数据

+ JSON 的基本格式

  ```json
  {
      "a": "Hello",
      "b": "World"
  }
  ```

  

#### 2. 结构体 与 JSON 序列化

+ **Golang JSON 序列化** : 把结构体数据转化为 JSON 格式的字符串

+ **Golang JSON 的反序列化** : 把 JSON 数据转化成 Golang 中的结构体对象

+ Golang 中序列化与反序列化主要通过 **"encoding/json"** 包中的 **json.Marshal()** 和 `json.Unmarshal()` 方法

  + `json.Marshal(结构体)` : 返回两个值
    + 第一个值为 切片比特类型的 json 数据
    + 第二个值为 error 报告
  + `json.Unmarshal(比特类型切片数据, 转换为结构体定义地址)` : 将 JSON 字符串 强制转换为 结构体对象, 返回 **error** 信息
    + 如果 error 信息 为空则转换成功
    + 如果 error 信息 不为空 则转换失败

+ 结构体转换为 JSON 字符串

  + `string(JSON 切片)` : 将 比特类型的 JSON 切片强制转换成 JSON 格式数据

  ```go
  package main
  
  import (
  	"encoding/json"
  	"fmt"
  )
  
  type Student struct {
  	ID int
  	Gender string
  	name string  // 私有属性不能被 json 包访问
  	Sno string
  }
  
  func main() {
  	var s = Student{
  		ID: 111,
  		Gender: "男",
  		name: "张三",
  		Sno: "G1212",
  	}
  
  	fmt.Println(s)
  	jsonByte,_ := json.Marshal(s)
      fmt.Println(jsonByte)
  
  	jsonStr := string(jsonByte)
  	fmt.Println(jsonStr)
  
  }
  /*
  {111 男 张三 G1212}
  [123 34 73 68 34 58 49 49 49 44 34 71 101 110 100 101 114 34 58 34 231 148 183 34 44 34 83 110 111 34 58 34 71 49 50 49 50 34 125]
  {"ID":111,"Gender":"男","Sno":"G1212"}
  */
  ```

+ JSON 字符串转换为 结构体

  + 初始化结构体字符串由于双引号冲突,用反引号将字符串包裹,或 由反斜杠对双引号进行转义

  ```go
  package main
  
  import (
  	"encoding/json"
  	"fmt"
  )
  
  type Student struct {
  	ID int
  	Gender string
  	name string  // 私有属性不能被 json 包访问
  	Sno string
  }
  
  func main() {
  	var str = `{"ID":111,"Gender":"男","Sno":"G1212"}`
  	var s Student
  	var err = json.Unmarshal([]byte(str), &s)
  	if err != nil{
  		fmt.Println(err)
  	}else {
  		fmt.Printf("%#v", s)
  	}
  }
  ```

  

#### 3. 结构体标签 Tag

+ Tag 是结构体的 **元信息**, 可以在运行时通过反射的机制读取出来.Tag 在结构体字段的后方定义,由一对**反引号**包裹起来

+ Tag 的作用 : 使 结构体转换成的 JSON 字符串 更加符合标准 (公有化首字母大写,然而json可以小写)

+ 具体格式 : **`key1:"value1" key2:"value2"`**

+ 结构体 Tag 由一个或多个键值对组成.键值对使用 冒号分隔,值使用双引号括起来.同一个结构体字段可以设置多个键值对 tag,不同的键值对之间使用 空格分隔

+ **注意** : 结构体标签的解析代码容错率很差,所以编写结构体 tag 时必须严格遵守键值对的规则(key 与 value 之间不要添加空格)

+ 转换实例

  ```go
  package main
  
  import (
  	"encoding/json"
  	"fmt"
  )
  
  type Student struct {
  	ID int `json:"id"`
  	Gender string `json:"gender"`
  	name string  // 私有属性不能被 json 包访问
  	Sno string `json:"sno"`
  }
  func main() {
  	var s = Student{
  		ID: 111,
  		Gender: "男",
  		name: "张三",
  		Sno: "G1212",
  	}
  
  	fmt.Println(s)
  	jsonByte,_ := json.Marshal(s)
  
  	jsonStr := string(jsonByte)
  	fmt.Println(jsonStr)
  }
  /*
  {111 男 张三 G1212}
  {"id":111,"gender":"男","sno":"G1212
  */
  ```

  

#### 4. 嵌套结构体 和 JSON 序列化反序列化

1. 嵌套结构体转换为 JSON 字符串

   ```go
   package main
   
   import (
   	"encoding/json"
   	"fmt"
   	"strconv"
   )
   
   type Student struct {
   	Id int `json:"id"`
   	Name string `json:"姓名"`
   	Gender string `json:"性别"`
   }
   
   type Class struct {
   	Title string `json:"班级"`
   	Student []Student `json:"学生"`
   }
   
   func main() {
   	var c = Class{
   		Title: "001",
   		Student: make([]Student, 0),
   	}
   	for i := 1; i <= 10; i++ {
   		s := Student{
   			Id: i,
   			Gender: "男",
   			//Name: fmt.Sprintf("stu_%v", i),
   			Name: "stu_" + strconv.FormatInt(int64(i), 10),
   		}
   		c.Student = append(c.Student, s)
   	}
   	fmt.Println(c)
   
   	jsonByte,_ := json.Marshal(c)
   
   	jsonStr := string(jsonByte)
   	fmt.Println(jsonStr)
   
   }
   /*
   {001 [{1 stu_1 男} {2 stu_2 男} {3 stu_3 男} {4 stu_4 男} {5 stu_5 男} {6 stu_6 男} {7 stu_7 男} {8 stu_8 男} {9 stu_9 男} {10 stu_10 男}]}
   {"班级":"001","学生":[{"id":1,"姓名":"stu_1","性别":"男"},{"id":2,"姓名":"stu_2","性别":"男"},{"id":3,"姓名":"stu_3","性别":"男"},{"id":4,"姓名":"stu_4","性别":"男"},{"id":5,"姓名":"stu_5","性别":"男"},{"id":6,"姓名":"stu_6","性别":"男"},{"id":7,"姓名":"stu_7","性别":"男"},{"id":8,"姓名":"stu_8","性别":"男"},{"id":9,"姓名":"stu_9","性别":"男"},{"id":10,"姓名":"stu_10","性别":"男"}]}
   */
   ```

   

2. JSON 字符串转换为 嵌套结构体

   ```go
   package main
   
   import (
   	"encoding/json"
   	"fmt"
   )
   
   type Student struct {
   	Id int `json:"id"`
   	Name string `json:"姓名"`
   	Gender string `json:"性别"`
   }
   
   type Class struct {
   	Title string `json:"班级"`
   	Student []Student `json:"学生"`
   }
   
   func main() {
   	var str = `{"班级":"001","学生":[{"id":1,"姓名":"stu_1","性别":"男"},{"id":2,"姓名":"stu_2","性别":"男"},{"id":3,"姓名":"stu_3","性别":"男"},{"id":4,"姓名":"stu_4","性别":"男"},{"id":5,"姓名":"stu_5","性别":"男"},{"id":6,"姓名":"stu_6","性别":"男"},{"id":7,"姓名":"stu_7","性别":"男"},{"id":8,"姓名":"stu_8","性别":"男"},{"id":9,"姓名":"stu_9","性别":"男"},{"id":10,"姓名":"stu_10","性别":"男"}]}`
   	var c Class
   
   	var err = json.Unmarshal([]byte(str), &c)
   	if err != nil {
   		fmt.Println(err)
   	}else {
   		fmt.Println(c)
   		fmt.Printf("%#v", c)
   	}
   }
   /*
   {001 [{1 stu_1 男} {2 stu_2 男} {3 stu_3 男} {4 stu_4 男} {5 stu_5 男} {6 stu_6 男} {7 stu_7 男} {8 stu_8 男} {9 stu_9 男} {10 stu_10 男}]}
   main.Class{Title:"001", Student:[]main.Student{main.Student{Id:1, Name:"stu_1", Gender:"男"}, main.Student{Id:2, Name:"stu_2", Gender:"男"}, main.Student{Id:3, Name:"stu_3", Gender:"男"}, main.Student{Id:4, Name:"stu_4", Gender:"男"}, main.Student{Id:5, Name:"stu_5", Gender:"男"}, main.Student{Id:6, Name:"stu_6", Gender:"男"}, main.Student{Id:7, Name:"stu_7", Gender:"男"}, main.Student{Id:8, Name:"stu_8", Gender:"男"}, main.Student{Id:9, Name:"stu_9", Gender:"男"}, main.Student{Id:10, Name:"stu_10", Gender:"男"}}}
   */
   ```

   

#### 5. 关于 Map、切片的序列化反序列化

