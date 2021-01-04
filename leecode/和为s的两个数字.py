"""
面试题57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 转化成集合
        nus = set(nums)
        for i in nus:
            reduce = target - i
            if reduce in nus:
                return [i, reduce]
        # i+j<target i -->
        # i+j=target [i.j]
        # i+j>target j-=1 直到 i+j<target / i+j=target双指针
        i, j = 0, len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum == target:
                return [nums[i], nums[j]]
            else:
                j -= 1
        # 递增排序，去除比 target 大的数，形成新数组,会超时
        # for index, num in enumerate(nums):
        #     if num >= target:
        #         new_nums = nums[:index]
        #         for n_num in new_nums:
        #             reduce = target - n_num
        #             if reduce in new_nums:
        #                 return [n_num, reduce]
        #     else:
        #         for n_num in nums:
        #             reduce = target - n_num
        #             if reduce in nums:
        #                 return [n_num, reduce]
        # 简单计算的话会出现超时
        # for num in nums:
        #     reduce = target - num
        #     if reduce in nums:
        #         return [num, reduce]