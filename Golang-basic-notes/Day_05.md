### Go 语言中的流程控制

#### 1. if else (分支结构)

##### 1.1  if 条件判断基本写法

```go
if 表达式 1 {
    分支 1
}else if 表达式 2 {
    分支 2
}else {
    分支 3
}
```

+ 常规写法

  ```go
  func main() {
  //	最简单的 if 语句
  //	flag := true
  //	if flag {
  //		fmt.Println("flag=true")
  //	}
  	age := 30
  	if age > 20 {
  		fmt.Println("成年人")
  	}else {
  		fmt.Println("没满20")
  	}
      fmt.Println(age)
  }
  ```

  

+ 另一种写法

  ```go
  func main() {
  	if age := 30; age > 20{
  		fmt.Println("成年人")
  	}else{
  		fmt.Println("你猜")
  	}
  }
  ```

+ 两种写法区别

  + 常规写法 age 为全局变量;写在判断内为局部变量,只可以在条件语句内使用

#### 2. for (循环结构)

##### 2.1 for 循环基本格式

```go
for 初始语句;条件表达式;结束语句 {
    循环体语句
}
```

+ 常规写法

  ```go
  for i := 0;i<10;i++{
      fmt.Println(i)
  }
  ```

+ 第二种写法 (将初始化变量作为全局变量)

  ```go
  i := 1
  for ; i < 11; i++ {
      fmt.Println(i)
  }
  ```

+ 第三种写法 (在循环语句中去除初始化语句与结束语句,也可以写为死循环)

  ```go
  i := 1
  for i < 11 {
      fmt.Println(i)
      i++
  }
  ```

+ 第四种写法 (死循环,无限循环: 使用 break 跳出循环)

  + 循环体语句

    ```go
    for {
        循环体语句
    }
    ```

  + 代码示例

    ```go
    i := 1
    for {
        if i < 11 {
            fmt.Println(i)
        }else {
            break
        }
        i++
    }
    ```

##### 2.2 for 循环的嵌套

```go
var row int = 4
var col int = 4
for i := 1; i<=row; i++{
    for j := 1; j<=col; j++ {
        fmt.Print("*")
    }
    fmt.Print("\n")
}
// 7. 练习 : 打印 九九乘法表
for i := 1; i <= 9; i++ {
    for j := 1; j <= i; j++ {
        fmt.Printf("%vx%v=%v\t", i, j, i*j)
    }
    fmt.Println()
}
```

#### 3. for range (键值循环)

##### 3.1 for range 遍历返回值规律

1. **数组**、**切片**、**字符串**返回索引和值
2. **map** 返回键和值
3. **通道** (channel) 只返回通道内的值
4. 循环遍历不需要的"key/value"可以用 "_" 进行占位

##### 3.2 for range 基本语法

1. 字符串遍历

   ```go
   func main() {
   	var str string = "你好 golang"
   
   	for key, value := range str{
   		fmt.Println("key=",key,"value=", value)
           fmt.Printf("key=%v, value=%c\n", key, value)
   	}
   }
   /*
   Println默认 汉字输出 Unicode 编码;英文输出 ASCII 码
   key= 0 value= 20320
   key= 3 value= 22909
   key= 6 value= 32
   key= 7 value= 103
   key= 8 value= 111
   key= 9 value= 108
   key= 10 value= 97
   key= 11 value= 110
   key= 12 value= 103
   Printf 输出
   key=0, value=你
   key=3, value=好
   key=6, value= 
   key=7, value=g
   key=8, value=o
   key=9, value=l
   key=10, value=a
   key=11, value=n
   key=12, value=g
   */
   ```

2. 切片遍历

   ```go
   func main() {
   	// 定义切片
   	var arr = []string{"php", "java", "python", "golang"}
   	for key, value := range arr{
   		fmt.Printf("key=%v, value=%v\n", key, value)
   	}
   }
   /*
   key=0, value=php
   key=1, value=java
   key=2, value=python
   key=3, value=golang
   */
   ```

#### 4. switch case (对大量值进行条件判断)

##### 4.1 基本格式

1. 常规写法

   ```go
   switch 变量 {
       case 值1 :
       	执行语句
       	break
       case 值2 :
       	执行语句
       	break
       default:
       	执行语句
   }
   ```

