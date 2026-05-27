# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            ls = height(root.left)
            rs = height(root.right)
            if abs(ls-rs) > 1:
                return -1
            if ls == -1  or rs == -1:
                return -1
            return 1+max(ls,rs)
        return height(root) != -1
