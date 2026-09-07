class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        visited.add(0)

        if len(edges) != n-1:
            return False
        queue = deque()
        queue.append((0,-1))

        while queue:
            node,parent = queue.popleft()

            for nbr in graph[node]:
                if nbr == parent:
                    continue
                if nbr in visited:
                    return False
                visited.add(nbr)
                queue.append((nbr,node))
        return len(visited)==n
