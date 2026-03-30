class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        count = 1
        for moving in range(1,len(nums)):
            if nums[moving] != nums[unique]:
                unique +=1
                count +=1
                nums[unique] = nums[moving]
        return count
