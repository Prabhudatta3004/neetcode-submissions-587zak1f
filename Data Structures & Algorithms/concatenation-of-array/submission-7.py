class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))

        for idx in range(len(nums)):
            ans[idx] = ans[len(nums)+idx] = nums[idx]
        return ans