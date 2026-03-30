class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n - 1

        # Case when array is not rotated
        if nums[start] <= nums[end]:
            return nums[start]

        while start <= end:
            mid = start + (end - start) // 2
            next_ele = (mid + 1) % n
            prev_ele = (mid - 1 + n) % n

            # Check if nums[mid] is the minimum
            if nums[mid] <= nums[next_ele] and nums[mid] <= nums[prev_ele]:
                return nums[mid]

            # Compare mid with end, not start
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
