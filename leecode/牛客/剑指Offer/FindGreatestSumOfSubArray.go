//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: FindGreatestSumOfSubArray
@time: 2020/12/25 14:30
@IDE: GoLand
@desc: 连续数组最大和
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).
输入
[1,-2,3,10,-4,7,2,-5]
返回值
18
说明
输入的数组为{1,-2,3,10,—4,7,2,一5}，和最大的子数组为{3,10,一4,7,2}，因此输出为该子数组的和 18。
*/

package main

import "fmt"

// 方法一、遍历
func FindGreatestSumOfSubArray( array []int ) int {
	if len(array) == 0 {
		return 0
	}
	max, sum := array[0], 0
	for i := 0; i < len(array); i ++ {
		if sum > 0{
			sum += array[i]
		}else {
			sum = array[i]
		}
		if sum > max {
			max = sum
		}
	}
	return max
}

func main() {
	arr := []int{1, -2, 3, 10, -4, 7, 2, -5}
	fmt.Println(FindGreatestSumOfSubArray(arr))
}
