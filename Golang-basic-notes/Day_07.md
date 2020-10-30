### Golang map 详解

#### 1. map 的介绍

+ map 是一种 无序的 key-value 数据结构, Go 语言的 map 是 引用类型 (改变变量副本时,会改变变量本身的值),必须初始化才可以使用
+ map 语法定义 : `map[KeyType]ValueType`
  + KeyType : 键的类型
  + ValueType : 键对应的值的类型
+ map 类型的变量 默认初始值为 nil, 需要使用 make() 函数 分配内存
+ make() 函数 : 用于 slice, map 和 channel 的初始化
+ make() 函数 创建 map 类型基本语法 (cap 表示 map 容量, 不是必须的) : `make(map[KeyType]ValueType, [cap])`

#### 2. map 的基本使用

1. make() 函数 创建 map 以及初始化

   ```go
   func main() {
   	//1. make 创建 map 类型数据
   	var userinfo = make(map[string]string)
   	userinfo["username"] = "张三"
   	userinfo["age"] = "20"
   	userinfo["sex"] = "男"
   	fmt.Println(userinfo)  // map[age:20 sex:男 username:张三]
       fmt.Println(userinfo["age"])  //  20
   }
   ```

2. 类型推导创建 map 类型 并且初始化

   ```go
   userinfo := map[string]string{
       "username": "李四",
       "age": "20",
       "gender": "男",
   }
   fmt.Println(userinfo) // map[age:20 gender:男 username:李四]
   fmt.Println(userinfo["gender"])  // 男
   ```

3. 直接创建并初始化 map 类型

   ```go
   var userinfo = map[string]string{
       "username": "李四",
       "age": "20",
       "gender": "男",
   }
   fmt.Println(userinfo) // map[age:20 gender:男 username:李四]
   fmt.Println(userinfo["gender"])  // 男
   ```

   

#### 3. 循环遍历 map 类型数据

1. for range 循环遍历 map 类型数据

   ```go
   userinfo := map[string]string{
       "username": "李四",
       "age": "20",
       "gender": "男",
   }
   
   for k, v := range userinfo {
       fmt.Println(k, v)
   }
   /*
   gender 男
   username 李四
   age 20
   */
   ```

#### 4. 判断 map 类型数据中 key 是否存在

+ 基本格式 : `v, ok := map["key"]` (如果 map 中 key 存在返回 ok 为 True 否则返回为 False, v 返回 map 中对应 key 的值)

  ```go
  var userinfo = make(map[string]string)
  userinfo["username"] = "张三"
  userinfo["age"] = "20"
  userinfo["sex"] = "男"
  
  v, ok := userinfo["age"]
  fmt.Println(v, ok) // 20 True
  ```

#### 5. 删除 map 数据 里面的 key 以及对应的值

+ 使用 delete() 内建函数 从 map 中删除 键值对 : `delete(map对象, key)`

  + map 对象 : 表示要删除键值对的 map 对象
  + key : 表示要删除键值对的 键

+ 实例

  ```go
  var userinfo = make(map[string]string)
  userinfo["username"] = "张三"
  userinfo["age"] = "20"
  userinfo["sex"] = "男"
  
  delete(userinfo, "sex")
  
  fmt.Println(userinfo) // map[age:20 username:张三]
  ```

#### 6. 元素为 map 类型的切片

+ 使用 make() 创建 map 类型的切片 : `make([]map[KeyString]ValueString, len, cap)`

+ 类似于 python 列表内存放字典

+ 实例

  ```go
  var userinfo = make([]map[string]string, 3, 3)
  
  fmt.Println(userinfo[0])  // map[]
  fmt.Println(userinfo[0] == nil)  // true
  if userinfo[0] == nil {
      userinfo[0] = make(map[string]string)
      userinfo[0]["age"] = "20"
      userinfo[0]["name"] = "张三"
  }
  if userinfo[1] == nil {
      userinfo[1] = make(map[string]string)
      userinfo[1]["age"] = "15"
      userinfo[1]["name"] = "李四"
  }
  if userinfo[2] == nil {
      userinfo[2] = make(map[string]string)
      userinfo[2]["age"] = "67"
      userinfo[2]["name"] = "万五"
  }
  
  fmt.Println(userinfo)  // [map[age:20 name:张三] map[age:15 name:李四] map[age:67 name:万五]]
  ```

