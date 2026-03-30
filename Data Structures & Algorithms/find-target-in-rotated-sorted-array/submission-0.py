from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Finding the index of the minimum element (pivot)
        def find_minele(nums):
            start = 0
            end = len(nums) - 1

            while start <= end:
                if nums[start] <= nums[end]:
                    return start  # return index, not value

                mid = start + (end - start) // 2
                prev = (mid - 1 + len(nums)) % len(nums)
                nex = (mid + 1) % len(nums)

                if nums[mid] <= nums[prev] and nums[mid] <= nums[nex]:
                    return mid  # return index

                elif nums[start] <= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

            return -1  # shouldn't happen for valid input

        ## Binary search
        def binary_search(nums, start, end, target):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        if not nums:
            return -1

        min_index = find_minele(nums)

        # Try searching in both sorted halves
        left = binary_search(nums, 0, min_index - 1, target)
        if left != -1:
            return left

        return binary_search(nums, min_index, len(nums) - 1, target)
