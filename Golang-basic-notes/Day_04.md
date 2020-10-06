### Golang 中运算符

#### 算术运算符

| 运算符 | 描述                                                 |
| ------ | ---------------------------------------------------- |
| +      | 相加                                                 |
| -      | 相减                                                 |
| *      | 相乘                                                 |
| /      | 相除(两数都为整数相除值为整数,都为小数,相除值为小数) |
| %      | 取余                                                 |

```go
var a = 5
var b = 4
var c = 5.0
var d = 4.0
fmt.Println(a+b) // 9
fmt.Println(a-b) // 1
fmt.Println(a*b) // 20
fmt.Println(a/b) // 1
fmt.Println(c/d) // 1.25
fmt.Println(a%b) // 1
```

+ Golang 中 `++` (自增) 和 `--` (自减) 只能单独使用,不能与赋值运算符一起使用

  ```go
  var a = 5
  var b = 4
  a++
  b--
  fmt.Println(a) // 6
  fmt.Println(b) // 3
  ```

  

+ Golang 中没有 `++i` 和 `--i` 的写法

#### 关系运算符(返回布尔值)

| 运算符 | 描述                         |
| ------ | ---------------------------- |
| `==`   | 比较两个值是否相等           |
| `!=`   | 比较两个值是否不等           |
| `>`    | 比较左边值是否大于右边值     |
| `<`    | 比较右边值是否大于左边值     |
| `>=`   | 比较左边值是否大于等于右边值 |
| `<=`   | 比较右边值是否大于等于左边值 |

```go
var a = 5
var b = 4
fmt.Println(a>b) // true
fmt.Println(a<b) // false
fmt.Println(a==b) // false
fmt.Println(a!=b) // true	
fmt.Println(a>=b) // true
fmt.Println(a<=b) // false
```

#### 逻辑运算符(返回布尔值)

| 运算符 | 描述                                                       |
| ------ | ---------------------------------------------------------- |
| `&&`   | 逻辑 AND 运算符,两边都 true 则为 true                      |
| `||`   | 逻辑 or 运算符,一边为true 则为 true                        |
| `!`    | 逻辑 NOT 运算符,条件为true则为 false,条件为false 则为 true |

```go
var a = 5
var b = 4
fmt.Println((a==b)&&(a>=b)) // false
fmt.Println((a==b)||(a>=b)) // true
fmt.Println(!(a==b)) // true
```

+ 短路逻辑

  + 逻辑与运算符 : `&&`

    + 如果左边为 false 则右边代码不执行

      ```go
      func test() bool {
      	fmt.Println("执行test")
      	return true
      }
      func main()  {
      	var a = 10
      	if a < 9 && test() {
      		fmt.Println("执行代码")
      	}
      }
      // 无输出
      
      func test() bool {
      	fmt.Println("执行test")
      	return true
      }
      func main()  {
      	var a = 10
      	if a > 9 && test() {
      		fmt.Println("执行代码")
      	}
      }
      // 执行test
      // 执行代码
      ```

      

  + 逻辑或运算符 : `||`

    + 如果左边为 true 则右边代码不执行

      ```go
      func test() bool {
      	fmt.Println("执行test")
      	return true
      }
      func main()  {
      	var a = 10
      	if a < 9 || test() {
      		fmt.Println("执行代码")
      	}
      }
      // 执行test
      // 执行代码
      
      func test() bool {
      	fmt.Println("执行test")
      	return true
      }
      func main()  {
      	var a = 10
      	if a > 9 || test() {
      		fmt.Println("执行代码")
      	}
      }
      // 执行代码
      ```

#### 赋值运算符

| 运算符    | 描述               |
| --------- | ------------------ |
| `=`或`:=` | 将左边值赋值给右边 |
| `+=`      | 相加后再赋值       |
| `-=`      | 相减后再赋值       |
| `*=`      | 相乘后再赋值       |
| `/=`      | 相除后再赋值       |
| `%=`      | 取余后再赋值       |

```go
var a = 5
var b = 4
// a += b
// fmt.Println(a) // 9
// a -= b
// fmt.Println(a) // 1
// a *= b
// fmt.Println(a) // 20
// a /= b
// fmt.Println(a) // 1
// a %= b
// fmt.Println(a) // 1
```

#### 位运算符(了解)

| 运算符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| `&`    | 参与运算的两数相对应的二进位相与 (两位都为 1才为 1)          |
| `|`    | 参与运算的两数相对应的二进位相或 (两位有一个为 1就为 1)      |
| `^`    | 参与运算的两数相对应的二进位异或 (两位不同就为 1)            |
| `<<`   | 左移 n 为就是乘以 2 的 n 次方。<br>`a<<b` : 把 a 的各二进位全部左移 b 位,高位丢弃,低位补0 |
| `<<`   | 右移 n 为就是除以 2 的 n 次方。<br/>`a>>b` : 把 a 的各二进位全部右移 b 位 |

```go
a := 5  // 101
b := 2  // 010
fmt.Println(a>>1) // 2
fmt.Println(b>>2) // 0
fmt.Println(b<<2) // 8
```

