class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end

        while start <= end:
            mid = start + (end-start)//2
            total_hour = 0
            for p in piles:
                total_hour += math.ceil(float(p)/mid)
            
            if total_hour <= h:
                res = mid
                end = mid - 1
            elif total_hour > h:
                start = mid + 1
        return res