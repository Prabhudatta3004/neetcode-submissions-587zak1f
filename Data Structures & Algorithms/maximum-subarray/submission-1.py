class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = 0

        for num in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum += num
            max_sum = max(max_sum, running_sum)

        return max_sum