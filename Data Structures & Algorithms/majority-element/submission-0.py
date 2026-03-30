class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)//2

        lookup ={}
        for n in nums:
            if n not in lookup:
                lookup[n] =1
            else:
                lookup[n] +=1
        for keys,values in lookup.items():
            if values > major:
                return keys