//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: jumpFloorII
@time: 2020/12/24 11:08
@IDE: GoLand
@desc: 变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
*/

package main

import "fmt"

// 数学函数
func jumpFloorII( number int ) int {
	// write code here
	if number == 1{
		return 1
	}
	 return 2 << (number - 2)
}

// 贪心算法
func jumpFloorII1( number int ) int {
	// write code here
	arr1, arr2 := 1, 2
	if number == 1{
		return arr1
	}
	for i := 0; i < number - 2; i ++ {
		arr2 = arr1 + arr2 + 1
		arr1 = arr2 - 1
	}
	return arr2
}

func main() {
	//fmt.Println(jumpFloorII(1))
	fmt.Println(jumpFloorII(4))
}