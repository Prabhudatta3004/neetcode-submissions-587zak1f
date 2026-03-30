class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for idx in range(len(nums)):

            if idx>0 and nums[idx] == nums[idx-1]:
                continue
            
            for idx2 in range(idx+1,len(nums)):
                if idx2>idx+1 and nums[idx2] == nums[idx2-1]:
                    continue
                
                start = idx2+1
                end = len(nums)-1

                while start<end:
                    four_sum = nums[idx] + nums[idx2] + nums[start] + nums[end]

                    if four_sum < target:
                        start +=1
                    elif four_sum > target:
                        end -=1
                    
                    else:
                        res.append([nums[idx],nums[idx2],nums[start],nums[end]])
                        start +=1
                        while start<end and nums[start] == nums[start-1]:
                            start +=1
        return res