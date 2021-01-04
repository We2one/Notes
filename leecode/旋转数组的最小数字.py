"""
面试题11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 方法三 二分法
        i, j = 0, len(numbers) - 1
        while i < j:
            middle = (i + j) // 2
            if numbers[middle] < numbers[j]:
                j = middle
            elif numbers[middle] > numbers[j]:
                i = middle + 1
            else:
                j -= 1
        return numbers[i]
        # 方法二
        # numbers.sort()
        # return numbers[0]
        # 方法一
        # if len(numbers) == 1 or len(list(set(numbers))) == 1:  # 考虑长度为 1 的数组，或 去重后为 1 的数组
        #     return numbers[0]
        # for i in range(len(numbers)):
        #     if numbers[i] < numbers[i-1]:
        #         return numbers[i]
