class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = [] # this will be our heap(stack with size k)

        for n in nums:
            self.add(n)



    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
