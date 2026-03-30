class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(root, subRoot):
            if root is None and subRoot is None:
                return True 
            if not root or not subRoot:
                return False
            return (
                root.val == subRoot.val and
                issame(root.left, subRoot.left) and
                issame(root.right, subRoot.right)
            )

        def dfs(root, subRoot):
            if not root:
                return False
            if issame(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)
