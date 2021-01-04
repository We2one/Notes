#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Balanced_Binary_Tree
@time: 2020/12/27 15:39
@IDE: PyCharm
@desc: 平衡二叉树
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
示例1
输入
{1,2,3,4,5,6,7}
返回值
true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getDepth(self, Root):
        if not Root:
            return True
        left = self.getDepth(Root.left)
        right = self.getDepth(Root.right)
        return max(left, right) + 1

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        # 求出左右子树的深度
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        if abs(left - right) > 1:
            return False
        # 递归判断每个子树是否是 平衡二叉树
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
