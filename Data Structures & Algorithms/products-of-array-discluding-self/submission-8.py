class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [0] * len(nums)
        for idx in range(len(nums)):
            res[idx] = prefix
            prefix *= nums[idx]
        
        postfix = 1
        for idx in range(len(nums)-1,-1,-1):
            res[idx] *= postfix
            postfix *= nums[idx]
        
        return res