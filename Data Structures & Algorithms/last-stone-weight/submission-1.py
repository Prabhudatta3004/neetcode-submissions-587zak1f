class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        k = 2
        minheap = stones
        heapq.heapify(minheap)

        while len(minheap)>1:
            first_element = heapq.heappop(minheap)
            second_element = heapq.heappop(minheap)
            if second_element>first_element:
                heapq.heappush(stones,first_element-second_element)

        
        minheap.append(0)

        return abs(stones[0])