# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSame(r1, r2):
            if not r1 and not r2:
                return True
            if bool(r1) ^ bool(r2):
                return False
            if r1.val != r2.val:
                return False
            if bool(r1.left) ^ bool(r2.left) or bool(r1.right) ^ bool(r2.right):
                return False
            l = True
            if r1.left and r2.left:
                l = isSame(r1.left, r2.left)
            r = True
            if r2.right and r2.right:
                r = isSame(r1.right, r2.right)
            return l and r
        return isSame(p,q)