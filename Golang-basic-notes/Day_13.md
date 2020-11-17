### Golang 中的 go mad 以及 Golang 包详解

#### 1. Golang 中 包的介绍和定义

+ Golang 中 **包** (package) 是多个源码的集合,是一种高级的代码复用方案
+ Golang 中的包分为三类
  1. Golang 系统内置包 : `fmt`、`strconv` (类型转换)、`sort`、`errors`、`time`、`encoding/json`、`os`、`io`由系统提供,引入后可直接使用
  2. 自定义包 : 开发者自己写的包
  3. 第三方包 : 属于自定义包的一种,需要下载安装到本地后才可以使用

#### 2. Golang 包管理工具 go mod

+ Golang 包管理变化
  + Golang 1.11 版本之前 : 自定义包必须把项目放在 GOPATH 目录
  + Golang 1.11 版本之后 : 无需手动配置环境变量,使用 **go mod** 管理项目,也不必须将项目放在 GOPATH 指定目录下,可以放在任意位置
  + Golang 1.13 版本之后 : 彻底可以不需要 GOPATH

+ go mod 使用

  1. `go mod init 项目名` : 初始化项目

     + 实际项目开发时需要首先在项目目录使用 go mod 生成一个 go.mod 文件管理项目依赖

     + 如果项目在 test 的文件夹下,需要在文件夹内使用 `go mod init test` 生成一个 go.mod 文件

       ```go
       //go.mod 内
       module 01
       
       go 1.15
       
       ```

       

#### 3. Golang 中自定义包

+ 一个包可以简单理解为一个存放多个 .go 文件的文件夹,该文件夹下 所有 go 文件 都要在代码的第一行添加 `package 包名`, 声明该文件归属的包
+ 注意
  1. 一个文件夹下面直接包含的文件只能归属一个 package, 同样一个 package 的文件不能在多个文件夹下,同一个包下不同 .go 文件内方法不能重复
  2. 包名可以不和文件夹的名字一样,包名不能含 "-" 符号
  3. 包名为 main 的包为应用程序的入口包,这种包编译后会得到一个可执行文件,编译不含 main 包的源代码则不会得到可执行文件

##### 3.1 定义一个包

+ 在生成 go.mod 文件夹下新建文件夹 , 在新建文件夹下创建 go 文件, 引用 package 建议为 新建文件夹名

  ```go
  package calc
  
  func Add(x, y int) int { // 首字母大写,公有方法, 可以在其他包访问
  	return x + y
  }
  
  func Sub(x, y int) int {
  	return x - y
  }
  ```

  

##### 3.2 导入一个包

+ 在 main.go 内 使用 import 引用包内定义方法

  ```go
  package main
  
  import (
  	"01/calc"  // model/新建自定义包名
  	"fmt"
  )
  
  func main() {
  	sum := calc.Add(10, 2)
  	fmt.Println(sum)
  }
  // 12
  ```

+ 包的导入

  1. 单行导入

     ```go
     import "包1"
     import "包2"
     ```

  2. 多行导入

     ```go
     import (
         "包1"
     	"包2"
     )
     ```

  3. 匿名导入包 : 只希望导入包而不使用包内部数据,可以使用匿名导入 (匿名导入的包与其他方式导入的包一样会被编译到可执行文件)

     ```go
     import_"包路径(包1)"
     ```

  4. 导入时自定义包名 : 为导入的包设置包名,处理导入包名过长以及导入包名冲突问题

     ```go
     import 别名 "包1"
     ```

     

#### 4. Golang 中 init() 初始化函数

+ Init() 函数介绍

  + 在 Go 语言执行程序时导入包会自动触发包内部 init() 函数的调用,init() 函数没有参数也没有返回值

  + Init() 函数在程序执行时自动被调用执行,不可以在代码中主动调用

  + 包初始化执行流程 : `全局声明 --> init() --> main()`

    ```go
    package main
    
    import (
    	"fmt"
    )
    
    func main() {
    	fmt.Println("main 执行")
    }
    
    func init()  {
    	fmt.Println("init 执行")
    }
    /*
    init 执行
    main 执行
    */
    ```

    

+ 导入多个包时,被最后导入的包会最先初始化并调用 它的 init() 函数

  + 导入包顺序 : `main --> A --> B --> C`
  + 初始化函数执行顺序 : `C.init() --> B.init() --> A.init() --> main.init()`

#### 5. Golang 中使用第三方包

##### 5.1 找到需要下载安装的第三方包的地址

+ 在 [https://pkg.go.dev/](https://pkg.go.dev/) 下查看常见的 golang 第三方包
+ 在 使用需要下载包的项目下 使用 `go mod init 项目名` 生成 go.mod

##### 5.2安装这个包

1. 方法 一 : `go get 包地址` (全局下载, 由于网络问题可能失败)

2. 方法 二 : `go mod dowwnload` (全局下载)

   + 设置Go 环境变量

     ```
     go env -w GOPROXY=https://goproxy.io,direct
     go env -w GO111MODULE=on
     ```

   + 使用 `go mod download`,然后运行程序会产生联系，生成依赖

   + 依赖包会自动下载到 **$GOPATH/pkg/mod**,多个项目可以共享缓存的 mod, 注意使用 go mod download 的时候首先需要在你的项目中引入第三方包

3. 方法 三 : `go mod vendor` 将依赖包复制到当前目录的 vendor 下 (仅限本项目使用, 首先需要在你的项目中引入第三方包)

4. 方法 四 : 配置 Goland 的 "settings --> Go Modules --> Environment" 设置为 [https://goproxy.io](https://goproxy.io),赋值使用包路径，到 Golang 根据提示下载

   