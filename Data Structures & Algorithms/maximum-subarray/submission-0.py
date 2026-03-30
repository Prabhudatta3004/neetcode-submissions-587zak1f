class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        best = float("-inf")

        for num in nums:
            curr += num
            best = max(curr,best)
            if curr < 0:
                curr = 0
        return best