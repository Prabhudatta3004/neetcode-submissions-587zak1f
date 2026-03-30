class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        min_length = float('inf')
        window_sum= 0
        while end < len(nums):
            window_sum += nums[end]

            while window_sum >= target:
                min_length = min(min_length,(end-start+1))
                window_sum -= nums[start]
                start +=1
            end +=1
        
        return 0 if min_length ==float("inf") else min_length