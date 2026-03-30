class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None, they are the same
        if not p and not q:
            return True
        
        # Base case: if one is None or the values don't match, they are not the same
        if not p or not q or p.val != q.val:
            return False
            
        # Recursive step: check both the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)