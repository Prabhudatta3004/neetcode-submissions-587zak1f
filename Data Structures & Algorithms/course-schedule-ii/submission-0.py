class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## first build the graph and in_degree
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1

        res = []

        q  = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr] ==0:
                    q.append(nbr)
        
        if len(res) != numCourses:
            return []
        else:
            return res