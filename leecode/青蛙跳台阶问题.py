"""
面试题10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。
求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），
如计算初始结果为：1000000008，请返回 1。
示例 1：
输入：n = 2   0 -> 1 1 -> 1 2 -> 2 3-> 3 4 -> 5  .... f(n) = f(n-1) + f(n-2)
输出：2
示例 2：
输入：n = 7
输出：21
提示：
0 <= n <= 100
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numWays(self, n: int) -> int:
        # if n < 2:
        #     return 1
        # else:
        #     arr = [1 for _ in range(n+1)]  # 用 1 填充数组,填充的数组大小应该比台阶数加一以存放结果
        #     arr[1] = 1
        #     for i in range(2, n+1):
        #         arr[i] = arr[i-1] + arr[i-2]
        #     return arr[-1] % 1000000007
        arr = {}
        arr[0] = 1
        arr[1] = 1
        for i in range(2, n+1):  # 向后排一格空位
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n] % 1000000007

        # a, b = 1, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007
