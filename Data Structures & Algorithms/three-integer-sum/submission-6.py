class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum = 0
        res = []
        nums.sort() # I am doing this to bring all duplicates together

        for i in range(len(nums)-2):
            if i>0 and nums[i-1] == nums[i]: ## removing the common pivots
                continue
            
            start = i+1
            end = len(nums)-1
            while start<end:
                three_sum = nums[start] + nums[end] + nums[i]
                if three_sum > 0:
                    end -=1
                elif three_sum < 0:
                    start +=1
                else:
                    res.append((nums[i],nums[start],nums[end]))
                    start +=1
                    while start<end and nums[start-1] == nums[start]:
                        start +=1
        return res