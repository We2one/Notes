"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 方法一、循环计算
        for i in range(1, len(digits)+1):  # [1, 9]  -> [1, 0] -> [2, 0]
            if digits[-i] != 9:  # i=2
                digits[-i] += 1  # [2, 0]
                return digits
            digits[-i] = 0  # [1,0]
        digits.insert(0, 1)
        return digits

        # 方法二、转字符串做加法
        # str_list = int("".join(str(i) for i in digits))
        # str_list += 1
        # list_str = [int(x) for x in str(str_list)]
        # return list_str