# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(node, max_val):
            nonlocal counter
            if not node:
                return None
            if node.val >= max_val:
                counter +=1
            max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, float('-inf'))
        return counter