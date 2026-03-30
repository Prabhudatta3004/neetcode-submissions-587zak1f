class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        first_speed = 1
        last_speed = max(piles)

        res = last_speed
        while first_speed<=last_speed:
            total_time = 0
            mid_speed = (first_speed+last_speed)//2
            for p in piles:
                total_time += math.ceil(float(p)/mid_speed)
            if total_time<=h:
                res = mid_speed
                last_speed = mid_speed-1
            elif total_time>h:
                first_speed = mid_speed+1
        
        return res