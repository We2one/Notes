//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: Mirror_binary_tree
@time: 2020/12/25 9:23
@IDE: GoLand
@desc: 操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
*/

package main
//import "nc_tools"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}


/**
 *
 * @param pRoot TreeNode类
 * @return TreeNode类
 */

// 方法一
func Mirror( pRoot *TreeNode ) *TreeNode {
	if pRoot == nil{
		return nil
	}
	pRoot.Left, pRoot.Right = Mirror(pRoot.Right), Mirror(pRoot.Left)
	return pRoot
}

// 方法二
func Mirror1( pRoot *TreeNode ) *TreeNode {
	if pRoot == nil{
		return nil
	}
	left, right := pRoot.Left, pRoot.Right
	pRoot.Left, pRoot.Right = right, left
	Mirror(pRoot.Left)
	Mirror(pRoot.Right)
	return pRoot
}