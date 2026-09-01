class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap= []

        freq = Counter(tasks)

        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)

        cooldown_queue = deque()
        time = 0
        while maxheap or cooldown_queue:
            time +=1

            if maxheap:
                remaining_count = heapq.heappop(maxheap) + 1

                if remaining_count != 0:
                    cooldown_queue.append([remaining_count, time + n])

            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(maxheap,cooldown_queue.popleft()[0])
        return time