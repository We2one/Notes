#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: python_study
@file: Rotating_min_num
@time: 2020/12/23 19:36
@IDE: PyCharm
@desc: 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


# 快速排序
class Solution5:
    def partition(self, arr, left, right):
        tmp = arr[left]
        while left < right:
            while arr[right] >= tmp and left < right:
                right -= 1
            arr[left] = arr[right]
            # print(arr, 'right')
            while arr[left] <= tmp and left < right:
                left += 1
            arr[right] = arr[left]
            # print(arr, 'left')
        arr[left] = tmp
        return left

    def quick_sort(self, arr, left, right):
        if left < right:  # 至少两个元素
            mid = self.partition(arr, left, right)
            self.quick_sort(arr, left, mid - 1)
            self.quick_sort(arr, mid + 1, right)

    def minNumberInRotateArray(self, rotateArray):
        self.quick_sort(rotateArray, 0, len(rotateArray)-1)
        return rotateArray


# 二分法
class Solution4:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (right + left) // 2
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left += 1
        return rotateArray[right]


# 选择排序 ---- 超时
class Solution3:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        for i in range(len(rotateArray) - 1):
            min_loc = i  # 最小值索引
            for j in range(i + 1, len(rotateArray)):
                if rotateArray[j] < rotateArray[min_loc]:
                    min_loc = j  # 找到最小值并赋值其索引为 min_loc
            # 将 i 值 与 最小值进行互换
            rotateArray[i], rotateArray[min_loc] = rotateArray[min_loc], rotateArray[i]
        return rotateArray[0]
        # 选择排序
        # arr_new = []
        # for i in range(len(rotateArray)):
        #     min_num = min(rotateArray)
        #     arr_new.append(min_num)
        #     rotateArray.remove(min_num)
        # return arr_new[0]


# 插入排序 ---- 超时
class Solution2:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        for i in range(1, len(rotateArray)):
            new_arr = rotateArray[i]
            j = i - 1
            while rotateArray[j] > new_arr and j >= 0:
                rotateArray[j+1] = rotateArray[j]
                j -= 1
            rotateArray[j+1] = new_arr
        return rotateArray[0]


# 冒泡排序 ---- 超时
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        for i in range(len(rotateArray)):
            for j in range(len(rotateArray) - i - 1):
                if rotateArray[j] > rotateArray[j + 1]:
                    rotateArray[j + 1], rotateArray[j] = rotateArray[j], rotateArray[j + 1]
        return rotateArray[0]


# 直接使用 sort 排序
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        rotateArray.sort()
        return rotateArray[0]


# s = Solution()
# s = Solution1()
# s = Solution2()
# s = Solution3()
# s = Solution4()
s = Solution5()
print(s.minNumberInRotateArray([4, 5, 1, 2, 3]))
