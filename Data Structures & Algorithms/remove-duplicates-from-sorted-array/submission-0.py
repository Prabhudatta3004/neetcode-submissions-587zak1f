class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        moving= 0
        counter = 1

        for moving in range(len(nums)):
            if nums[moving] != nums[unique]:
                unique +=1
                counter +=1
                nums[unique] = nums[moving]
        return counter