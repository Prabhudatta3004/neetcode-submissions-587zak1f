class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## a+b = target
        ## I need some previous knowledge of values
        ## can use a hashmap value:index we have to return the index
        ## i thought of hashset but that will store only non-repetative characters

        hashmap = {} ## values:indices

        for i in range(len(nums)):
            
            diff = target- nums[i]

            if diff in hashmap:
                return [hashmap[diff],i]
            
            hashmap[nums[i]] = i
        

            