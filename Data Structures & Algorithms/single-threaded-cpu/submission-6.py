class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_tasks = []

        for i,task in enumerate(tasks):
            new_tasks.append((task[0],task[1],i))
        new_tasks.sort()

        minheap = []
        time = 0
        i = 0
        res = []
        while minheap or i<len(new_tasks):
            
            if not minheap and time < new_tasks[i][0]:
                time = new_tasks[i][0]
            
            while i<len(new_tasks) and new_tasks[i][0] <= time:
                heapq.heappush(minheap,(new_tasks[i][1],new_tasks[i][2]))
                i +=1
            
            if minheap:
               proc_time,indx = heapq.heappop(minheap)
               time += proc_time
               res.append(indx)
        return res