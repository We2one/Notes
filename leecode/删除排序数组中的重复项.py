"""
删除排序数组中的重复项:
给定一个排序数组，你需要在 原地 删除重复出现的元素，
使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1)
额外空间的条件下完成。
[1,2,2,3,3]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        # 方法1、双指针
        # p, q = 0, 1
        # while len(nums) > q:
        #     if nums[p] == nums[q]:
        #         q += 1
        #     else:
        #         nums[p+1] = nums[q]
        #         p += 1
        #         q += 1
        # return len(nums[:p+1])
        # 方法2、遍历
        # for i in nums:
        #     num_count = nums.count(i)
        #     while num_count > 1:
        #         nums.remove(i)
        #         num_count -= 1
        # return nums
        # 方法3、逆序判断并输出
        for num_index in range(len(nums)-1, 0, -1):
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index)
        return nums


        # nus = sorted(list(set(nums)))
        # 	nums[i] = nus[i]
        # return len(nus)
        # i = 0
        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        #         nums = nums[:i+1]
        #     return i+1


s = Solution()
arr = [1, 1, 2, 3, 3, 4, 5, 6, 6]
print(s.removeDuplicates(arr))