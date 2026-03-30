class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = set()
        start = end = 0

        while end< len(nums):
            if nums[end] in lookup:
                return True
            
            lookup.add(nums[end])
            end +=1

            if end-start > k:
                lookup.remove(nums[start])
                start +=1
        return False