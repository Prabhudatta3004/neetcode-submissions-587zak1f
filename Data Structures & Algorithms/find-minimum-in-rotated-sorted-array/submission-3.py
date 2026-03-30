class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## We are trying to find the minimum element
        ## To identify the minimum element always check
        ## if the element is smaller than its right as well as
        ## smaller than its left
        ## Now we can search using the mid index
        ## Now how to go to the correct subarray?
        ## if the subarray is unsorted then we will find the
        ## minimum in that subarray

        start = 0
        end = len(nums)-1
        mid = 0

        while start <= end:
            mid = start + (end-start)//2
            if nums[start] <= nums[end]:
                return nums[start]

            next_ele = (mid + 1) % len(nums)
            prev_ele= (mid + len(nums) - 1) % len(nums)

            if nums[mid] <= nums[next_ele] and nums[mid] <= nums[prev_ele]:
                return nums[mid]
            
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1