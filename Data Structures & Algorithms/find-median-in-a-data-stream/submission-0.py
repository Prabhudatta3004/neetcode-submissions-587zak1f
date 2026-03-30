class MedianFinder:

    def __init__(self):
        self.minheap= []
        self.maxheap = [] 
        

    def addNum(self, num: int) -> None:
        ## Checking if the number is greater than the
        ## root of the minheap at the right
        # if yes it belongs to the right heap
        # if no it belongs to the left heap
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1 * num)


        ## Now we need to make sure that both the 
        ## heap trees are balanced
        ## if the left side heap > right side heap 
        ## we can pop from left add it to right and vice versa

        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * val)

    def findMedian(self) -> float:

        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        return (-1 * self.maxheap[0] + self.minheap[0]) / 2.0
        
        