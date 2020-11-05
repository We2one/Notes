### Golang 中的数组

#### 1. 数组定义

+ 标准格式 : `var 数组变量名 [元素数量]数组类型`

+ 数组的长度是类型的一部分,数组长度为固定不变:

  ```go
  var b [3]int
  // 整数数组,长度固定为 3
  func main()  {
  	var arr1 [4]int
  	var arr2 [3]int
  	var strArr [3]string
  
  	fmt.Printf("arr1 : %T arr2 : %T, strArr: %T", arr1, arr2, strArr)
  }
  // arr1 : [4]int arr2 : [3]int, strArr: [3]string
  ```

+ 初始化数组

  ```go
  //func main()  {%T, strArr: %T", arr1, arr2, strArr)
  	var arr1 [4]int
  	var strArr [3]string
  
  	fmt.Println(arr1) // [0 0 0 0]
  	fmt.Println(strArr) // [  ]
  }
  ```

  + 初始化方法一

    ```go
    func main()  {%T, strArr: %T", arr1, arr2, strArr)
    	var arr1 [4]int
    	arr1[0] = 23
    	arr1[2] = 23
    	arr1[3] = 23
    	arr1[1] = 12
    
    	fmt.Println(arr1) // [23 12 23 23]
    }
    ```

  + 初始化方法二

    ```go
    var arr1 = [3]int{22, 11, 44}
    fmt.Println(arr1) // [22 11 44]
    ```

  + 初始化方法三 : 让编译器根据初始值的个数自行推断数组的长度

    ```go
    var arr1 = [...]int{1,2,3,4}
    fmt.Println(arr1) // [1 2 3 4]
    fmt.Println(len(arr1)) // 4
    ```

  + 初始化方法四 : 通过指定索引的方式初始化数组

    ```go
    a := [...]int{1:1, 4:4}
    fmt.Println(a) // [0 1 0 0 4]
    ```

    

  + 改变数组值

    ```go
    var arr1 = [...]int{1,2,3,4}
    arr1[2] = 6
    fmt.Println(arr1) // [1 2 6 4]
    fmt.Println(len(arr1)) // 4
    ```

#### 2. 数组的遍历

+ for 循环遍历

  ```go
  var arr1 = [3]int{22,11,44}
  for i := 0; i < len(arr1); i++ {
      fmt.Println(arr1[i])
  }
  /*
  22
  11
  44
  */
  ```

+ for range 循环遍历

  ```go
  arr1 := [...]string{"php", "jave", "c++"}
  for _,value := range arr1 {
      fmt.Println(value)
  }
  /*
  php
  jave
  c++
  */
  ```

#### 3. 数组的类型

+ 在 Golang 中 数组是值类型,赋值和传参会复制整个数组.因此改变副本的值,不会改变本身的值

+ 值类型 : 基本数据类型 和 数组, 赋值和传参会复制整个数组.因此改变副本的值,不会改变本身的值

  ```go
  var a = 10
  b := a
  a = 20
  fmt.Println(a, b) // 20, 10
  var arr1 = [...]int{1,2,3,4}
  arr2 := arr1
  arr1[0] = 11
  fmt.Println(arr1, arr2) // [11 2 3 4] [1 2 3 4]
  ```

  

+ 引用数据类型 : 切片 (使用指针指向赋值数据,改变一个变量副本的时候会改变原数据)

  ```go
  // 引用数据类型 : 切片
  var arr1 = []int{1,2,3}
  arr2 := arr1
  arr1[2] = 32
  fmt.Println(arr1, arr2) // [1 32 3] [1 32 3]
  ```

  

#### 4. 多维数组

+ 基本类型 : `var 数组变量名 [元素数量][元素数量]...[元素数量]Type`

+ 多维数组定义

  ```go
  // 多维数组
  var arr = [2][4]string{
      {"四川", "北京", "上海", "成都"},
      {"新疆", "蒙古", "东北", "苏杭"},
  }
  
  fmt.Println(arr) // [[四川 北京 上海 成都] [新疆 蒙古 东北 苏杭]]
  fmt.Println(arr[1][2])  // 东北
  ```

+ 循环遍历多维数组

  ```go
  // 多维数组
  var arr = [2][4]string{
      {"四川", "北京", "上海", "成都"},
      {"新疆", "蒙古", "东北", "苏杭"},
  }
  
  for _, v1 := range arr {
      for _, v2 := range v1 {
          fmt.Println(v2)
      }
  }
  
  //for i:=0;i<len(arr);i++{
  //    for j:=0;j<len(arr[i]);j++{
  //        fmt.Println(arr[i][j])
  //    }
  //}
  /*
  四川
  北京
  上海
  成都
  新疆
  蒙古
  东北
  苏杭
  */
  ```

