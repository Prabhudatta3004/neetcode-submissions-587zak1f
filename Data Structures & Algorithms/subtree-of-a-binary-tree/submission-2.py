# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1,node2):
            if not node1 and not node2:
                return True
            
            if node1 and node2 and node1.val==node2.val:
                return same_tree(node1.left,node2.left) and same_tree(node1.right,node2.right)

            return False
        
        def dfs(root,subroot):
            if not subroot:
                return True
            
            if not root:
                return False


            if not same_tree(root,subroot):
                return dfs(root.left,subroot) or dfs(root.right,subroot)

            return True
        return dfs(root,subRoot)