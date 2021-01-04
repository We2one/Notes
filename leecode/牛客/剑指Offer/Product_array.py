#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Product_array
@time: 2020/12/28 8:55
@IDE: PyCharm
@desc: 构造乘积数组
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
输入
[1,2,3,4,5]
返回值
[120,60,40,30,24]
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
B[0] = A[1] * A[2] * ... * A[n-1]
B[1] = A[0]*A[2]*...*A[n-1]
B[2] = A[0]*A[1]*A[3]*...*A[n-1]
B[3] = A[0]*A[1]*A[2]*A[4]
B[n-1] = A[0] * A[1] * ... * A[n-2]
"""


# 方法一
class Solution:
    def multiply(self, A):
        n, B = len(A), []
        if n == 0:
            return B
        for i, v in enumerate(A):
            arr = A[:i]+A[i+1:]
            B.append(self.product(arr))
        return B

    def product(self, arr):
        ride = 1
        for i in arr:
            ride *= i
        return ride


# 方法二
class Solution1:
    def multiply(self, A):
        n, B = len(A), []
        for i in range(n):
            temp = 1
            for j in range(n):
                if i != j:
                    temp *= A[j]
            B.append(temp)
        return B


# s = Solution()
s = Solution1()
arr = [1, 2, 3, 4, 5]
print(s.multiply(arr))
