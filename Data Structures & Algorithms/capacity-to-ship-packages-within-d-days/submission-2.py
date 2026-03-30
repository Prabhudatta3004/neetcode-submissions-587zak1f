class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        candidate = end

        def can_ship(capacity):
            day = 1
            total_weight = 0

            for w in weights:
                if total_weight + w > capacity:
                    day +=1
                    total_weight = w
                else:
                    total_weight +=w
            return day <= days

        while start <= end:
            mid = start + (end-start)//2

            if can_ship(mid):
                candidate = mid
                end = mid - 1
            else:
                start = mid + 1
        return candidate