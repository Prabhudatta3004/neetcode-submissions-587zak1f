class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []

        lookup = {} #task:frequencies

        for task in tasks:
            lookup[task] = lookup.get(task,0) + 1
        

        for _,freq in lookup.items():
            heapq.heappush(maxheap,-freq)
        queue = deque()
        time = 0
        while maxheap or queue:
            time +=1

            if maxheap:
                count = heapq.heappop(maxheap) + 1
                if count < 0: ## it needs more cycles
                    queue.append((time+n,count))
            
            if queue and queue[0][0] == time:
                heapq.heappush(maxheap,queue.popleft()[1])
        return time

