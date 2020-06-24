# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not( root.left and root.right ):
            if root.left or root.right:
                return False
            return True
        q_left, q_right = [root.left], [root.right]
        
        while q_left and q_right:
            val_left = [node.val if node!='null' else 'null' for node in q_left]
            val_right = [node.val if node!='null' else 'null' for node in q_right]
            if val_left != val_right:
                return False
            q_left = [node for node in q_left if node != 'null']
            q_right = [node for node in q_right if node != 'null']
            l = []
            for node in q_left:
                l.append(node.left if node.left else 'null')
                l.append(node.right if node.right else 'null')
            q_left = l
            r = []
            for node in q_right:
                r.append(node.right if node.right else 'null')
                r.append(node.left if node.left else 'null')
            q_right = r
            
        return not(q_left or q_right)