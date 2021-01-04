"""
面试题39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
限制：
1 <= 数组长度 <= 50000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n_dict = {}
        for num in nums:
            if num in n_dict:
                n_dict[num] += 1
            else:
                n_dict[num] = 1
        sort_value = sorted(n_dict.items(), key=lambda v: v[1])
        if sort_value[-1][-1] > len(nums)/2:
            return int(sort_value[-1][0])
        # 使用 Counter 计算
        # from collections import Counter
        # if Counter(nums).most_common(1)[0][1] > len(nums)/2:
        #     return Counter(nums).most_common(1)[0][0]
        # 不允许负值
        # import numpy as np
        # max_count = np.bincount(nums)
        # max_num = np.argmax(max_count)
        # if max_count[max_num] > len(nums)/2:
        #     return int(max_num)

