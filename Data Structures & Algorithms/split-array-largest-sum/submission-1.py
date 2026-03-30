class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > limit:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k
        
        low = max(nums)
        high = sum(nums)
        candidate = high
        while low<=high:
            mid = low + (high-low)//2

            if can_split(mid):
                candidate = mid
                high = mid - 1
            else:
                low = mid + 1
        return candidate
        