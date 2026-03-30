class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1

        queue = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)
        courses = []
        while queue:
            node = queue.popleft()
            courses.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr] == 0:
                    queue.append(nbr)
        return courses if len(courses)==numCourses else []
