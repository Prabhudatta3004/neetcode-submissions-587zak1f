# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## The DFS function returns us the height of the subtree
        ## This will not be helpful to get the diameter
        ## The diameter encompasses height of left subtree + height of right subtree
        res = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal res
            res = max(res, dfs(node.left) + dfs(node.right))
            return 1 + max(dfs(node.left), dfs(node.right))
        
        dfs(root)
        return res
