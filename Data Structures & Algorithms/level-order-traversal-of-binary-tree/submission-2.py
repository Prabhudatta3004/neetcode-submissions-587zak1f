# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] ## this will return the outer list
        queue = deque() ## this queue will hold all the elements level wise
        ## lets insert the root node to the queue
        queue.append(root)

        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            if level:
                result.append(level)
        return result