class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        ##visited.add(0)
        count = 0
        def dfs(node,visited):
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr,visited)
        for i in range(n):
            if i not in visited:
                count +=1
                visited.add(i)
                dfs(i,visited)

        return count