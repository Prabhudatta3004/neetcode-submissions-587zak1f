class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        start = 0
        end = 0
        while end < len(nums):
            if (end-start)>k:
                seen.remove(nums[start])
                start +=1
            if nums[end] in seen:
                return True
            seen.add(nums[end])
            end +=1
        return False
