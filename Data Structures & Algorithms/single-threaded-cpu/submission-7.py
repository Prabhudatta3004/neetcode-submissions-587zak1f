class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        res = []
        minheap = []
        process=[]
        for idx,task in enumerate(tasks):
            process.append((task[0],task[1],idx))
        process.sort()

        i = 0
        while minheap or i<len(process):
            if not minheap and time < process[i][0]:
                time = process[i][0]
            
            while i<len(process) and process[i][0]<=time:
                heapq.heappush(minheap,(process[i][1],process[i][2]))
                i +=1
            
            if minheap:
                proc_time,idx = heapq.heappop(minheap)
                time +=proc_time
                res.append(idx)
        return res