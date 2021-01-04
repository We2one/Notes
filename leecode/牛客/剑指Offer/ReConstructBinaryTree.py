#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: ReConstructBinaryTree
@time: 2020/12/29 9:02
@IDE: PyCharm
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
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        head_node = TreeNode(pre[0])
        tin_head_ind = tin.index(head_node.val)
        # 判断左右子树是否存在
        # 如果二叉树每一个子树的 根节点 不在中序遍历的第一位，说明存在 根节点的左子树
        if tin_head_ind != 0:
            # 根节点的 左子树 为 前序遍历的 前 1: tin_head_ind 位，中序遍历的 前 tin_head_ind 位
            head_node.left = self.reConstructBinaryTree(pre[1:tin_head_ind+1], tin[:tin_head_ind])
        # 如果二叉树 的中序遍历 根节点 的 下标不是 中序遍历最后一个下标，证明存在右子树
        if tin_head_ind != len(tin)-1:
            # 前序遍历 代表 二叉树 右子树 的部分在 中序遍历 根节点 的下标之后 tin_head_ind+1: ， 中序遍历的 根节点之后 不包括根节点 tin_head_ind+1:
            head_node.right = self.reConstructBinaryTree(pre[tin_head_ind+1:], tin[tin_head_ind+1:])
        return head_node


# 前序遍历结果
preorder = [1, 2, 3, 4, 5, 6, 7]
# 中序遍历
middle_order = [3, 2, 4, 1, 6, 5, 7]
s = Solution()
print(s.reConstructBinaryTree(pre=preorder, tin=middle_order))
