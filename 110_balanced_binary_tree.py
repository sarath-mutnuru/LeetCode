# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        heights ={}
        def get_heights(node, heights):
            if not node:
                return 0
            if node in heights:
                return heights[node]
            
            h_left = get_heights(node.left, heights)
            h_right = get_heights(node.right, heights)
            if node.left:
                heights[node.left] = h_left
            if node.right:
                heights[node.right] = h_right
            res = max(h_left, h_right) + 1
            heights[node] = res
            return res
        ans = get_heights(root, heights)
        
        for node in heights:
            if abs(heights.get(node.left, 0) - heights.get(node.right, 0)) not in [0, 1]:
                return False
        return True