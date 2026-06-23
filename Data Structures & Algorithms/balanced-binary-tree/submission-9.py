# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)

            if abs(ls-rs)>1 or ls == -1 or rs == -1:
                return -1
            return 1 + max(ls,rs)
        val = dfs(root)
        
        return True if val != -1 else False