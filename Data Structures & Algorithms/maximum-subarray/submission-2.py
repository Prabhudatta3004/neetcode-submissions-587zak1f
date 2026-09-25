class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        running_sum = 0
        max_sum = float('-inf')
        for num in nums:
            if running_sum <0:
                running_sum = 0
            running_sum += num
            max_sum = max(max_sum,running_sum)
        return max_sum