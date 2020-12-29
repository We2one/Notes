#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: MoreThanHalfNum_Solution
@time: 2020/12/25 9:31
@IDE: PyCharm
@desc: 数组中出现次数超过一半的是数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


# 内置函数法
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        for i in set(numbers):
            if numbers.count(i) > len(numbers) // 2:
                return i


# 遍历添加字典计数
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        dic, lenght = {}, len(numbers)//2
        for num in numbers:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] > lenght:
                return num
        return 0


# s = Solution()
s = Solution1()
arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(s.MoreThanHalfNum_Solution(arr))
