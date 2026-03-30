class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        # If array is not rotated
        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            mid = start + (end - start) // 2

            next_ele = (mid + 1) % len(nums)
            prev_ele = (mid - 1) % len(nums)

            # Check if mid is the pivot (minimum element)
            if nums[mid] <= nums[next_ele] and nums[mid] <= nums[prev_ele]:
                return nums[mid]

            # ✅ Key Fix: compare with nums[end], not nums[start]
            elif nums[mid] > nums[end]:
                # Minimum lies in the right half
                start = mid + 1
            else:
                # Minimum lies in the left half (including mid)
                end = mid

        return nums[start]