+ 定义n维数组的另一种方式 : `var arr = [...][n]Type{}`

### Golang 中的切片

#### 1. 切片的定义

+ 切片 (Slice) : 一个拥有相同类型元素的可变长度的序列,基于数组类型做的一层封装,支持自动扩容

+ 切片 : 是一个引用类型,内部结构包括 : 地址、长度 和 容量

+ 声明语法: `var name []Type`

+ 初始化切片

  1. 声明切片方法一

     ```go
     var arr = []int{1,2,3,4,5}
     fmt.Printf("%v - %T - 长度 %v", arr, arr, len(arr)) // [1 2 3 4 5] - []int - 长度 5
     ```

  2. 声明切片方法二

     ```go
     var arr = []int{1:2,3,4:5}
     fmt.Printf("%v - %T - 长度 %v", arr, arr, len(arr)) // [0 2 3 0 5] - []int - 长度 5
     ```

  3. 声明切片方法三 : 使用 make() 关键词

     ```go
     a := make([]int, 4, 8)
     fmt.Println(a) // [0 0 0 0]
     ```

     

#### 2. nil 默认赋值

+ 当声明一个变量却未赋值时,Golang自动为变量赋一个零值

+ 声明切片的默认值是 nil	

  | 变量类型  | 零值  |
  | --------- | ----- |
  | bool      | false |
  | numbers   | 0     |
  | string    | ""    |
  | pointers  | nil   |
  | slices    | nil   |
  | maps      | nil   |
  | channels  | nil   |
  | functions | nil   |

+ 实例证明

  ```go
  var arr []int
  fmt.Printf("%v\n", arr) // []
  fmt.Println(arr == nil) // True
  ```

#### 3. 切片的循环遍历

+ 切片的循环遍历和数组一样

  + for range 循环遍历

    ```go
    var strSlice = []string{"php", "java", "C++", "Python"}
    
    for _,v := range strSlice {
        fmt.Println(v)
    }
    /*
    php
    java
    C++
    Python
    */
    ```

  + for 循环

    ```go
    var strSlice = []string{"php", "java", "C++", "Python"}
    
    for i:=0;i<len(strSlice);i++{
        fmt.Println(strSlice[i])
    }
    /*
    php
    java
    C++
    Python
    */
    ```

#### 4. 基于数组定义切片

+ 切片 = 数组名[start: stop]
  + 获取数组所有制为一个切片

    ```go
    // 基于数组定义切片
    a := [5]int{1,2,5,7,3}
    
    // 获取数组所有值
    b := a[:]
    fmt.Printf("%v - %T", b, b) // [1 2 5 7 3] - []int
    ```

  + 截取数组指定部分 (左包右不包)

    ```go
    a := [5]int{1,2,5,7,3}
    
    b := a[1:4]
    fmt.Printf("%v - %T", b, b) // [2 5 7] - []int
    ```

  + 从左边指定位置开始获取到最后

    ```go
    a := [5]int{1,2,5,7,3}
    
    b := a[1:]
    fmt.Printf("%v - %T", b, b) // [2 5 7 3] - []int
    ```

    

  + 获取右边数据前所有数据

    ```go
    a := [5]int{1,2,5,7,3}
    
    b := a[:3]
    fmt.Printf("%v - %T", b, b) // [1 2 5] - []int
    ```

#### 5. 切片再切片

+ 通过对切片切片来获得切片

+ 实例

  ```go
  a := []string{"北京", "上海", "广州", "苏州", "四川"}
  b := a[1:]
  fmt.Printf("%v - %T", b, b) // [上海 广州 苏州 四川] - []string
  ```

#### 6. 切片的长度和容量

+ 切片有自己的长度和容量

  + 长度 : 切片所包含的元素个数,可以通过内置的 len() 函数求长度
  + 容量 : 从**切片第一个元素**开始数,到其**底层数组元素末尾**的个数,使用内置的 cap() 函数求容量

