class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the prefix and the postfix size should be same as the nums
        n = len(nums)
        prefix_prod = [0] * n
        postfix_prod = [0] * n
        res=[0] * n

        ## Now we have two lists for pre and post
        ## For pre I want the first element to be 1 and 
        ## For post fix I want the last element to be 1 
        ## THis handles our tests cases for the 1st and last ele

        prefix_prod[0] = 1
        postfix_prod[n-1] = 1

        ##Now We need to populate the entire pre and post lists

        ## For prefix we need to loop through the entire nums 
        ## starting from 1 till n

        for i in range(1,n):
            prefix_prod[i] = nums[i-1] * prefix_prod[i-1]
        ## For postfix
        for i in range(n-2,-1,-1):
            postfix_prod[i] = nums[i+1] * postfix_prod[i+1]

        for i in range(n):
            res[i] = prefix_prod[i] * postfix_prod[i]

        return res
