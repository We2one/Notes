#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: jumpFloorII
@time: 2020/12/24 11:03
@IDE: PyCharm
@desc: 变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
"""


# 贪心算法
class Solution2:
    def jumpFloorII(self, number):
        arr1, arr2 = 1, 2
        if number == 1:
            return arr1
        for i in range(number-2):
            arr2 = arr1 + arr2 + 1
            arr1 = arr2 - 1
        return arr2


# 位运算
class Solution1:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        return 2 << (number - 2)


# 数学函数
class Solution:
    def jumpFloorII(self, number):
        return 2 ** (number - 1)


# s = Solution()
# s = Solution1()
s = Solution2()
print(s.jumpFloorII(4))