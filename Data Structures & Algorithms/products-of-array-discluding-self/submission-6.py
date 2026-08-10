class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        ## lets fill prefix first
        prefix[0] = 1 ## for 1st element

        for idx in range(1,n):
            prefix[idx] = prefix[idx-1] * nums[idx-1]
        
        postfix[n-1] = 1
        for idx in range(n-2,-1,-1):
            postfix[idx] = postfix[idx+1] * nums[idx+1]
        
        for idx in range(n):
            res[idx] = prefix[idx] * postfix[idx]
        return res