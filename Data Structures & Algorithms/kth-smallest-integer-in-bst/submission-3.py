# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res,k
            ## if i reached null node: I simply return
            if not node:
                return
            
            ## smaller elements always lie in left subtree
            ## but what if we dont have left subtree or we
            ## ran out of nodes compared to k
            ## i can enter the left subtree, reduce k by 1 
            ## if k becomes ==0 then I can return
            ## else I can call the rightsubtree, move to its left

            dfs(node.left)
            k -=1
            if k == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res