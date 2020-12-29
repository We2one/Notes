"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def findn(root):
            if root == None:
                return []
            return findn(root.left) + [root.val] + findn(root.right)  # 将二叉树通过函数构建成数组
        arr = findn(root)
        i, j = 0 , len(arr) - 1
        while i < j:    # 二分法查找数组
            s = arr[i] + arr[j]
            if s == k:
                return True
            elif s > k:
                j -= 1
            else:
                i += 1
        return False