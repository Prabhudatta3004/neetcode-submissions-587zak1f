# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ## If i go for DFS , it will visit a node
        ## keep checking with max val if val > max_val
        ## add counter
        ## Now in the example at first i will pass the 
        ## root node
        ## now as per dfs we will go left subtree and 
        ## right subtree
        ## while doing so we will eventually keep on passing the 
        ## max_val and while backtracking we will increment the counter

        def dfs(root, max_val):
            ## Now base case
            if not root:
                return 0
            if root.val >= max_val:
                res = 1
            else:
                res = 0
            max_val = max(max_val, root.val)

            res += dfs(root.left,max_val)
            res += dfs(root.right, max_val)

            return res
        return dfs(root, root.val)