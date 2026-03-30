class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * 2 * len(nums)
        length = len(nums)

        for i in range(length):
            ans.insert(i,nums[i])
            ans.insert(length+i, nums[i])
        
        return ans