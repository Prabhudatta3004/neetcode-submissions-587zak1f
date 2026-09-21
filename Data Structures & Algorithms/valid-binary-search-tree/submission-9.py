class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return (
                dfs(node.left, lower, node.val)
                and dfs(node.right, node.val, upper)
            )

        return dfs(root, float("-inf"), float("inf"))