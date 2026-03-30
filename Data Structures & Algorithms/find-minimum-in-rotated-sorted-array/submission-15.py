class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        # if array is not rotated
        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            mid = start + (end - start) // 2

            # if middle element > rightmost element,
            # then min must be in right half
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid  # pivot is in left half including mid

        return nums[start]
