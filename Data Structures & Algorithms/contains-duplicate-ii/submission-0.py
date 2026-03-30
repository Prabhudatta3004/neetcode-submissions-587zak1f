from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        start = 0

        for end in range(len(nums)):
            # if num already in window → duplicate found
            if nums[end] in seen:
                return True

            seen.add(nums[end])

            # keep window size <= k
            if end - start >= k:
                seen.remove(nums[start])
                start += 1

        return False
