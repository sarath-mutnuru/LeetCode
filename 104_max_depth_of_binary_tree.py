# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def maxDepthUtil(node, heights):
            if not node:
                return 0
            if node in heights:
                return heights[node]
            h_left = maxDepthUtil(node.left, heights)
            h_right = maxDepthUtil(node.right, heights)
            if node.left:
                heights[node.left] = h_left
            if node.right:
                heights[node.right] = h_right
            res = max(h_left, h_right) + 1
            heights[node] = res
            return res
        heights = {}
        ans = maxDepthUtil(root, heights)
        return ans
    