class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start = end = 0

        chars = set()

        while end < len(nums):
            if nums[end] in chars:
                return True
            
            chars.add(nums[end])
            end +=1

            while end-start>k:
                chars.remove(nums[start])
                start+=1
        return False