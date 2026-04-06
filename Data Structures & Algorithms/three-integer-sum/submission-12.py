class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):

            if idx>0 and nums[idx] == nums[idx-1]:
                continue
            
            start = idx+1
            end = len(nums)-1

            while start < end:
                threesum = nums[idx] + nums[start] + nums[end]

                if threesum > 0:
                    end -=1
                elif threesum < 0:
                    start +=1
                else:
                    res.append([nums[idx],nums[start],nums[end]])
                    start +=1
                    end -=1
                    while start < end and nums[start] == nums[start-1]:
                        start +=1
                    while start < end and nums[end] == nums[end+1]:
                        end -=1

                    
        return res
