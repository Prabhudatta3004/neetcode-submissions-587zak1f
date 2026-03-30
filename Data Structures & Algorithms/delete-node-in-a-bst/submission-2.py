class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            # 1. Base case: If we reach a null pointer, the key wasn't found
            if not node:
                return None
            
            if key > node.val:
                node.right = dfs(node.right, key)
            elif key < node.val:
                node.left = dfs(node.left, key)
            else:
                # 2. Found the node to delete!
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # 3. Two children case
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                node.val = successor.val
                # Crucial: find and delete that duplicate value in the right subtree
                node.right = dfs(node.right, successor.val)
            
            # 4. Return the (possibly modified) node back up the stack
            return node
            
        return dfs(root, key)