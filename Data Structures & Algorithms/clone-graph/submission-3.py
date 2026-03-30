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
            return None
        hashmap ={node:Node(node.val)}# created a copy


        queue = deque()
        queue.append(node)

        while queue:
            n = queue.popleft()

            for nbr in n.neighbors:
                if nbr not in hashmap:
                    hashmap[nbr] = Node(nbr.val)
                    queue.append(nbr)
                
                hashmap[n].neighbors.append(hashmap[nbr])
        return hashmap[node]
        