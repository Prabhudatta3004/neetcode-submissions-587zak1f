class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = {}
        for num in nums:
            # Standard way to increment or initialize
            lookup[num] = lookup.get(num, 0) + 1
            
            # Optimization: check as you go
            if lookup[num] > len(nums) // 2:
                return num