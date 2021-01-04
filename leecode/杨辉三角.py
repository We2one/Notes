"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
通过次数78,549提交次数118,
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         triangle = [[1]]
#         if numRows == 0:
#             return []
#         elif numRows == 1:
#             return triangle
#         else:
#             r = [1]
#             for i in range(1, numRows):
#                 r.insert(0, 0)
#                 for j in range(i):
#                     r[j] = r[j] + r[j+1]
#                 triangle.append(r)
#                 return triangle
#         if numRows == 0:
#             return []
#         else:
#             triangle = [[1]]
#             while len(triangle) < numRows:
#                 new_triangle = [a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])]
#                 triangle.append(new_triangle)
#             return triangle
"""
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 3
输出: [1,3,3,1]
"""
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         triangle = [[1]]
#         if rowIndex == 0:
#             return triangle
#         else:
#             while len(triangle) < 35:
#                 new_triangle = [a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])]
#                 triangle.append(new_triangle)
#             return triangle[rowIndex + 1]
r = [1]
for i in range(1, 3 + 1):
    r.insert(0, 0)
    # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
    for j in range(i):
        r[j] = r[j] + r[j + 1]
print(r)

