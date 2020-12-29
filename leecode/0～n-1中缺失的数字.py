"""
面试题53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，
并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
示例 1:
输入: [0,1,3]
输出: 2
示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
限制：
1 <= 数组长度 <= 10000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 数学法
        nums.sort()
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)
        # 二分法
        # i, j = 0, len(nums)-1
        # while i <= j:
        #     middle = (i + j) // 2
        #     if nums[middle] == middle:  # 缺失一定在右半部分
        #         i = middle + 1
        #     else:
        #         j = middle - 1
        # return i

        # 补集
        # complete_nums = []
        # for i in range(nums[-1]+1):
        #     complete_nums.append(i)
        # if complete_nums == nums:
        #     return nums[-1] + 1
        # else:
        #     return list(set(complete_nums) - set(nums))[0]
