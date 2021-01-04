#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: JumpFloor
@time: 2020/12/29 10:09
@IDE: PyCharm
@desc: 跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果
1 -> 1
2 -> 2
3 -> 3 = 1 + 2
4 -> 5 = 3 + 2
5 -> 8 = 5 + 3
输入
4
返回值
5
"""


# 方法一、用一个列表保存每级台阶 跳跃次数
class Solution:
    def jumpFloor(self, number):
        arr = [1, 2]
        if number in arr:
            return number
        for _ in range(number-2):
            arr.append(arr[-1]+arr[-2])
        return arr[-1]


# 方法二、使用 a, b 保存前两次跳跃所用次数
class Solution1:
    def jumpFloor(self, number):
        a, b = 1, 2
        if number == 1 or number == 2:
            return number
        for _ in range(number-2):
            a, b = b, a+b
        return b


# s = Solution()
s = Solution1()
print(s.jumpFloor(5))
