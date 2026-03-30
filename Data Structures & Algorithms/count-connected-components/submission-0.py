class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        count = 0

        def bfs(node):
            queue = deque()
            queue.append(node)

            while queue:
                curr_node = queue.pop()
                for nbr in graph[curr_node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)

        for i in range(n):
            if i not in visited:
                count +=1
                bfs(i)

        return count