import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        minheap= []

        count = {} 

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] +=1
        
        for num in count.keys():
            heapq.heappush(minheap, (count[num],num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res
