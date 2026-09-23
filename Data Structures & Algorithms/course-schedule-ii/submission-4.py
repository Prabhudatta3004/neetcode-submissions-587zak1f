class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        in_degree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1
        
        for val in range(numCourses):
            if in_degree[val] == 0:
                queue.append(val)
        res=[]
        while queue:
            node = queue.popleft()
            res.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr]==0:
                    queue.append(nbr)
        if len(res)==numCourses:
            return res
        else:
            return []
