from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        # Build the adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([(0, -1)])  # (node, parent)

        while queue:
            node, parent = queue.popleft()
            
            if node in visited:
                continue
            visited.add(node)
            
            for nbr in graph[node]:
                if nbr == parent:
                    continue
                if nbr in visited:
                    # Found a back-edge → cycle
                    return False
                queue.append((nbr, node))
        
        # Must be connected (all nodes visited)
        return len(visited) == n
