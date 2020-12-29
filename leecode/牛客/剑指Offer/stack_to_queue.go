//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: stack_to_queue
@time: 2020/12/23 19:23
@IDE: GoLand
@desc:
*/

package main

import "fmt"

var stack1 []int
var stack2 []int

func Push(node int) {
	// 将 node 的数据传入 栈 stack1
	stack1 = append(stack1, node)
}

func Pop() int{
	if len(stack2) == 0 {
		// 将 stack1 的数据 传入 栈 stack2
		stack2 = append(stack2, stack1...)
		// 将 stack1 置为空
		stack1 = []int{}
	}
	// 将 stack2 中的 第一个数据 输出 存入 变量 res
	res := stack2[0]
	// 将 stack2 向后移一位
	stack2 = stack2[1:]
	// 返回 res
	return res
}

func main() {
	for i := 1; i < 10; i++ {
		Push(i)
	}
	fmt.Println(Pop())
	fmt.Println(Pop())
	fmt.Println(Pop())
	fmt.Println(Pop())
	fmt.Println(Pop())
	fmt.Println(Pop())

}