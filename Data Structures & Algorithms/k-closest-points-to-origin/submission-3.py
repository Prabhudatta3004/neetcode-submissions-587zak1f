class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxheap = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = - ((x**2) + (y**2))

            ## somehow push the points to a maxheap
            ## comparison based on distance

            heapq.heappush(maxheap,(dist,x,y))

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        res = []
        for _ in range(k):
          dist,x,y =  heapq.heappop(maxheap)
          res.append([x,y])
        return res