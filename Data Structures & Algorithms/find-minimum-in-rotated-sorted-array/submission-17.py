class Solution:
    def findMin(self, nums: List[int]) -> int:
         
        start = 0
        end = len(nums)-1
        
        ## condition if the array is rotated N times
        if nums[start] <= nums[end]:
            return nums[start]
        
        while start<=end:

            mid = start +(end-start)//2

            prev = (mid-1) % len(nums)
            nxt = (mid+1) %  len(nums)

            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        