+ map 类型切片遍历

  ```go
  var userinfo = make([]map[string]string, 3, 3)
  
  //fmt.Println(userinfo[0])  // map[]
  //fmt.Println(userinfo[0] == nil)  // true
  if userinfo[0] == nil {
      userinfo[0] = make(map[string]string)
      userinfo[0]["age"] = "20"
      userinfo[0]["name"] = "张三"
  }
  if userinfo[1] == nil {
      userinfo[1] = make(map[string]string)
      userinfo[1]["age"] = "15"
      userinfo[1]["name"] = "李四"
  }
  if userinfo[2] == nil {
      userinfo[2] = make(map[string]string)
      userinfo[2]["age"] = "67"
      userinfo[2]["name"] = "万五"
  }
  
  //fmt.Println(userinfo)  // [map[age:20 name:张三] map[age:15 name:李四] map[]]
  
  for i := 0; i < len(userinfo); i ++ {
      for k,v := range userinfo[i] {
          fmt.Printf("key: %v --- value: %v\n", k, v)
      }
  }
  /*
  key: age --- value: 20
  key: name --- value: 张三
  key: name --- value: 李四
  key: age --- value: 15
  key: age --- value: 67
  key: name --- value: 万五
  */
  ```

#### 7. 值为 切片类型的 map

+ 应对 一个 key 对应多个值 ,将多个值存至 切片内 作为 map 类型中 key 的值.

+ 基本格式 : `make(map[KeyString][]SliceString)`

+ 实例

  ```go
  var userinfo = make(map[string][]string)
  
  userinfo["username"] = []string{"张三"}
  userinfo["hobby"] = []string{
      "足球",
      "篮球",
      "傻球",
  }
  fmt.Println(userinfo)  //map[hobby:[足球 篮球 傻球] username:[张三]]
  ```

+ 遍历

  ```go
  var userinfo = make(map[string][]string)
  
  userinfo["username"] = []string{"张三"}
  userinfo["hobby"] = []string{
      "足球",
      "篮球",
      "傻球",
  }
  //fmt.Println(userinfo)
  
  for k, v := range userinfo {
      fmt.Println(k, v)
      for _, value := range v {
          fmt.Println(value)
      }
  }
  /*
  username [张三]
  张三
  hobby [足球 篮球 傻球]
  足球
  篮球
  傻球
  */
  ```

#### 8. map 的排序

+ map 排序后 并没有按照 key 值升序或降序排列,需要后期处理

+ 实例

  ```go
  map1 := make(map[int]int, 10)
  
  map1[10] = 100
  map1[2] = 20
  map1[5] = 50
  map1[4] = 40
  
  fmt.Println(map1) // map[2:20 4:40 5:50 10:100]
  
  for i, i2 := range map1 {
      fmt.Println(i, i2)
  }
  /*
  10 100
  5 50
  2 20
  4 40
  */
  ```

+ 按照 key 升序输出 map 的 key => value

  1. 把 map 的 key 放在切片内
  2. 对切片内值进行升序排序
  3. 循环遍历 切片内存的 key 间接对 map 中的数据按 key 值升序读取

  ```go
  map1 := make(map[int]int, 10)
  
  map1[10] = 100
  map1[2] = 20
  map1[5] = 50
  map1[4] = 40
  
  //fmt.Println(map1) // map[2:20 4:40 5:50 10:100]
  
  var keySlice []int
  for key, _ := range map1 {
      keySlice = append(keySlice, key)
  }
  
  fmt.Println(keySlice) // [10 2 5 4]
  
  sort.Ints(keySlice)
  
  fmt.Println(keySlice)  // [2 4 5 10]
  
  for _, v := range keySlice {
      fmt.Printf("key: %v --- value: %v\n", v, map1[v])
  	}
  /*
  key: 2 --- value: 20
  key: 4 --- value: 40
  key: 5 --- value: 50
  key: 10 --- value: 100
  */
  ```

#### 8. 写一个程序, 统计一个字符串中每个单词出现的次数

```go
var str = "how do you do"
var strSlice = strings.Split(str, " ")  // 返回一个切片

fmt.Println(strSlice) // [how do you do]

var strMap = make(map[string]int)

for _, val := range strSlice {
    strMap[val]++
}
/*
map[do:2 how:1 you:1]
*/
```











