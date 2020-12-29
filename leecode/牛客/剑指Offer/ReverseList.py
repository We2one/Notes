#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: ReverseList
@time: 2020/12/29 20:04
@IDE: PyCharm
@desc: 反转链表
输入一个链表，反转链表后，输出新链表的表头
输入
{1,2,3}
返回值
{3,2,1}
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None
        root = None
        # 将 pHead 输出，最后一个就是 root 的值
        while pHead:
            pHead.next, root, pHead = root, pHead, pHead.next
        return root


# 方法二、递归到最后将数据输出到 cur
class Solution1:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        cur = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return cur


arr = ListNode(1)
arr.next = ListNode(2)
arr.next.next = ListNode(3)

# s = Solution()
s = Solution1()
print(s.ReverseList(arr))
