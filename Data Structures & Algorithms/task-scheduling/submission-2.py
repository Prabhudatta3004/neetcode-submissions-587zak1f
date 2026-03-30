from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        cooldown_queue = deque()
        freq= Counter(tasks)

        maxheap = [-cnt for cnt in freq.values()]

        heapq.heapify(maxheap)

        time = 0

        while maxheap or cooldown_queue:
            time +=1

            if maxheap:
                count = heapq.heappop(maxheap) + 1
                if count < 0:
                    cooldown_queue.append((time+n,count))
            
            if cooldown_queue and cooldown_queue[0][0] == time:
                heapq.heappush(maxheap,cooldown_queue.popleft()[1])
        return time
