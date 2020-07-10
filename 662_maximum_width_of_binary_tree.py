# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        pos ={root:1}
        ans = 1
        curr_nodes=[root]
        while curr_nodes:
            next_nodes = []
            min_pos = float("inf")
            max_pos = 0
            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)
                    pos[node.left] = (pos[node] - 1)*2 + 1
                    min_pos = min((pos[node] - 1)*2 + 1, min_pos)
                    max_pos = max((pos[node] - 1)*2 + 1, max_pos)
                if node.right:
                    next_nodes.append(node.right)
                    pos[node.right] = (pos[node] - 1)*2 + 2
                    min_pos = min((pos[node] - 1)*2 + 2, min_pos)
                    max_pos = max((pos[node] - 1)*2 + 2, max_pos)
            ans = max(ans, max_pos - min_pos + 1)
            curr_nodes = next_nodes
        return ans
                
                
        