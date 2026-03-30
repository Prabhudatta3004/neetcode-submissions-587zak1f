class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for idx, val in enumerate(nums):
            comp = target - val
            if comp in lookup:
                return [lookup[comp], idx]
            lookup[val] = idx