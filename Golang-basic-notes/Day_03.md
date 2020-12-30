### Go 语言基本数据类型

#### 1.Golang 数据类型介绍

+ 基本数据类型
  + 整型、浮点型、布尔型、字符串
+ 复合数据类型
  + 数组、切片、结构体、函数、map、通道 (channel)、接口等
+ golang中分为值类型和引用类型
  + 值类型分别有：int系列、float系列、bool、string、数组和结构体
  + 引用类型有：指针、slice切片、管道channel、接口interface、map、函数等
+ 值类型的特点是：变量直接存储值，内存通常在栈中分配
+ 引用类型的特点是：变量存储的是一个地址，这个地址对应的空间里才是真正存储的值，内存通常在堆中分配

#### 2.整型

1. 有符号整形

   + 按长度分为 : int8 (-128, 127)、int16 (-32768, 32767)、int32、int64

2. 无符号整形

   + 对应长度划分 : uint8 (0, 255)、uint16 (0, 65535)、uint32、uint64

3. 特殊整型

   | 类型    | 描述                                           |
   | ------- | ---------------------------------------------- |
   | uint    | 32 位操作系统为 uint32，64 位操作系统为 uint64 |
   | int     | 32 位操作系统为 int32，64 位操作系统为 int64   |
   | uintptr | 无符号整形,用于存放一个指针                    |

   

4. `unsafe.Sizeof` : 查看不同长度的整型,在内存中的存储空间,使用时需要在 import 中引用 unsafe,无法查看 string 类型所占空间 

   ```go
   func main()  {
   	// 1. 定义 int 类型
   	var num int = -10
   	fmt.Println(num, unsafe.Sizeof(num))
   
   }
   /*
   -10 8
   */
   ```

5. int 不同长度直接的转换

   + 高位向低位转换时,如果超出存储空间就回西安市委低位最大或最小值

   ```go
   var a1 int32 = 10
   var a2 int64 = 12
   fmt.Println(int64(a1) + a2)
   // 22
   ```

   

6. int 数字字面量语法

   + %d : 10进制输出

   + %x : 16进制输出

   + %b : 二进制输出

   + %o : 8进制输出

     ```go
     var a1 int32 = 10
     fmt.Printf("10进制输出%d\n", a1)
     fmt.Printf("2进制输出%b\n", a1)
     fmt.Printf("8进制输出%o\n", a1)
     fmt.Printf("16进制输出%x", a1)
     /*
     10进制输出10
     2进制输出1010
     8进制输出12
     16进制输出a
     */
     ```

#### 3.浮点型

+ Go 语言支持两种浮点数,默认为 float64 位数据

  + float32 占 4 字节

    ```go
    var a float32 = 3.14
    fmt.Printf("%v --- %f,类型是%T,占用空间为%v", a, a, a, unsafe.Sizeof(a) )
    // 3.14 --- 3.140000,类型是float32,占用空间为4
    ```

    

  + float64 占 8 字节

    ```go
    var a float64 = 3.14
    fmt.Printf("%v --- %f,类型是%T,占用空间为%v", a, a, a, unsafe.Sizeof(a) )
    // 3.14 --- 3.140000,类型是float64,占用空间为8
    ```

  + %f 输出格式化 float 类型, %.2f : 输出数据时保留两位小数

    ```go
    var a float64 = 3.1415926
    fmt.Printf("%.2f",a) // 3.14
    ```

  + 使用科学计数法 (e) 表示浮点数据

    ```go
    var f = 3.14e2 // 表示3.14*10的2次方
    var f1 = 3.14e-2 // 表示3.14*10的-2次方
    fmt.Println(f, f1) // 314, 0.0314
    ```

  + Golang 中精度丢失问题 (使用第三方包 decimal 解决问题)

    ```go
    var d float64 = 1129.6
    fmt.Println(d*100) //112959.99999999999
    ```

  + float 类型转换为 int 型

    ```go
    var d float64 = 1129.6
    var e int = int(d)
    fmt.Println(e) // 1129
    ```

