### Golang 文件、目录操作

#### 1. 打开和关闭文件

+ 只读打开文件 : `file, err = os.Open("file_path")`

  + **err != nil** 打开文件失败

+ 读写打开文件 (配置文件权限) : `file, err = os.OpenFile("file_path", os.O_CREATE|os.O_RDWR, 0666)`

  + `OpenFile(name string, flag int, perm FileMode) (*File, error)` 

    + **name** : 打开文件名称

    + **flag** : 打开文件模式

      | 模式            | 含义     |
      | --------------- | -------- |
      | **os.O_WRONLY** | 只写     |
      | **os.O_CREATE** | 创建文件 |
      | **os.O_RDONLY** | 只读     |
      | **os.O_RDWR**   | 读写     |
      | **os.O_TRUNC**  | 清空     |
      | **os.O_APPEND** | 追加     |

      

    + **perm** : 文件权限, 一个八进制数 

      + **r(读)** : 04
      + **w (写)** ： 02
      + **x (只写)** : 01

+ 读取后关闭文件流 : `defer file.Close()`

#### 2. 读取文件

##### 2.1 file.Read() 读取文件

+ 直接读取 (读取到文件不全)

  ```go
  package main
  
  import (
  	"fmt"
  	"os"
  )
  
  func main() {
  	// 只读形式打开文件
  	file, err := os.Open("E://Golang_study/go_base/demo24/01/main.go")
  	//file, err := os.Open("main.go")
  
  	defer file.Close()  // 必需关闭文件流
  	// err != nil 打开文件失败
  	if err != nil{
  		fmt.Println(err)
  		return
  	}else {
  		// 打开文件成功
  		// 定义切片接收读取到的数据 以及读取数据大小
  		var tempSlice = make([]byte, 128)
  		n, err := file.Read(tempSlice)
  		if err != nil {
  			fmt.Println("读取失败")
  			return
  		}
  		fmt.Printf("读取到了 %v 个字节", n)
  		// 读取到的是二进制字符串需要转化为字符串
  		fmt.Println(string(tempSlice))
  	}
  
  }
  /*
  读取到了 128 个字节package main
  
  import (
  	"fmt"
  	"os"
  )
  
  func main() {
  	// 只读形式打开文件
  	file, err := os.Open("E://Golang_study/go_bas
  */
  ```

  

+ 必需循环读取到文件所有内容 (通过 is.EOF 判读读取完毕结束循环, `strSlice = append(strSlice, tempSlice[:n]...)` 读取到多少字节的数据就存入多少,防止最后读取字节数不够而乱码)

  ```go
  package main
  
  import (
  	"fmt"
  	"io"
  	"os"
  )
  
  func main() {
  	file, err := os.Open("E://Golang_study/go_base/Day_02.md")
  	defer file.Close()
  	if err != nil {
  		fmt.Println("打开失败")
  		return
  	}else {
  		var strSlice []byte
  		tempSlice := make([]byte, 128)
  		for {
  			n, err := file.Read(tempSlice)
  			if err == io.EOF {
  				fmt.Println("读取完毕")
  				break
  			}
  			if err != nil {
  				print("读取失败")
  				return
  			}else {
  				fmt.Printf("读取了 %v 字节的数据\n", n)
  				strSlice = append(strSlice, tempSlice[:n]...)
  			}
  		}
  
  		fmt.Println(string(strSlice))
  	}
  }
  
  /*
  func main() {
  	// 只读形式打开文件
  	file, err := os.Open("E://Golang_study/go_base/demo24/01/main.go")
  	//file, err := os.Open("main.go")
  
  	defer file.Close()  // 必需关闭文件流
  	// err != nil 打开文件失败
  	if err != nil{
  		fmt.Println(err)
  		return
  	}else {
  		// 打开文件成功
  		// 定义切片接收读取到的数据 以及读取数据大小
  		var tempSlice = make([]byte, 128)
  		var strSlice []byte
  
  		for {
  			n, err := file.Read(tempSlice)
  			// io 包在读取完毕后会抛出异常
  			if err == io.EOF {
  				fmt.Println("读取完毕")
  				break
  			}
  			if err != nil {
  				fmt.Println("读取失败")
  				return
  			}
  			fmt.Printf("读取到了 %v 个字节\n", n)
  			strSlice = append(strSlice, tempSlice...)
  		}
  
  		// 读取到的是二进制字符串需要转化为字符串
  		//fmt.Println(string(tempSlice))
  		fmt.Println(string(strSlice))
  	}
  
  }
  
   */
  
  ```

  

##### 2.3 bufio 读取文件

+ 只读方式打开文件 : `file, err := os.Open(file_path)`

+ 创建 reader 对象 : `reader := bufio.NewReader(file)`

+ ReadString 读取文件 : `line, err := reader.ReadString("\n")`

+ 关闭文件流 : `defer file.Close`

