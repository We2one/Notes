//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: MoreThanHalfNum_Solution
@time: 2020/12/25 9:44
@IDE: GoLand
@desc: 数组中出现次数超过一半的是数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
*/

package main

import "fmt"

/*
 *
 * @param numbers int整型一维数组
 * @return int整型
*/

// 方法一
func MoreThanHalfNum_Solution( numbers []int ) int {
	if numbers == nil{
		return 0
	}
	var dic =  make(map[int]int)
	harf_len := len(numbers) / 2
	for _, v := range numbers {

		if _, ok := dic[v]; ok == false{
			dic[v] = 1
		}else {
			dic[v] += 1
		}
		if dic[v] > harf_len{
			return v
		}
	}
	return 0
}

// 方法二
func MoreThanHalfNum_Solution1( numbers []int ) int {
	num, num_count := 0, 0
	for _, v := range numbers {
		if num_count == 0{
			num = v
			num_count += 1
		}else {
			if v == num {
				num_count += 1
			}else {
				num_count -= 1
			}
		}
	}
	if num_count != 0 {
		num_count = 0
		for _, v := range numbers {
			if v == num {
				num_count += 1
			}
		}
		if num_count > len(numbers) / 2 {
			return num
		}
	}
	return 0
}

func main() {
	arr := []int{1, 2, 3, 2, 2, 2, 5, 4, 2}
	//fmt.Println(MoreThanHalfNum_Solution(arr))
	fmt.Println(MoreThanHalfNum_Solution1(arr))
}