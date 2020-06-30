# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        s = []
        res = []
        if not root:
            return
        s.append(root)
        while s:
            node = s.pop()
            if node:
                res.append(node.val)
                s.append(node.right)
                s.append(node.left)
        return res