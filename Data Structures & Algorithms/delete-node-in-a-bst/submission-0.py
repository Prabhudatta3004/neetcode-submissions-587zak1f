class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = dfs(node.left, key)
            
            elif key > node.val:
                node.right = dfs(node.right, key)

            else:
                # Node to delete found

                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Two children: find inorder successor
                successor = node.right
                while successor.left:
                    successor = successor.left

                node.val = successor.val
                node.right = dfs(node.right, successor.val)

            return node
        
        return dfs(root, key)
