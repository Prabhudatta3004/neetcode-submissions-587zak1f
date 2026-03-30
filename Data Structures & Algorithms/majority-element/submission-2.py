class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            lookup[num] +=1
        for num,count in lookup.items():
            if count > len(nums)//2:
                return num
                