+ 实例

  ```go
  a := []string{"北京", "上海", "广州", "苏州", "四川"}
  fmt.Printf("切片的长度为 %v, 切片的容量为 %v", len(a), cap(a))
  // 切片的长度为 5, 切片的容量为 5
  b := a[1:]
  fmt.Printf("切片的长度为 %v, 切片的容量为 %v", len(b), cap(b))
  // 切片的长度为 4, 切片的容量为 4
  s := a[1: 3]
  fmt.Printf("切片的长度为 %v, 切片的容量为 %v", len(s), cap(s))
  // 切片的长度为 2, 切片的容量为 4
  c := a[:3]
  fmt.Printf("切片的长度为 %v, 切片的容量为 %v", len(c), cap(c))
  // 切片的长度为 3, 切片的容量为 5
  ```

#### 7. 切片的本质

+ 切片的本质 : 对底层数组的封装
+ 切片包含的三个信息: 底层数组的指针、切片的长度(len) 和 切片的容量 (cap)

#### 8. 使用 make() 函数构造切片

+ 格式 : `make([]Type, size, cap)`

  + 实例

    ```go
    // make() 函数构造切片
    a := make([]int, 4, 8)
    fmt.Println(a) // [0 0 0 0]
    fmt.Printf("长度: %v, 容量: %v", len(a), cap(a)) // 长度: 4, 容量: 8
    ```

+ 切片的修改

  + 方法一

    ```go
    var sliceA = make([]int, 4, 8)
    sliceA[0] = 12
    sliceA[1] = 32
    sliceA[2] = 45
    sliceA[3] = 67
    fmt.Println(sliceA) // [12 32 45 67]
    
    sliceB := []string{"php", "java", "golang"}
    
    sliceB[2] = "go"
    
    fmt.Println(sliceB) // [php java go]
    ```

  + 方法二 ,var 定义切片 赋值会发生越界错误,无法通过下标方式给切片扩容,需要使用 append 方法

    ```go
    var sliceC []int
    
    fmt.Printf("长度 %v, 容量 %v",len(sliceC), cap(sliceC)) // 长度 0, 容量 0
    ```

+ append 方法扩容切片

  + 动态添加

    ```go
    var sliceC []int
    
    //sliceC = append(sliceC, 12)
    //sliceC = append(sliceC, 16)
    sliceC = append(sliceC, 12,34,56,77)
    
    fmt.Printf("长度 %v, 容量 %v", len(sliceC), cap(sliceC)) // 长度 4, 容量 4
    ```

  + append 合并切片,追加

    ```go
    sliceA := []string{"php", "java"}
    sliceB := []string{"nodejs", "go"}
    
    sliceA = append(sliceA, sliceB...)
    fmt.Println(sliceA) // [php java nodejs go]
    ```

+ 切片的扩容策略 : 容量是 2^n 

  ```go
  var sliceC []int
  for i:=1;i<=10;i++{
      sliceC = append(sliceC, i)
      fmt.Printf("sliceC: %+v, 长度: %v, 容量: %v\n", sliceC, len(sliceC), cap(sliceC))
  /*
  sliceC: [1], 长度: 1, 容量: 1
  sliceC: [1 2], 长度: 2, 容量: 2
  sliceC: [1 2 3], 长度: 3, 容量: 4
  sliceC: [1 2 3 4], 长度: 4, 容量: 4
  sliceC: [1 2 3 4 5], 长度: 5, 容量: 8
  sliceC: [1 2 3 4 5 6], 长度: 6, 容量: 8
  sliceC: [1 2 3 4 5 6 7], 长度: 7, 容量: 8
  sliceC: [1 2 3 4 5 6 7 8], 长度: 8, 容量: 8
  sliceC: [1 2 3 4 5 6 7 8 9], 长度: 9, 容量: 16
  sliceC: [1 2 3 4 5 6 7 8 9 10], 长度: 10, 容量: 16
  */
  ```

  1. 首先判断,如果新申请的容量 (cap) 大于 2 倍的旧容量 (old.cap), 最终容量 (newwcap) 就是新申请的容量 (cap)
  2. 否则判断,如果旧切片长度小于 1024 ,则最终容量就是旧容量的两倍,即 (newwcap=doublecap)
  3. 否则判断,如果旧切片长度大于等于1024,则最终容量(newcap) 从旧容量开始循环增加原来的 1/4, 即 (newcap=old.cap, for {newwcap += newcap/4}) 直到最终的容量大于等于新申请的容量,即 (newwcap >=cap)
  4. 如果最终容量 (cap) 的计算值溢出,则最终容量就是新申请容量

#### 9. 使用 copy() 函数复制切片

+ 切片是引用类型 : 改变副本会对切片本身产生改变

