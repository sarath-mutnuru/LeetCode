# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def get_sum(node,p_sum):
            if not node:
                return False
            if not(node.left or node.right):
                return p_sum + node.val == sum
            p_sum += node.val
            return get_sum(node.left, p_sum) or get_sum(node.right, p_sum)
        
        return get_sum(root, 0)