class Solution:
    def findMin(self, nums: List[int]) -> int:
        candidate= 0

        start = 0
        end = len(nums)-1

        while start<end:
            mid = start + (end-start)//2

            if nums[mid]>nums[end]:
                start = mid+1
            elif nums[mid]<nums[end]:
                #candidate = mid
                end = mid
        return nums[start]