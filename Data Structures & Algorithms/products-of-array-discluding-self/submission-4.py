class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length
        res = [0] * length
        prefix[0] = postfix[length-1] = 1

        ## for the prefix

        for idx in range(1,length):
            prefix[idx] = prefix[idx-1] * nums[idx-1]
        

        ## for the postfix

        for idx in range(length-2,-1,-1):
            postfix[idx] = postfix[idx+1] * nums[idx+1]

        
        for idx in range(length):
            res[idx] = postfix[idx] * prefix[idx]
        
        return res