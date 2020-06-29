# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, k: int) -> List[List[int]]:
        def path_util(node):
            if not node :
                return []
            if not(node.left or node.right):
                return [[node.val,],]
            left = path_util(node.left)
            right = path_util(node.right)
            ans = [[node.val] + arr for arr in left+right]
            return ans
        ans = path_util(root)
        #print(ans)
        return [arr for arr in ans if sum(arr) == k]