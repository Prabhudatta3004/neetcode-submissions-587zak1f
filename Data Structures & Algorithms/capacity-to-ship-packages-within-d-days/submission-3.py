class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        candidate = end

        def covers(capacity)->bool:
            day = 1
            weight = 0
            for w in weights:
                if weight + w > capacity:
                    day +=1
                    weight = w
                else:
                    weight +=w
            return day <= days
        while start <= end:
            mid = start + (end-start)//2

            if covers(mid):
                candidate = mid
                end = mid-1
            else:
                start = mid+1
        return candidate 
