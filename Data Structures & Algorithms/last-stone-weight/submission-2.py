class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]

        maxheap = stones
        heapq.heapify(maxheap)

        while len(maxheap)>1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)

            if second > first:
                heapq.heappush(maxheap,first-second)
        
        
        maxheap.append(0)

        return abs(stones[0])