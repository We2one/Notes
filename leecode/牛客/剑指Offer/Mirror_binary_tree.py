#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Mirror_binary_tree
@time: 2020/12/25 8:58
@IDE: PyCharm
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
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @param pRoot TreeNode类
# @return void


# 方法一
class Solution:
    def Mirror(self, pRoot):
        if not pRoot:
            return pRoot
        pRoot.left, pRoot.right = self.Mirror(pRoot.right), self.Mirror(pRoot.left)
        return pRoot


# 方法二
class Solution1:
    def Mirror(self, pRoot):
        if not pRoot:
            return None
        stack = [pRoot]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return pRoot


# 方法三
class Solution2:
    def Mirror(self, pRoot):
        if not pRoot:
            return None
        left, right = pRoot.left, pRoot.right
        pRoot.left, pRoot.right = right, left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot