//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: Add_num
@time: 2020/12/27 15:45
@IDE: GoLand
@desc: 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
*/

package main

import "fmt"

func Add( num1 int ,  num2 int ) int {
	// write code here
	for num2 != 0 {
		num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF
	}
	if num1 <= 0x7FFFFFFF {
		return num1
	}else {
		// Golang 中按位取反 为 ^
		return ^(num1 ^ 0xFFFFFFFF)
	}
}

func main() {
	fmt.Println(Add(1, -2))
}