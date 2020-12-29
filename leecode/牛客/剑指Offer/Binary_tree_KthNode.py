#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Binary_tree_KthNode
@time: 2020/12/28 9:49
@IDE: PyCharm
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
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一
class Solution:
    # 返回对应节点TreeNode
    index = 0

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        left = self.KthNode(pRoot.left, k)
        self.index += 1
        if self.index == k:
            return pRoot
        right = self.KthNode(pRoot.right, k)
        if left:
            return left
        elif right:
            return right


# 方法二
class Solution1:
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        self.arr = []
        if not pRoot:
            return None
        self.tree_to_list(pRoot)
        if 0 < k <= len(self.arr):
            return self.arr[k-1]

    # 中序遍历 得到的列表是有序的
    def tree_to_list(self, Root):
        if not Root:
            return None
        self.tree_to_list(Root.left)
        self.arr.append(Root)
        self.tree_to_list(Root.right)


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(7)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(8)
s = Solution1()
print(s.KthNode(tree, 1))