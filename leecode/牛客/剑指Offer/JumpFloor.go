//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: JumpFloor
@time: 2020/12/29 10:21
@IDE: GoLand
@desc: 跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果
1 -> 1
2 -> 2
3 -> 3 = 1 + 2
4 -> 5 = 3 + 2
5 -> 8 = 5 + 3
输入
4
返回值
5
*/

package main

import (
	"fmt"
)

// 方法一、使用 a, b 存储前两次跳跃所用次数
func jumpFloor( number int ) int {
	if number == 1 || number == 2 {
		return number
	}
	a, b := 1, 2
	for i := 0; i < number - 2; i ++ {
		a, b = b, a + b
	}
	return b
}

// 方法二、使用切片保存每次跳跃次数
func jumpFloor1( number int ) int {
	if number == 1 || number == 2 {
		return number
	}
	arr := []int{1, 2}
	for i := 0; i < number -2 ; i ++ {
		sum := arr[len(arr)-1] + arr[len(arr)-2]
		arr = append(arr, sum)
	}
	return arr[len(arr)-1]
}

func main() {
	num := 5
	fmt.Println(jumpFloor(num))
	fmt.Println(jumpFloor1(num))
}