class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def add(minheap, val):
            heapq.heappush(minheap, val )
            if len(minheap) > k:
                heapq.heappop(minheap)
            
            return minheap[0]
        minheap = []
        for n in nums:
            ans = add(minheap,n)
        return ans
        