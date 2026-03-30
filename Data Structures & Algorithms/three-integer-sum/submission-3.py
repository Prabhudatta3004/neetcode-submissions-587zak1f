class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # need to sort the given input
        nums.sort()

        ## now i will fix one number and do
        ## two pointer approach

        for idx in range(len(nums)):

            if idx>0 and nums[idx-1] == nums[idx]:
                continue
            
            start = idx+1
            end = len(nums)-1

            while start<end:
                three_sum = nums[idx] + nums[start] + nums[end]

                if three_sum<0:
                    start +=1
                elif three_sum>0:
                    end -=1
                else:
                    res.append([nums[idx],nums[start],nums[end]])
                    start +=1
                    while start<end and nums[start] == nums[start-1]:
                        start +=1
        return res
