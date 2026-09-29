class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        freq = Counter(nums)
        for idx,val in freq.items():
            heapq.heappush(minheap,(val,idx))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res =[]
        while minheap:
            _,num = heapq.heappop(minheap)
            res.append(num)
        return res
