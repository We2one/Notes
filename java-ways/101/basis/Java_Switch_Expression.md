```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-19 20:48:31
   Modified by: Gentleman.Hu
   Modified time: 2020-10-19 20:58:13
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Java Switch表达式新特性
 ```

## Java Switch Expression

> [source](http://tutorials.jenkov.com/java/switch.html)

## Multiple case statements for same operation

```java
char key = '\t';

switch (key) {
	case ' ':
	case '\t' System.out.println("white space char");
		break;
	default:
		break;
}
```

上述如果是空格的话,两个都会执行

## Multiple Values Pre Case Statement

> Java 13特性,同个case,多个条件

```java
char key = '\t';

switch (key) {
	case ' ','\t':
		System.out.println("white space char");
		break;

	default:
		break;
}

```

## Switch Expressions above Java 12

```java
int  digitInDecimal = 12;
char digitInHex     =
    switch(digitInDecimal){
        case  0 -> '0';
        case  1 -> '1';
        case  2 -> '2';
        case  3 -> '3';
        case  4 -> '4';
        case  5 -> '5';
        case  6 -> '6';
        case  7 -> '7';
        case  8 -> '8';
        case  9 -> '9';
        case 10 -> 'A';
        case 11 -> 'B';
        case 12 -> 'C';
        case 13 -> 'D';
        case 14 -> 'E';
        case 15 -> 'F';

        default -> '?';
    };

System.out.println(digitInHex);
```

语法糖,用lambda箭头,可省略break,或者充当return,编译器根据上下文自动推断.

```java
public char toHexDigit(int digitInDecimal) {

    return
    switch(digitInDecimal){
        case  0 -> '0';
        case  1 -> '1';
        case  2 -> '2';
        case  3 -> '3';
        case  4 -> '4';
        case  5 -> '5';
        case  6 -> '6';
        case  7 -> '7';
        case  8 -> '8';
        case  9 -> '9';
        case 10 -> 'A';
        case 11 -> 'B';
        case 12 -> 'C';
        case 13 -> 'D';
        case 14 -> 'E';
        case 15 -> 'F';

        default -> '?';
    };

}
```

直接作为return结果

```java
String token = "123";

int tokenType = switch(token) {
    case "123" -> 0;
    case "abc" -> 1;
    default -> -1;
};
```

同样也能传参


## Java `yield` keyword

```java
String token = "123";

int tokenType = switch(token) {
    case "123" : yield 0;
    case "abc" : yield 1;
    default : yield -1;
};
```

- switch Expression Use Cases
  - The Java switch expressions are useful in use cases where you need to obtain a value based on another value. For instance, when converting between number values and characters, as shown in the example above.

  - Java switch expressions are also useful when parsing characters into values, or String tokens into integer token types. In general, whenever you need to resolve one value to another.
