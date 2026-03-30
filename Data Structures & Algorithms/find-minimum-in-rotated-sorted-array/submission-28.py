class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            # compare middle element with rightmost
            if nums[mid] > nums[end]:
                # minimum lies to the right
                start = mid + 1
            else:
                # minimum is at mid or to the left
                end = mid

        # start == end → smallest element
        return nums[start]
