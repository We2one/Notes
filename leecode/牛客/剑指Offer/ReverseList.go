//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: ReverseList
@time: 2020/12/29 20:33
@IDE: GoLand
@desc: 反转链表
输入一个链表，反转链表后，输出新链表的表头
输入
{1,2,3}
返回值
{3,2,1}
*/

package main

import "fmt"

type ListNode struct{
	Val int
	Next *ListNode
}


/**
 *
 * @param pHead ListNode类
 * @return ListNode类
 */

// 方法一、递归
func ReverseList( pHead *ListNode ) *ListNode {
	if pHead == nil || pHead.Next == nil {
		return pHead
	}
	cur := ReverseList(pHead.Next)
	pHead.Next.Next = pHead
	pHead.Next = nil
	return cur
}

// 方法二
func ReverseList1( pHead *ListNode ) *ListNode {
	//if pHead == nil {
	//	return nil
	//}
	var root *ListNode
	for pHead != nil {
		root, pHead.Next, pHead = pHead, root, pHead.Next
	}
	return root
}

func main() {
	list := &ListNode{
		Val: 1,
	}
	list.Next = &ListNode{
		Val: 2,
	}
	list.Next.Next = &ListNode{
		Val: 3,
	}
	fmt.Println(*ReverseList(list))
	fmt.Println(*ReverseList1(list))
}