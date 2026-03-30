class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for idx in range(0,len(nums)-3):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            for idx2 in range(idx+1,len(nums)-2):
                if idx2 > idx+1 and nums[idx2] == nums[idx2-1]:
                    continue
                
                start = idx2 + 1
                end = len(nums)-1

                while start < end:
                    foursum = nums[idx] + nums[idx2] + nums[start] + nums[end]

                    if foursum < target:
                        start +=1
                    elif foursum > target:
                        end -=1
                    else:
                        res.append([nums[idx],nums[idx2],nums[start],nums[end]])
                        start +=1
                        end -=1
                        while start < end and nums[start] == nums[start-1]:
                            start +=1
                        while start < end and nums[end] == nums[end+1]:
                            end -=1
        return res