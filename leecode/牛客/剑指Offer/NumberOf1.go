//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: NumberOf1
@time: 2020/12/29 11:15
@IDE: GoLand
@desc: 二进制中 1 的个数
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
输入
10
返回值
2
*/

package main

import "fmt"

func NumberOf1( n int ) int {
	print(n)
	n1 := int32(n)
	print(n1)
	cnt := 0
	// 两位同时为“1”，结果才为“1”，否则为0
	for n1!=0{
		cnt++
		n1 &= n1-1
	}
	return cnt
}

func main() {
	fmt.Println(NumberOf1(-2147483648))
}