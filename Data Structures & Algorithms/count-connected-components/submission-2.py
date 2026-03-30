class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        graph =[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node,visited):
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr,visited)
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i,visited)
        return count