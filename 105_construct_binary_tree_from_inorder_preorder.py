# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> TreeNode:
        
        if not len(p):
            return None
        root = TreeNode(p[0])
        def make_tree_util(node, preo, ino):
            if not node or not len(preo) or not len(ino):
                return
            
            L = len(preo)
            p_idx = {v:i for i,v in enumerate(preo)}
            i_idx = {v:i for i,v in enumerate(ino)}
            
            p_idx_node = p_idx[node.val]
            i_idx_node = i_idx[node.val]
            
            num_nodes_left = i_idx_node
            num_nodes_right = L - i_idx_node - 1

            if num_nodes_left:
                node.left = TreeNode(preo[p_idx_node+1])
                make_tree_util(node.left, preo[p_idx_node + 1 : p_idx_node + num_nodes_left + 1], ino[0:i_idx_node])
            if num_nodes_right:
                node.right = TreeNode(preo[p_idx_node+num_nodes_left+1])
                make_tree_util(node.right, preo[p_idx_node+num_nodes_left+1:], ino[i_idx_node+1:])
            
            
        make_tree_util(root, p, i)
        return root
            
                
        