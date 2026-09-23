class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree= [0]*numCourses
        graph = [[] for _ in range(numCourses)]
    
        for v,u in prerequisites:
            graph[u].append(v)
            in_degree[v] +=1
        
        queue = deque()## will store those which have 0 in_degeee
        for val in range(numCourses):
            if in_degree[val] == 0:
                queue.append(val)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for nbr in graph[node]:
                in_degree[nbr] -=1
                if in_degree[nbr]==0:
                    queue.append(nbr)
        return True if len(res)==numCourses else False