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
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            max_diameter = max(max_diameter, left_subtree+right_subtree)

            return 1+max(left_subtree,right_subtree)

        dfs(root)
        return max_diameter