+ 改变副本改变本身

  ```go
  sliceA := []int{1,2,3,45}
  sliceB := sliceA
  sliceB[0] = 11
  fmt.Println(sliceA, sliceB) 
  /*
  [11 2 3 45] 	
  [11 2 3 45]
  */
  ```

+ 改变副本不影响本身

  ```go
  sliceA := []int{1,2,3,45}
  sliceB := make([]int, 4, 4)
  //将 sliceA 复制到 sliceB 内
  copy(sliceB, sliceA)
  sliceB[1] = 323
  fmt.Println(sliceA, sliceB)
  /*
  [1 2 3 45] 
  [1 323 3 45]
  */
  ```

#### 10. 从切片中删除元素

+ Go 中没有专用于删除切片元素的方法,但是可以用 append 方法 达到效果

  ```go
  sliceA :=[]int{32,53,123,54532,4231,13,231,12}
  // 删除索引值为 2 的数据
  sliceA = append(sliceA[:2], sliceA[3:]...)
  
  fmt.Println(sliceA) // [32 53 54532 4231 13 231 12]
  ```

#### 11. 通过切片对字符串进行修改

+ 字符串转换为 **byte** 类型切片 (**字符串无汉字**)

  ```go
  s := "big"
  byteStr := []byte(s)
  
  byteStr[1] = 'o'
  
  fmt.Println(byteStr, string(byteStr)) // [98 111 103] bog
  fmt.Printf("%s", byteStr) // bog
  ```

  

+ 字符串转换为 **rune** 类型切片 (**字符串有汉字**)

  ```go
  s := "big"
  runeStr := []rune(s)
runeStr[1] = 'o'
  fmt.Printf("%q", runeStr) // ['b' 'o' 'g']
  fmt.Println(string(runeStr)) // bog
  ```

### Golang 数组切片的排序算法以及 sort 包

#### 1. 选择排序

+ 算法编写

  ```go
  func main() {
  	/*
  	选择排序: 进行从小到大排序
  	概念 : 通过 比较 首先选出最小的数放在第一个位置上,然后在其余的数中选出次小的数放在第二个位置上
  	[9, 8, 7, 6, 5, 4]
  	*/
  	var numSlice = []int{9, 8, 7, 6, 5, 4}
  
  	for i := 0; i < len(numSlice); i ++ {
  		for j := i+1; j < len(numSlice); j ++ {
  			if numSlice[i] > numSlice[j]{
  				temp := numSlice[i]
  				numSlice[i] = numSlice[j]
  				numSlice[j] = temp
  			}
  
  		}
  	} 
  	fmt.Println(numSlice)  // [4 5 6 7 8 9]
  }
  ```

  

#### 2. 冒泡排序

+ 算法编写

  ```go
  func main() {
  	/*
  	冒泡排序 :
  	概念 : 从头到尾,比较两个相邻元素的大小,如果符合交换条件,交换两个元素的位置
  	特点 : 每一次比较中, 都会选出一个最大的数,放在正确的位置
  	 */
  
  	var numSlice = []int{4, 6, 5, 7, 3}
  	for i := 0; i < len(numSlice); i ++ {
  		for j := 0; j < len(numSlice)-1; j ++ {
  			if numSlice[j+1] < numSlice[j] {
  				numSlice[j], numSlice[j+1] = numSlice[j+1], numSlice[j]
  			}
  		}
  	}
  	fmt.Println(numSlice) // [3 4 5 6 7]
  
  }
  
  ```

#### 3. sort 包

1. sort 升序排序

   + int 数组或切片 : `sort.Ints(arr)`

     ```go
     var numSlice = []int{4, 6, 5, 7, 3}
     sort.Ints(numSlice)
     fmt.Println(numSlice) // [3 4 5 6 7]
     ```

     

   + float64 数组或切片 : `sort.Float64s(arr)`

   + string 数组或切片 : `sort.Strings(arr)`

2. sort 降序排序 : `sort.Sort(sort.Reverse(slice))`

   + int 数组或切片 : `sort.Sort(sort.Reverse(sort.IntSlice(arr)))`

     ```go
     var numSlice = []int{4, 6, 5, 7, 3}
     sort.Sort(sort.Reverse(sort.IntSlice(numSlice)))
     
     fmt.Println(numSlice)  // [7 6 5 4 3]
     ```

     

   + float64 数组或切片 : `sort.Sort(sort.Reverse(sort.Float64Slice(arr)))`

   + string 数组或切片 : `sort.Sort(sort.Reverse(sort.StringSlice(arr)))`







