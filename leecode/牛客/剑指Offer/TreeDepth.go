//package main

/*
@author: forgotten_liu
@projectName: Golang_study
@file: TreeDepth
@time: 2020/12/27 15:22
@IDE: GoLand
@desc: 二叉树的深度
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
示例1
输入
{1,2,3,4,5,#,6,#,#,7}
返回值
4
*/

package main


//type TreeNode struct {
//	Val int
//  	Left *TreeNode
//  	Right *TreeNode
//}


/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * @param pRoot TreeNode类
 * @return int整型
 */

func TreeDepth( pRoot *TreeNode ) int {
	if pRoot == nil{
		return 0
	}
	if TreeDepth(pRoot.Right)+1 > TreeDepth(pRoot.Left)+1{
		return TreeDepth(pRoot.Right)+1
	}else {
		return TreeDepth(pRoot.Left)+1
	}
}

func main() {
}
