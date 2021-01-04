//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: ReConstructBinaryTree
@time: 2020/12/29 9:41
@IDE: GoLand
@desc: 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
输入
前序遍历: [1,2,3,4,5,6,7]
中序遍历: [3,2,4,1,6,5,7]
返回值
{1,2,5,3,4,6,7}
        1
    2       5
 3     4 6     7
规律 : 前序遍历第一个为 根节点, 前序遍历第二个节点为左节点
      中序遍历第一个为左子树的最左边的叶子结点
*/

package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}


/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pre int整型一维数组
 * @param vin int整型一维数组
 * @return TreeNode类
 */
func reConstructBinaryTree( pre []int ,  vin []int ) *TreeNode {
	if pre == nil || vin == nil{
		return nil
	}
	headNode := TreeNode{
		Val: pre[0],
	}
	headIndex := 0
	for i, v := range vin {
		if headNode.Val == v {
			headIndex = i
		}
	}
	// 判断左右子树是否存在
	if headIndex != 0 {
		headNode.Left = reConstructBinaryTree(pre[1:headIndex+1], vin[:headIndex])
	}
	if headIndex != len(vin) - 1 {
		headNode.Right = reConstructBinaryTree(pre[headIndex+1:], vin[headIndex+1:])
	}
	return &headNode
}

func main() {
	// 前序遍历结果
	preorder := []int{1, 2, 3, 4, 5, 6, 7}
	// 中序遍历
	middle_order := []int{3, 2, 4, 1, 6, 5, 7}
	fmt.Println(*reConstructBinaryTree(preorder, middle_order))
}