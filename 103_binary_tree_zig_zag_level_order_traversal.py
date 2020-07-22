# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        curr = [root]
        ans = []
        move_left = 1
        while curr:
            ans.append([n.val for n in curr[::move_left]])
            move_left = -1*move_left
            p = []
            for n in curr:
                if n.left:
                    p.append(n.left)
                if n.right:
                    p.append(n.right)
            curr = p
        return ans
            
                    
                    
        