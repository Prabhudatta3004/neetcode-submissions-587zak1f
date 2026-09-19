class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        def can_ship(capacity):
            curr_weight = 0
            ship = 1
            for weight in weights:
                if curr_weight+weight > capacity:
                    ship +=1
                    curr_weight = weight
                else:
                    curr_weight +=weight
            return ship <=days
        
        while start<=end:
            mid = start + (end-start)//2

            if can_ship(mid):
                candidate = mid
                end = mid-1
            else:
                start = mid+1
        return candidate