# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## The question asks for the diameter of the binary tree
        ## Which gives the longest path, since we have to go through
        ## All the paths, we can go for a DFS, now for the diameter
        ## I was thinking of using dfs to get the maximum depth
        ## then we can use and keep on adding the left subtree and 
        ## right subtree depths and store it in the result

        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left+right) 
            # Adding the left and right subtree length
            return 1 + max(left,right)

        dfs(root)
        return res
