//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: Rotating_min_num
@time: 2020/12/23 21:06
@IDE: GoLand
@desc: 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
*/

package main

import "fmt"

// 二分法
func minNumberInRotateArray( rotateArray []int ) int {
	left, right := 0, len(rotateArray) - 1
	for left < right{
		mid := (left + right) / 2
		if rotateArray[left] < rotateArray[right]{
			return rotateArray[left]
		}
		if rotateArray[left] < rotateArray[mid] {
			left = mid + 1
		}else if rotateArray[right] > rotateArray[mid]{
			right = mid
		}else {
			left += 1
		}
	}
	return rotateArray[left]
}

// 冒泡排序
func minNumberInRotateArray1( rotateArray []int ) int {
	if rotateArray == nil{
		return 0
	}
	for i, _ := range rotateArray {
		for j := 0; j < len(rotateArray) - i - 1; j ++ {
			if rotateArray[j] > rotateArray[j+1]{
				rotateArray[j+1], rotateArray[j] = rotateArray[j], rotateArray[j+1]
			}
		}
	}
	return rotateArray[0]
}

// 插入排序
func minNumberInRotateArray2( rotateArray []int ) int {
	if rotateArray == nil {
		return 0
	}
	// 方法三
	for i := 0; i < len(rotateArray) - 1; i ++ {
		minIndex := i
		for j := i + 1; j < len(rotateArray); j ++ {
			if rotateArray[minIndex] > rotateArray[j] {
				minIndex = j
			}
		}
		rotateArray[i], rotateArray[minIndex] = rotateArray[minIndex], rotateArray[i]
	}
	return rotateArray[0]
	// 方法二
	//for i := 1; i < len(rotateArray); i ++ {
	//	newArr := rotateArray[i]
	//	j := i - 1
	//	for j >= 0 && rotateArray[j] > newArr{
	//		rotateArray[j+1] = rotateArray[j]
	//		j -= 1
	//	}
	//	rotateArray[j+1] = newArr
	//}
	//return rotateArray[0]
	// 方法一
	//var j int = 0
	//for i := 1; i < len(rotateArray); i ++ {
	//	newArr := rotateArray[i]
	//	for j=i; j>0 && rotateArray[j-1] > newArr; j--{
	//		rotateArray[j] = rotateArray[j-1]
	//	}
	//	rotateArray[j] = newArr
	//}
	//return rotateArray[0]
}

// 选择排序
func minNumberInRotateArray3( rotateArray []int ) int {
	if rotateArray == nil {
		return 0
	}
	for i := 0; i < len(rotateArray) - 1; i ++ {
		minIndex := i
		for j := i + 1; j < len(rotateArray); j ++ {
			if rotateArray[j] < rotateArray[minIndex]{
				minIndex = j
			}
		}
		rotateArray[i], rotateArray[minIndex] = rotateArray[minIndex], rotateArray[i]
	}
	return rotateArray[0]
}

func main() {
	arr := []int{4, 5, 1, 2, 3}
	//fmt.Println(minNumberInRotateArray(arr))
	//fmt.Println(minNumberInRotateArray1(arr))
	//fmt.Println(minNumberInRotateArray2(arr))
	fmt.Println(minNumberInRotateArray3(arr))
}
