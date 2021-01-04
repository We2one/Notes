#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: TreeDepth
@time: 2020/12/27 15:06
@IDE: PyCharm
@desc: 二叉树的深度
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
示例1
输入
{1,2,3,4,5,#,6,#,#,7}
返回值
4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一、返回左节点的节点深度与右节点的节点深度中的最大值
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left)+1, self.TreeDepth(pRoot.right)+1)


# 方法二
class Solution1:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        pArr, depth = [pRoot], 0
        while pArr:
            b = []
            # 在这里取出了 根节点，留下左节点作为左子树的根节点，右节点作为右子树的根节点，继续循环
            for node in pArr:
                if node.left:
                    b.append(node.left)
                if node.right:
                    b.append(node.right)
            pArr = b
            depth += 1
        return depth



s = Solution()
arr = TreeNode(x=[])
s.TreeDepth(arr)