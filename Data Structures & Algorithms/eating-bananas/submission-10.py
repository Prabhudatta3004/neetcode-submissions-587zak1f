class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        candidate = end

        def can_eat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            
            return time <= h
        

        while start <= end:
            mid = start + (end-start)//2

            if can_eat(mid):
                candidate = mid
                end = mid-1
            else:
                start = mid+1
        return candidate