# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
            # return x
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2**31 < x < 2 ** 31 - 1 else 0
        # if x == 0:
        #     return x
        # elif x > 0:
        #     x_list = [int(x) for x in str(x)]
        #     rx_list = map(str, list(reversed(x_list)))
        #     xr = int("".join(str(i) for i in rx_list))
        #     if xr > 2 ** 31 - 1:
        #         return 0
        #     return xr
        # elif x < 0:
        #     x = abs(x)
        #     x_list = [int(x) for x in str(x)]
        #     rx_list = map(str, list(reversed(x_list)))
        #     xr = -int("".join(str(i) for i in rx_list))
        #     if xr < -2 ** 31:
        #         return 0
        #     return xr

#         int("".join(str(i) for i in map(str, sorted([1,2,3], reverse=True))))
