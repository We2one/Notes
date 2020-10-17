```yaml
   Author: Gentleman.Hu
   Create Time: 2020-10-17 15:01:32
   Modified by: Gentleman.Hu
   Modified time: 2020-10-17 16:43:20
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description: Leetcode of concurrency,Pirnt zero Even odd
 ```

## Print Zero Even Odd

> [source](https://leetcode.com/problems/print-zero-even-odd/)

- Problem

Suppose you are given the following code:

```java
class ZeroEvenOdd{
	public ZeroEvenOdd(int n){...} // 

	public void zero(printNumber){}// only output 0's
	public void even(printNumber){}// only output even numbers
	public void odd(printNumber){} // only output odd numbers
}
```

The same instance of `ZeroEvenOdd` will be passed to three different threads:

1. Thread A will call `zero()` which should only output 0's.
2. Thread B will call `zero()` which should only output even numbers.
3. Thread C will call `zero()` which should only output odd numbers.

Each of the threads is given a `printNumber` method to output an integer. Modify the given program to output the `010203040506...`where the length of the series must be `2n`.

- Example

```yaml
Input: n = 2
Output: "0102"
```

```yaml
Input: n = 5
Output: "0102030405"
```

## Solution

### Java

- 1. 
