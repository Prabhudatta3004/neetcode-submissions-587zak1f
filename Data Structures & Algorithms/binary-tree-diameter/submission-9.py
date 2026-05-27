# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            ls = dfs(node.left)
            rs = dfs(node.right)

            res = max(res,ls+rs)
            return 1 + max(ls,rs)
        dfs(root)
        return res
