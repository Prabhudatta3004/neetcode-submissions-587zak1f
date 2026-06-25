class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ## to detect and prevent duplicates

        res = [] ## to store triplets

        ## this loop runs from start till length-2

        for idx in range(0,len(nums)-2):

            ## skip same values to avoid duplicate triplets
            if idx>0 and nums[idx] == nums[idx-1]:
                continue
            
            start = idx+1
            end = len(nums)-1

            while start < end:
                three_sum = nums[idx] + nums[start] + nums[end]

                if three_sum < 0:
                    start +=1
                elif three_sum > 0:
                    end -=1
                else:
                    res.append([nums[idx],nums[start],nums[end]])
                    start +=1
                    end -=1
                    while start < end and nums[start] == nums[start-1]:
                        start +=1
                    while end > start and nums[end] == nums[end+1]:
                        end -=1
        return res