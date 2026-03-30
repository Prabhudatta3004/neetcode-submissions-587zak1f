class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## Need to find the closest values to the origin
        ## So we need distance as the key for the points
        ## distance from origin is sqrt(x1**2+y1**2) but we can 
        ## ignore the sqrt and use it as key
        ## since we are trying to find the minimum value
        ## we should go for a MAX_HEAP

        maxheap = []
        res = []
        for x,y in points:
            distance = (x**2 + y**2)
            heapq.heappush(maxheap,[-distance, x, y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        while maxheap:
            distance, x, y = heapq.heappop(maxheap)
            res.append([x,y])
        return res