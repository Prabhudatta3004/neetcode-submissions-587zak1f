class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                
                start = j+1
                end = len(nums)-1

                while start<end:
                    four_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if four_sum < target:
                        start +=1
                    elif four_sum>target:
                        end -=1
                    else:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        start +=1
                        while start<end and nums[start-1] == nums[start]:
                            start +=1
        return res
            
