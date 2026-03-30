class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        
        ## cycle detection in undirected graph

        graph= [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        
        queue = deque()
        queue.append((0,-1))
        visited.add(0)
        while queue:
            node,parent = queue.popleft()
           
            for nbr in graph[node]:
                if nbr not  in visited:
                    visited.add(nbr)
                    queue.append((nbr,node))
                elif nbr != parent:
                    return False
        return len(visited) == n 
        