class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end
        while start<=end:
            mid = start + (end-start)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/mid)
            
            if total_time <=h:
                res = mid
                end = mid - 1
            elif total_time > h:
                start = mid + 1

        return res