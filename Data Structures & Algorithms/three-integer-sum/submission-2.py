class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            while start<end:
                s = nums[i]+nums[start]+nums[end]

                if s>0:
                    end -=1
                elif s<0:
                    start +=1
                else:
                    res.append([nums[i],nums[start],nums[end]])

                    start +=1

                    while start<end and nums[start]== nums[start-1]:
                        start +=1
        return res