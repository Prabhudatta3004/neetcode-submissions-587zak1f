class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        min_len = float('inf')
        window_sum = 0
        while end < len(nums):
            window_sum += nums[end]
            end +=1

            while window_sum >= target:
                min_len = min(min_len,end-start)

                window_sum -= nums[start]
                start +=1
        return min_len if min_len != float('inf') else 0