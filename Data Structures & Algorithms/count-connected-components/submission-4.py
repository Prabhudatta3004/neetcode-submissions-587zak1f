class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph =[[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        def dfs(node):
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr)
        count = 0
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)
        return count