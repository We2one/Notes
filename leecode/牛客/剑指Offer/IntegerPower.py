#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: IntegerPower
@time: 2020/12/29 19:03
@IDE: PyCharm
@desc: 数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
输入
2,3
返回值
8.00000
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        return float(base ** exponent)


s = Solution()
print(s.Power(2, -3))