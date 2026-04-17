class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        candidate = max(piles)

        start = 1
        end = max(piles)

        while start <= end:
            mid = start +  (end-start)//2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile)/mid)

            if total_time <=h:
                candidate= mid
                end = mid-1
            elif total_time >h:
                start = mid+1
        return candidate