# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def get_sum_util(node):
            if not node:
                return [(0, 0)]
            if not(node.left or node.right):
                return [(node.val, 1),]
            
            left_arr = get_sum_util(node.left) if node.left else []
            right_arr = get_sum_util(node.right) if node.right else []
            arr = left_arr + right_arr
            ans = [(num + p10*10*node.val, p10*10) for num, p10 in arr]
            return ans
        res = get_sum_util(root)
        return sum(r[0] for r in res)