"""
面试题 05.07. 配对交换
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。
示例1:
 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:
 输入：num = 3
 输出：3
提示:
num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/exchange-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        b_num = list(bin(num))[2:]
        # b_num = "{0:b}".format(num)
        sq = 2
        if len(b_num) % 2 != 0:
            b_num.insert(0, '0')
        i, j = len(b_num) - 1, len(b_num) - 2
        while i >= 0 and j >= 0:
            b_num[i], b_num[j] = b_num[j], b_num[i]
            i -= sq
            j -= sq
        return int(''.join(x for x in b_num), 2)
