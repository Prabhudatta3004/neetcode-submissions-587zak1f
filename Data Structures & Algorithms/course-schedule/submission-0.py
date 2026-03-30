class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        ## build the graph and in_degree
        for u,v in prerequisites:
            graph[v].append(u)
            in_degree[u] +=1

        ## create a queue that holds all 0 indegree nodes
        res = []
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        ## in the end check the length of the queue being == or != to NumCourses
        while q:
            node = q.popleft()
            res.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr] == 0:
                    q.append(nbr)

            
        if len(res) != numCourses:
            return False
        else:
            return True

