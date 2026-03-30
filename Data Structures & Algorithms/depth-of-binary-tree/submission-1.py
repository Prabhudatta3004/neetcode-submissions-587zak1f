# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## Since we are exploring the depths of the tree
        ## we need to move till the end leaf nodes.
        ## we can do that by going through each subtree
        ## and while we do so we can keep on adding +1 for the
        ## current visited node , this will give us the 
        ## depth of the tree
        ## when we reach the leaf node, it wont have any depth
        ## the value will be 0 ## we can return 1+ max(dfs(left), dfs(tright))

        ## By doing so for each node we can get the max depth and recursively
        ## we can calculate that and backtrack to the root node to
        ## get the final max depth of the tree

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)
        return dfs(root)