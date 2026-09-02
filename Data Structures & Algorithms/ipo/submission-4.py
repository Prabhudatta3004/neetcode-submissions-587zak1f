class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital,profits))
        i  = 0 
        maxheap = []

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(maxheap,-(projects[i][1]))
                i +=1
            
            if not maxheap:
                break
            
            profit = -(heapq.heappop(maxheap))
            w += profit
        return w

