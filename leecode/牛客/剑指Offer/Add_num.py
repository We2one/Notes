#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Add_num
@time: 2020/12/27 21:20
@IDE: PyCharm
@desc: 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


class Solution:
    def Add(self, num1, num2):
        # &、^代表的是位运算符
        # 按位与&: A&B表明A与B的二进制逐位与，有0为0，非0为1
        # 按位异或^: A^B表明A与B的二进制逐位异或，相同为0，不同为1.
        # ~: 操作符按位取反
        while num2:
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)


s = Solution()
print(s.Add(4, 9))