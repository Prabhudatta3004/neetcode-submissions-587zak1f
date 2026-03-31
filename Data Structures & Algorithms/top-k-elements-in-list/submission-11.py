class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        minheap = []
        res = []
        for num in nums:
            freqmap[num] = freqmap.get(num,0) + 1
        
        for val,freq in freqmap.items():

            heapq.heappush(minheap,(freq,val))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        for _ in range(k):
            _,val = heapq.heappop(minheap)
            res.append(val)
        return res