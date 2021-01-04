#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: stack_ to_queue
@time: 2020/12/23 18:58
@IDE: PyCharm
@desc: 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""


class Solution:
	def __init__(self):
		# 队列 先进先出 栈 先进后出
		# 两个栈 组成一个队列 一个栈进一个栈出
		# stack1 存储数据 进
		self.stack1 = []
		# stack2 弹出数据 出
		self.stack2 = []

	def push(self, node):
		# 将需要传入的 node 传入 stack1 内
		# node = [1, 2, 3, 4, 5]
		# stack1 = [1, 2, 3, 4, 5]
		self.stack1.append(node)

	def pop(self):
		# 当 stack2 为空 stack1 不为空的时候，将 栈中的数据 倒序传出
		# stack1.pop() : [5, 4, 3, 2, 1]
		# stack2 [5, 4, 3, 2, 1]
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		# 如果 stack2 不为空 弹出 stack2 的最后一个值
		# stack2.pop()    [1, 2, 3, 4, 5]
		return self.stack2.pop()


s = Solution()
s.push([1, 3, 2, 9, 7])
print(s.pop())