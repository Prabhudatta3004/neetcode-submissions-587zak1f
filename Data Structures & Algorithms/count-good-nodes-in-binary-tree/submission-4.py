# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ## The children must know that the 
        ## max ele of the current path
        max_val = float('-inf')
        counter = 0
        def dfs(node,max_val):
            if not node:
                return 0
            nonlocal counter
            if node.val >= max_val:
                max_val= max(max_val,node.val)
                counter +=1
            dfs(node.left,max_val)
            dfs(node.right,max_val)
        dfs(root,max_val)
        return counter
