class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rotated_index(nums):
            n = len(nums)
            start, end = 0, n - 1

            if nums[start] <= nums[end]:
                return 0

            while start <= end:
                mid = start + (end - start) // 2
                prev_ele = (mid - 1 + n) % n
                next_ele = (mid + 1) % n

                # Check if mid is the smallest
                if nums[mid] <= nums[prev_ele] and nums[mid] <= nums[next_ele]:
                    return mid

                # If mid is bigger than end, min is in right half
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

            return 0  # fallback

        def binary_search(nums, start, end, target):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        n = len(nums)
        pivot = rotated_index(nums)

        # Search in the correct half
        if nums[pivot] <= target <= nums[n - 1]:
            return binary_search(nums, pivot, n - 1, target)
        else:
            return binary_search(nums, 0, pivot - 1, target)
