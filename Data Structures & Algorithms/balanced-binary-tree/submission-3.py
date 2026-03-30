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
                return 0
            
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            if abs(left_subtree-right_subtree)>1:
                return -1
            
            if left_subtree == -1 or right_subtree == -1:
                return -1

            return 1 + max(left_subtree,right_subtree)
        res = dfs(root)
        if res != -1:
            return True
        else:
            return False