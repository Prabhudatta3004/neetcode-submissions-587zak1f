# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            ls = dfs(node.left)
            rs = dfs(node.right)

            curr_dia = ls+rs
            max_diameter =max(max_diameter, curr_dia)

            return 1 + max(ls,rs)
        dfs(root)
        return max_diameter