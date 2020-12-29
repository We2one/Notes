#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: RectCover
@time: 2020/12/29 10:34
@IDE: PyCharm
@desc: 矩形覆盖  ---> 等同于 青蛙跳台阶
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
输入
4
返回值
5
"""


# 方法一
class Solution:
    def rectCover(self, number):
        if number == 0 or number == 1 or number == 2:
            return number
        a, b = 1, 2
        for _ in range(number-2):
            a, b = b, a+b
        return b


# 方法二
class Solution1:
    def rectCover(self, number):
        arr = [0, 1, 2]
        if number in arr:
            return number
        for _ in range(number-2):
            arr.append(arr[-1] + arr[-2])
        return arr[-1]


# s = Solution()
s = Solution1()
print(s.rectCover(5))