class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        writer = 0
        reader = 1

        while reader < len(nums):

            if nums[reader] != nums[writer]:
                writer +=1
                count +=1
                nums[writer] = nums[reader]
            reader +=1
        return count