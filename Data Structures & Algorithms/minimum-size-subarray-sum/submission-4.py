class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        window_val = 0
        min_val = float('inf')

        while end < len(nums):
            window_val += nums[end]
            end +=1

            while window_val >=target:
                min_val= min(min_val, end-start)
                window_val -= nums[start]
                start +=1
        return min_val if min_val != float('inf') else 0