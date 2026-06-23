class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            ls = dfs(node1.left, node2.left)
            rs = dfs(node1.right, node2.right)

            return ls and rs

        return dfs(p, q)