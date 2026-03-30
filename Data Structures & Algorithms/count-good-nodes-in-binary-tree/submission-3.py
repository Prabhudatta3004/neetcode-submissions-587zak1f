# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(node,max_value):
            nonlocal counter
            if not node:
                return None
            if node.val >= max_value:
                max_value = max(max_value,node.val)
                counter +=1
            
            dfs(node.left,max_value)
            dfs(node.right,max_value)

        dfs(root,root.val)

        return counter