class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx in range(len(nums)-2):

            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            
            left = idx+1
            right = len(nums)-1

            while left<right:
                three_sum = nums[idx] + nums[left] + nums[right]

                if three_sum > 0:
                    right -=1
                elif three_sum < 0:
                    left +=1
                else:
                    res.append([nums[idx],nums[left],nums[right]])
                    left +=1
                    right -=1

                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
        return res