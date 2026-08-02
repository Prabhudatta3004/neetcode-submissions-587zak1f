class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        idx = 0

        ans = [-1] * (2*len(nums))

        for idx in range(0,len(nums)):
            ans[idx] = ans[idx+len(nums)] = nums[idx]
        return ans