+ 实例

  ```go
  package main
  
  import (
  	"bufio"
  	"fmt"
  	"io"
  	"os"
  )
  
  func main() {
  
  	file, err := os.Open("E://Golang_study/go_base/Day_02.md")
  	defer file.Close()
  	if err != nil {
  		fmt.Println("读取失败")
  		return
  	}
  	// 读取文件
  	var fileStr string
  	reader := bufio.NewReader(file)
  	for {
  
  		str, err := reader.ReadString('\n')  // 表示一次读取一行数据
  		if err == io.EOF{
              // 发出异常后仍会返回数据
  			fileStr += str
  			break
  		}
  		if err != nil {
  			fmt.Println(err)
  			return
  		}
  		fileStr += str
  	}
  
  	fmt.Println(fileStr)
  
  }
  
  ```

  

##### 2.4 ioutil 读取文件

+ `ioutil.ReadFile("file_path")` : 一次读取,不以流的形式读取 (读取小文件)

  ```go
  package main
  
  import (
  	"fmt"
  	"io/ioutil"
  )
  
  func main() {
  	strSlice, err := ioutil.ReadFile("E://Golang_study/go_base/Day_02.md")
  	if err != nil {
  		fmt.Println("读取失败")
  		return
  	}
  	fmt.Println(string(strSlice))
  }
  ```

#### 3. 文件的写入

##### 3.1 file.Write() 写入文件

+ 写入步骤

  1. 打开文件 `file, err = os.OpenFile("file_path", os.O_CREATE|os.O_RDWR, 0666)`
  2. 写入文件 : 
     1. `file.Write([]byte(str))` 写入字节切片数据
     2. `file.WriteString("直接写入")` 直接写入字符串数据
  3. 关闭文件流

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"os"
  	"strconv"
  )
  
  func main() {
  	// 追加 | 写入 | 新建
  	file, err := os.OpenFile("E://Golang_study/go_base/demo24/text.txt", os.O_CREATE|os.O_RDWR|os.O_APPEND, 0666)
  	defer file.Close()
  	if err != nil {
  		fmt.Println(err)
  		return
  	}
  	// 写入文件
  	//n, err1 := file.WriteString("String 字符串直接写入")
  	// 写入多行, 将数字转化为字符串
  	for i := 0; i < 10; i ++ {
  		var str = "String 字符串直接写入" + strconv.Itoa(i) + "\r\n"
  		n, err1 := file.Write([]byte(str))
  		//n, err1 := file.WriteString("String 字符串直接写入" + strconv.Itoa(i) + "\r\n")
  		if err1 != nil {
  			fmt.Println(err1)
  			return
  		}
  		fmt.Println(n)
  	}
  
  }
  
  ```

  

##### 3.2 bufio 写入文件

+ 步骤

  1. 打开文件 `file, err = os.OpenFile("file_path", os.O_CREATE|os.O_RDWR, 0666)`
  2. 创建 writer 对象 : `writer := bufio.NewWriter(file)`
  3. 将数据写入缓存 : `writer.WriterString("测试")`
  4. 将缓存中数据写入文件 : `writer.Flush()`
  5. 关闭文件流

+ 实例

  ```go
  package main
  
  import (
  	"bufio"
  	"fmt"
  	"os"
  	"strconv"
  )
  
  func main() {
  	// 追加 | 写入 | 新建
  	file, err := os.OpenFile("E://Golang_study/go_base/demo24/text.txt", os.O_CREATE|os.O_RDWR|os.O_APPEND, 0666)
  	defer file.Close()
  	if err != nil {
  		fmt.Println(err)
  		return
  	}
  
  	writer := bufio.NewWriter(file)
  	for i := 0; i < 10; i ++ {
  		n, err1 := writer.WriteString("String bufio写入" + strconv.Itoa(i) + "\r\n")
  		if err1 != nil {
  			fmt.Println(err1)
  			return
  		}
  		fmt.Println(n)
  		writer.Flush()
  	}
  }
  ```

  

##### 3.3 ioutil 写入文件

+ 步骤

  1. 定义写入字符串
  2. `err := ioutil.Write("path", []byte(str), 0666)`

+ `WriteFile(filename string, data []byte, perm os.FileMode)` : 无追加模式,写入会覆盖,每次写入一行,需要传入 字符串为 切片类型的字符串

+ 实例

  ```go
  package main
  
  import (
  	"fmt"
  	"io/ioutil"
  	"strconv"
  )
  
  func main() {
  
  	for i := 0; i < 10; i ++ {
  		var str = []byte("ioutil直接写入" + strconv.Itoa(i) + "\r\n")
  		err := ioutil.WriteFile("E://Golang_study/go_base/demo24/text.txt", str, 0666)
  		if err != nil {
  			fmt.Println(err)
  			return
  		}
  	}
  ```

  

##### 