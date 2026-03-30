# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ## adding treenode only if it is after a leaf node
        ## if I encounter None then i add it over there
        ## checking condition is if the given val is < or >
        ## than current val
        if not root:
            return TreeNode(val)

        def dfs(node,val):
            if not node:
                return TreeNode(val)
            
            ## checking if the val < than the node.val
            if val < node.val:
                node.left = dfs(node.left,val)
            else:
                node.right = dfs(node.right,val)
            return node
        
        dfs(root,val)
        return root