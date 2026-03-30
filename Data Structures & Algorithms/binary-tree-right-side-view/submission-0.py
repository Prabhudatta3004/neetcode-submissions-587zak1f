# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # The right side view does not always gives the right children
        # It can be a left child if there is no right child
        # My first intuition is to go with the level order traversal
        ## and print the last element of each level

        def bfs(root):
            if root is None:
                return []
            res = []
            q= collections.deque()
            q.append(root)
            while q:
                qlen = len(q)
                for i in range(qlen):
                    node = q.popleft()
                    if i == qlen-1:
                        res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return res
        return bfs(root)