class MedianFinder:

    def __init__(self):
        self.maxheap = [] ## entry point
        self.minheap = []
        #self.count = 0

    def addNum(self, num: int) -> None:
        #self.count += 1
        heapq.heappush(self.maxheap,(-num))
        if self.maxheap and self.minheap and -(self.maxheap[0])>self.minheap[0]:
            heapq.heappush(self.minheap,-(heapq.heappop(self.maxheap)))
        
        if len(self.maxheap)>len(self.minheap)+1:
            heapq.heappush(self.minheap,-(heapq.heappop(self.maxheap)))
        if len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,-(heapq.heappop(self.minheap)))





    def findMedian(self) -> float:
        if len(self.maxheap)> len(self.minheap):
            return -(self.maxheap[0])
        else:
            return (-(self.maxheap[0])+self.minheap[0])/2.0
        