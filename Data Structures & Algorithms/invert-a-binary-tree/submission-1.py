# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## This feels like we are traversing each child and reversing
        ## This needs to be done for all nodes, DFS comes to mind
        ## Now tha I look into the graphic I see that the left subtree and 
        ## right subtree are swapped and their children are also swapped

        ## The perfect traversal for such case feels like inorder where we 
        ## visit a node , swap the left child and the right child 
        ## then we move ahead 

        def dfs(node):
            if not node:
                return 
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            return root
        return dfs(root)