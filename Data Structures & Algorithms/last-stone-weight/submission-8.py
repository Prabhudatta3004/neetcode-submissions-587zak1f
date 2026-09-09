class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap= []
        for stone in stones:
            heapq.heappush(maxheap,(-stone))

        while len(maxheap) > 1:
            first = - (heapq.heappop(maxheap))
            second= - (heapq.heappop(maxheap))

            if first != second:
                heapq.heappush(maxheap,-(first-second))
        return -maxheap[0] if maxheap else 0