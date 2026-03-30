class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## not be any duplicates
        ## sorted
        ## target has to be found
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1 ## fallback