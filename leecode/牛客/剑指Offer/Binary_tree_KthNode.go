//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: Binary_tree_KthNode
@time: 2020/12/28 13:49
@IDE: GoLand
@desc: 二叉树的第 n 个节点
给定一棵二叉搜索树，请找出其中的第k小的结点。
示例1
输入
{5,3,7,2,4,6,8},3
返回值
{4}
     5
  3    7
 2 4  6 8
*/

package main

import "fmt"

type TreeNode struct {
	Val int
  	Left *TreeNode
  	Right *TreeNode
}


/**
 *
 * @param pRoot TreeNode类
 * @param k int整型
 * @return TreeNode类
 */

// 由于返回值需要为 *TreeNode 类型 ,所以 无法使用 切片存入遍历值,需要用切片存入遍历节点
func KthNode( pRoot *TreeNode ,  k int ) *TreeNode {
	if pRoot == nil || k <= 0 {
		return nil
	}
	arr := dfs(pRoot)
	if len(arr) < k {
		return nil
	}
	return arr[k-1]
}

// 中序遍历树
func dfs(Root *TreeNode) (arr []*TreeNode) {
	if Root == nil {
		return nil
	}
	// 在 dfs(Root.Left) []*TreeNode 内开始存入 节点值
	arr = append(dfs(Root.Left), Root)
	arr = append(arr, dfs(Root.Right)...)
	return arr
}

func main() {
	leftLeft := TreeNode{
		Val: 2,
	}
	leftRight := TreeNode{
		Val: 4,
	}
	left := TreeNode{
		Val:   3,
		Left:  &leftLeft,
		Right: &leftRight,
	}
	rightLeft := TreeNode{
		Val: 6,
	}
	rightRight := TreeNode{
		Val: 8,
	}
	right := TreeNode{
		Val: 7,
		Left: &rightLeft,
		Right: &rightRight,
	}
	tree := TreeNode{
		Val: 5,
		Left: &left,
		Right: &right,
	}
	fmt.Println(*KthNode(&tree, 3))
}