#### 4.布尔型

+ Go 中布尔类型只有 true 和 false

  + 布尔类型变量默认值是 false

    ```go
    var d bool
    fmt.Print(d) // false
    ```

    

  + Go 中不允许将整数强制转化为布尔型

  + 布尔型无法参与数值运算,也无法与其他类型转换

#### 5.byte 和 rune 类型

+ 组成每个字符串的元素叫做 '字符',可以通过遍历字符串元素获得字符。
+ 字符用 ('') 单引号 包裹起来,字符串用 ("")双引号 包裹起来

+ 定义字符, 字符属于 int 类型

  ```go
  var a = 'a'
  fmt.Printf("%v -- %T\n", a, a)  // 输出为 Ascii 码值 97 -- int32
  fmt.Printf("%c", a)  // 原样输出 a
  var str = "this"
  fmt.Printf("值 : %v ; 类型 : %T ; 原样输出 : %c", str[2], str[2], str[2]) // 值 : 105 ; 类型 : uint8 ; 原样输出 : i
  ```

+ Go 语言字符
  1. unit8 (byte) 类型 : 代表了 ASCII 码的一个字符

  2. rune 类型 : 代表一个 UTF-8 字符 (汉字使用)，实际是一个 int32

     ```go
     // 3. 一个汉字占用 3 个字节 , 汉字使用 utf-8 编码, 一个字母占用 1 个字节 使用 ASCII 编码
     var str = "this" // 占用四个字节
     var str1 = "你好"
     fmt.Println(unsafe.Sizeof(str)) // 包含指针等所占字节 16
     fmt.Println(len(str)) // 直接输出占用字节 4
     fmt.Println(len(str1)) // 6
     fmt.Printf("UTF_8值: %v ; 类型 : %T" ; 原样输出 %c, str1[1], str1[1], str1[1]) // UTF_8值: 189 ; 类型 : uint8 ; 原样输出 : 好
     ```

  3. 循环输出含中英文的字符串 (如果直接循环输出无法识别汉字,占用字符数不同)

     + 直接循环输出 使用的是 byte 类型

       ```go
       str := "你好 GGboy"
       for i := 0; i<len(str); i++ {
           fmt.Printf("%v(%c)", str[i], str[i]) // 228(ä)189(½)160( )229(å)165(¥)189(½)32( )71(G)71(G)98(b)111(o)121(y)
           }
       ```

     + 加以改进输出 使用的是 rune 类型

       ```go
       str := "你好 GGboy"
       for _, r := range str{
           fmt.Printf("%v(%c)", r, r) // 20320(你)22909(好)32( )71(G)71(G)98(b)111(o)121(y)
       }
       ```

  4. 修改字符串

     + 先将其转换成 []rune 或 []byte 类型,完成后再转换为 string, 无论哪种转换,都会重新分配内存,并复制字节数组

       ```go
       s1 := "big"
       // 强制转换类型
       byteS1 := []byte(s1)
       byteS1[0] = 'p'
       fmt.Println(string(byteS1)) // pig
       
       s2 := "白萝卜 hello"
       runeS2 := []rune(s2)
       runeS2[0] = '红'
       fmt.Println(string(runeS2)) // 红萝卜 hello
       ```

#### 6. Golang 基本数据类型转换

1. 数值类型之间的相互转换 (整型和浮点型)

   + Go 运算需要转换为相同数据类型

   + 转换时建议从低位转换为高位,防止高位转化为低位时数据溢出

   + int8 --> int16

     ```go
     var a int8 = 20
     var b int16 = 40
     var c = int16(a) + b // 转换为相同类型才可以进行计算
     fmt.Println(c) // 60
     ```

   + float32 --> float64

     ```go
     var a float32 = 20
     var b float64 = 40
     var c = float64(a) + b // 转换为相同类型才可以进行计算
     fmt.Println(c) // 60
     ```

   + 整型和浮点型转换

     ```go
     var a float32 = 20
     var b int = 40
     var c = float32(b) + a // 转换为相同类型才可以进行计算
     fmt.Println(c) // 60
     ```

