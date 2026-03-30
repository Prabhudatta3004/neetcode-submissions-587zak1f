# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            if lh < 0: lh = 0
            if rh<0: rh = 0
            max_sum = max(max_sum,node.val+lh+rh)

            return node.val + max(lh,rh)
        dfs(root)
        return max_sum