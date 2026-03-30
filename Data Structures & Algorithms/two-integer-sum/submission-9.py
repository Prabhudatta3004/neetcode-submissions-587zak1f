class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for idx,num in enumerate(nums):
            diff = target-num
            if diff in lookup:
                return [lookup[diff],idx]
            lookup[num] = idx