class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## construct the graph and calculate the indegree

        graph = [[] for _ in range(numCourses)]
        in_degree = [0]* numCourses
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1
        

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        counter = 0
        while q:
            node = q.popleft()
            counter +=1

            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr] == 0:
                    q.append(nbr)

        return counter == numCourses
