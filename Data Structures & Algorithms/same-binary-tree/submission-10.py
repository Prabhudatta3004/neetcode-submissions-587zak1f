class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            # Case 1: Both are empty (reached the end of a branch)
            if not node1 and not node2:
                return True
            
            # Case 2: One is empty or values don't match
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Case 3: Recursively check left and right subtrees
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(p, q)