2. 其他类型转换成 String 类型

   1. Sprintf 把其他类型转换成 string 类型 (转换时需要注意转换的格式为 int : %d; float : %f; bool : %t byte : %c)	

      ```go
      var i int = 20
      var f float64 = 12.456
      var t bool = true
      var b byte = 'a'
      str1 := fmt.Sprintf("%d", i)
      str2 := fmt.Sprintf("%f", f)
      str3 := fmt.Sprintf("%t", t)
      str4 := fmt.Sprintf("%c", b)
      fmt.Printf("%v--类型: %T", str1, str1) // 20--类型: string
      fmt.Printf("%v--类型: %T", str2, str2) //12.456000--类型: string
      fmt.Printf("%v--类型: %T", str3, str3) // true--类型: string
      fmt.Printf("%v--类型: %T", str4, str4) // a--类型: string
      ```

      

   2. 使用 strconv 包中的几种转换方法 (即可以将其他类型转换为string类型,也可以将 string 类型转换为 其他类型)

      1. `FormatInt(i int64, base int)` : 整数转化为字符串

         1. 参数1 ; 必须为 int64 格式
         2. 参数2 : 显示进制数

      2. `FormatFloat(f float64, fmt byte, prec, bitSize int)` :

         1. 参数1 : 必须为 float64 格式
         2. 参数2 : 格式化类型
            1. 'f' : (-ddd.dddd)
            2. 'b' : (-ddddp±ddd),指数为二进制
            3. 'e' : (-d.dddde±dd),十进制指数
            4. 'E' : (-d.ddddE±dd),十进制指数
            5. 'g' : (指数很大时用'e'格式, 否则 'f' 格式)
            6. 'G' : (指数很大时用'E'格式, 否则 'f' 格式)
         3. 参数3 : 保留的小数点, -1 (不对小数点格式化)
         4. 参数4 : 格式化类型 (可以传入 64 或 32 代表格式化为 64 位 或 32 位)

      3. `FormatBool(b bool)` : 布尔值转化字符串,意义不大

      4. `FormatUint(i uint64, base int)` : 字符传入输出为 ASCII 码

         ```go
         var i int = 20
         var f float64 = 12.456
         var t bool = true
         var b byte = 'a'
         str1 := strconv.FormatInt(int64(i), 10)
         str2 := strconv.FormatFloat(f, 'f', -1, 64)
         str3 := strconv.FormatBool(t)
         str4 := strconv.FormatUint(uint64(b), 10)
         fmt.Printf("%v--类型: %T", str1, str1) // 20--类型: string
         fmt.Printf("%v--类型: %T", str2, str2) // 12.456--类型: string
         fmt.Printf("%v--类型: %T", str3, str3) // true--类型: string
         fmt.Printf("%v--类型: %T", str4, str4) // 97--类型: string
         ```

3. String 类型转换为数值类型

   1. `ParseInt(s string, base int, bitSize int)` : string 类型转换为 int 类型

      ```go
      var s = "1234"
      i64, _ := strconv.ParseInt(s, 10, 64)
      fmt.Printf("%v--类型: %T", i64, i64) // 1234--类型: int64
      ```

   2. `ParseFloat(s string, bitSize int)` : string 类型转换成 float 类型

      ```go
      str := "3.1415926"
      v1, _ := strconv.ParseFloat(str, 64)
      v2, _ := strconv.ParseFloat(str, 32)
      fmt.Printf("%v--类型: %T", v1, v1) // 3.1415926--类型: float64
      fmt.Printf("%v--类型: %T", v2, v2) // 3.141592502593994--类型: float64
      ```

   3. `ParseBool(str string)` : string 类型转换为 布尔型,意义不大,不建议如此

4. 数值类型没法和 bool 类型进行转换

   

   