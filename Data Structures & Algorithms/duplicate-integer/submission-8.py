class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        num = 0 
        while num < len(nums):
            if nums[num] in seen:
                return True
            seen.add(nums[num])
            num +=1
        return False