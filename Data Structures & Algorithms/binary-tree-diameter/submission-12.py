# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = float('-inf')

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)

            diameter = lh+rh
            max_diameter = max(max_diameter,diameter)
            return 1+max(lh,rh)
        dfs(root)
        return max_diameter