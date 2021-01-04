package main

import "fmt"

// 两个变量存储
func Fibo(n int) int {
	if n == 0 || n == 1{
		return n
	}
	num1, num2, nSum := 0, 1, 0
	for i := 1; i < n; i ++ {
		nSum = num1 + num2
		num1 = num2
		num2 = nSum
	}
	return nSum
}

// 列表保存
func Fibo2(n int) int {
	if n == 0 || n == 1{
		return n
	}
	var nArr []int
	nArr = append(nArr, 0, 1, 1)
	for len(nArr) <= n {
		nArr = append(nArr, nArr[len(nArr)-1]+nArr[len(nArr)-2])
	}
	return nArr[n]
}

// 递归
func Fibo3(n int) int {
	if n == 0 || n == 1{
		return n
	}
	return Fibo3(n-1) + Fibo3(n-2)
}

func main() {
	//fmt.Println(Fibo(4))
	//fmt.Println(Fibo2(4))
	fmt.Println(Fibo3(4))
}