#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: NumberOf1
@time: 2020/12/29 10:48
@IDE: PyCharm
@desc: 二进制中 1 的个数
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
输入
10
返回值
2
"""


class Solution:
    def NumberOf1(self, n):
        if n >= 0:
            n = bin(n)[2:]
            return n.count("1")
        else:
            n = bin(0xFFFFFFFF & n)[2:]
            return n.count("1")


s = Solution()
print(s.NumberOf1(-2147483648))
