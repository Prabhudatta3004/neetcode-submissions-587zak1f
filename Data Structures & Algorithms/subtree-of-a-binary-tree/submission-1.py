class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are exactly the same
        def issame(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return issame(t1.left, t2.left) and issame(t1.right, t2.right)
        
        # Main DFS to traverse the root tree
        def dfs(node):
            if not node:
                return False
            if issame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
