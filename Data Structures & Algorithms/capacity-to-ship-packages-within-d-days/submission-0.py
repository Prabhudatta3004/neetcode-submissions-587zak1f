class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        res = sum(weights)

        def canShip(cap):
            ships_counter = 1
            curr_cap = cap

            for w in weights:
                if curr_cap-w < 0:
                    ships_counter +=1
                    if ships_counter>days:
                        return False
                    curr_cap = cap
                curr_cap -= w
            return ships_counter <= days
        while left<=right:
            mid = left + (right-left)//2

            if canShip(mid):
                res = min(res,mid)
                right = mid-1
            else:
                left= mid+1
        
        return res