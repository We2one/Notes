"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            # r_x 为求余的余数
            r_x = 0
            while x > r_x:
                r_x = r_x * 10 + x % 10
                x = x // 10
            if x == r_x or r_x // 10 == x:
                return True
            else:
                return False

        # """
        #         只反转后面一半的数字!!(节省一半的时间)
        #         """
        # if x < 0 or (x != 0 and x % 10 == 0):
        #     return False
        # elif x == 0:
        #     return True
        # else:
        #     reverse_x = 0
        #     while x > reverse_x:
        #         remainder = x % 10
        #         reverse_x = reverse_x * 10 + remainder
        #         x = x // 10
        #     # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
        #     if reverse_x == x or reverse_x // 10 == x:
        #         return True
        #     else:
        #         return False
        # str_x = str(x)
        # if str_x[::-1] == str_x:
        #     return True
        # else:
        #     return False