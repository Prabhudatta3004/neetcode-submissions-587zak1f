class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        courses = []
        while queue:
            node = queue.popleft()
            courses.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr] == 0:
                    queue.append(nbr)
        if len(courses) == numCourses:
            return True
        else:
            return False