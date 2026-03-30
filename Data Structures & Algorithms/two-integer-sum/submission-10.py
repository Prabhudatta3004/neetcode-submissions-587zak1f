class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}## number and index

        for idx,num in enumerate(nums):
            lookup[num] = idx
        
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in lookup and lookup[diff] != idx:
                return [idx,lookup[diff]]
        