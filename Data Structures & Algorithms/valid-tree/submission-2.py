from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # checking connected
        visited = set([0])
        q = deque([0])

        while q:
            node = q.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)

        return len(visited) == n
