#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: FindGreatestSumOfSubArray
@time: 2020/12/25 11:21
@IDE: PyCharm
@desc: 连续数组最大和
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).
输入
[1,-2,3,10,-4,7,2,-5]
返回值
18
说明
输入的数组为{1,-2,3,10,—4,7,2,一5}，和最大的子数组为{3,10,一4,7,2}，因此输出为该子数组的和 18。
"""


# 方法一 : 遍历所有和
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        max_sum = float('-Inf')
        for i in range(len(array)):
            k = 0
            for j in range(i, len(array)):
                k += array[j]
                max_sum = max(max_sum, k)
        return max_sum


# 方法二 :
class Solution1:
    def FindGreatestSumOfSubArray(self, array):
        sum_num = 0
        res = float("-inf")
        for num in array:
            if sum_num > 0:
                sum_num += num
            else:
                sum_num = num
            res = max(sum_num, res)

        return res


# s = Solution()
s = Solution1()
arr = [1, -2, 3, 10, -4, 7, 2, -5]
# arr = [-1, -2, -3, -4, 5]
print(s.FindGreatestSumOfSubArray(arr))
