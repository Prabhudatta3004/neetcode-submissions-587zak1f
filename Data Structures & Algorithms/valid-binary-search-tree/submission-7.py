# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,leftMax,rightMax):
            if not node:
                return True
            
            if not leftMax < node.val < rightMax:
                return False
            
            ls = dfs(node.left,leftMax,node.val)
            rs = dfs(node.right,node.val,rightMax)

            if not ls or not rs:
                return False
            else:
                return True
        return dfs(root,float('-inf'),float('inf'))
