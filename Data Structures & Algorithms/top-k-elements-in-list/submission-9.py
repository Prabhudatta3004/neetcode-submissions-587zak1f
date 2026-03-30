class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        res =[]
        lookup = {}
        for num in nums:
            lookup[num] = lookup.get(num,0) + 1
        for num,count in lookup.items():
            heapq.heappush(minheap,(count,num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        while k:
            res.append(heapq.heappop(minheap)[1])
            k -=1
        return res