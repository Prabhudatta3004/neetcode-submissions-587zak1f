class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res=[]
        for idx in range(0,len(nums)-3):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            for idx2 in range(idx+1,len(nums)-2):
                if idx2>idx+1 and nums[idx2]== nums[idx2-1]:
                    continue
                left = idx2+1
                right = len(nums)-1

                while left < right:
                    four_sum = nums[idx] + nums[idx2] + nums[left] + nums[right]

                    if four_sum < target:
                        left +=1
                    elif four_sum > target:
                        right -=1
                    else:
                        res.append([nums[idx],nums[idx2],nums[left],nums[right]])
                        left +=1
                        right -=1

                        while left<right and nums[left] == nums[left-1]:
                            left +=1
                        while right>left and nums[right] == nums[right-1]:
                            right -=1
        return res         