2. case 表达式 判断, switch 不需要传值

   ```go
   var age = 30
   switch {
   case age < 20:
       fmt.Println("未满20")
   case 20 <= age && age <= 60:
       fmt.Println("工作")
   case 60 < age:
       fmt.Println("累了")
   default:
       fmt.Println("输入错误")
   }
   ```

   

3. 第二种写法 (将变量写在判断语句中)

   ```go
   switch score := "A"; score {
   case "A","B","C":
       fmt.Println("及格")
   case "D":
       fmt.Println("不及格")
   }
   ```

4. golang 中 switch 内 break 可以不写;一个分支可以有多个值

   ```go
   var n = 5
   switch n {
   case 1,3,5,7,9:
       fmt.Println("奇数")
   case 2,4,6,8,10:
       fmt.Println("偶数")
   }
   ```

   

##### 4.2 举例说明 

```go
func main() {
	// 判断文件类型
	var ext = ".html"
	switch ext {
	case ".html":
		fmt.Println("text/html")
		break
	case ".css":
		fmt.Println("text/css")
		break
	case ".js":
		fmt.Println("text/javascript")
		break
	default:
		fmt.Println("找不到此类型")
	}
}
```

##### 4.3 switch 的穿透 fallthrough

+ `fallthrough` 语法可以执行满足条件的 case 的下一个 case，为了兼容 C 语言中的 case 设计

+ 一个 `fallthrough` 仅仅 穿透一层 case

+ 实例

  ```go
  var age = 30
  switch {
  case age < 20:
      fmt.Println("未满20")
  case 20 <= age && age <= 60:
      fmt.Println("工作")
      fallthrough
  case 60 < age:
      fmt.Println("累了")
  default:
      fmt.Println("输入错误")
  }
  /*
  工作
  累了
  */
  ```

#### 5. break、continue、goto (跳出语句)

##### 5.1 break (跳出循环)

+ 用于循环语句中跳出循环 (for/switch)

+ break 在 switch (开关语句) 中执行一条 case 后跳出语句

+ 在多重循环中,可以用标号 label 标出想 break 的循环

  ```go
  label1:
  	for i := 0; i < 2; i++ {
  		for j := 0; j< 10; j++{
  			if j == 3 {
  				break label1
  			}
  			fmt.Printf("i=%v, j=%v\n", i, j)
  		}
  	}
  /*
  i=0, j=0
  i=0, j=1
  i=0, j=2
  */
  ```

  

##### 5.2 continue (跳出此次循环,继续下次循环)

+ 常规用法

  ```go
  for i := 0; i<=3;i++{
      for j := 0; j<10;j++{
          if j == 2{
              //continue here
              continue
          }
          fmt.Printf("i=%v,j=%v\n",i,j)
      }
  }
  /*
  i=0,j=0
  i=0,j=1
  i=0,j=3
  i=0,j=4
  i=0,j=5
  i=0,j=6
  i=0,j=7
  i=0,j=8
  i=0,j=9
  i=1,j=0
  i=1,j=1
  i=1,j=3
  i=1,j=4
  i=1,j=5
  i=1,j=6
  i=1,j=7
  i=1,j=8
  i=1,j=9
  i=2,j=0
  i=2,j=1
  i=2,j=3
  i=2,j=4
  i=2,j=5
  i=2,j=6
  i=2,j=7
  i=2,j=8
  i=2,j=9
  i=3,j=0
  i=3,j=1
  i=3,j=3
  i=3,j=4
  i=3,j=5
  i=3,j=6
  i=3,j=7
  i=3,j=8
  i=3,j=9
  */
  ```

  

+ 在 continue 语句后添加标签时,表示开始标签对应的循环

  ```go
  here:
  	for i := 0; i<=3;i++{
  		for j := 0; j<10;j++{
  			if j == 2{
  				continue here
  				//continue
  			}
  			fmt.Printf("i=%v,j=%v\n",i,j)
  		}
  	}
  /*
  i=0,j=0
  i=0,j=1
  i=1,j=0
  i=1,j=1
  i=2,j=0
  i=2,j=1
  i=3,j=0
  i=3,j=1
  */
  ```

  

##### 5.3 goto (跳转到指定标签)

+ 基本语法

  ```go
  var n = 30
  if n > 24 {
      fmt.Printf("成年人")
      goto label3
  }
  fmt.Printf("aaa")
  fmt.Printf("bbb")
  label3:
  fmt.Printf("ccc")
  /*
  成年人ccc
  */
  ```

  