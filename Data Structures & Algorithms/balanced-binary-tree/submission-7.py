# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True,0]
            
            ls = dfs(node.left)
            rs = dfs(node.right)
            is_balanced = ls[0] and rs[0] and abs(ls[1]-rs[1]) <= 1
            return [is_balanced, 1 + max(ls[1],rs[1])]
        return dfs(root)[0]