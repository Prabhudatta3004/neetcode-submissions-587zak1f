class Solution:
    def findMin(self, nums: List[int]) -> int:
         
        start = 0
        end = len(nums)-1

        if nums[start] <= nums[end]:
            return nums[start]

        
        while start<end:
            mid = start + (end-start)//2

            ## if mid < from both ends then return mid

            prev = (mid-1) % len(nums)
            nxt = (mid+1) % len(nums)

            if nums[mid] < nums[nxt] and nums[mid] < nums[prev]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        return nums[start]

