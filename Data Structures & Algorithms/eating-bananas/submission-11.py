class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start_rate = 1
        end_rate = max(piles)
        candidate = end_rate

        def can_eat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            return time<=h
        
        

        while start_rate<=end_rate:
            mid = start_rate +(end_rate-start_rate)//2

            if can_eat(mid):
                candidate = mid
                end_rate= mid-1
            else:
                start_rate = mid+1
        return candidate