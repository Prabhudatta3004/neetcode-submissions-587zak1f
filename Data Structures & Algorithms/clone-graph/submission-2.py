"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        lookup = {} ## key: original_node: copied_node
        lookup[node] = Node(node.val)
        queue = deque()
        queue.append(node)


        while queue:
            current_node= queue.popleft()

            for nbr in current_node.neighbors:
                if nbr not in lookup:
                    lookup[nbr] = Node(nbr.val)
                    queue.append(nbr)
                
                lookup[current_node].neighbors.append(lookup[nbr])

        return lookup[node]