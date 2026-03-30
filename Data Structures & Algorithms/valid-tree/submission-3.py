class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)

        while queue:
            node = queue.popleft()
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)
        return len(visited) == n