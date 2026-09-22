class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap=[]
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)
        cooldown = deque()
        time = 0
        while cooldown or maxheap:
            time +=1

            if maxheap:
                remaining_time = heapq.heappop(maxheap) + 1

                if remaining_time !=0:
                    cooldown.append((remaining_time,time+n))
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxheap,cooldown.popleft()[0])
        return time

