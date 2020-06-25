# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, n1, n2, ans):
            if not node:
                return []
            l = lca(node.left, n1, n2, ans)
            r = lca(node.right, n1, n2, ans)
            desc = [ p for p in [node.left] + l + [node.right] + r if p]
            if n1 in desc + [node] and n2 in desc + [node] and not ans:
                ans.append(node)
            return desc
        ans = []
        _ = lca(root, p, q, ans)
        
        return ans[0]
        