class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        count = 0
        res = []

        for point in points:
            count +=1
            dist = (point[0]**2) + (point[1]**2)

            heapq.heappush(maxheap,(-dist,count,point))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        
        while maxheap:
            _,_,point = heapq.heappop(maxheap)
            res.append(point)
        return res