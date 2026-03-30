class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}

        ## Now all I have to do is to iterate over
        ## the array and find the difference in 
        ## the hashmap, If i get the difference
        ## I just need to return the indices

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lookup:
                return [lookup[diff],i]
            else:
                lookup[nums[i]] = i
