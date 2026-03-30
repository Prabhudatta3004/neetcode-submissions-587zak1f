class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## [1,2,3,5] target : 4

        start = 0
        end = len(nums)-1

        while start<=end:
            mid = start + (end-start)//2

            if nums[mid] < target:
                start +=1
            elif nums[mid] > target:
                end -=1
            else:
                return mid
        
        return start ## fallback
