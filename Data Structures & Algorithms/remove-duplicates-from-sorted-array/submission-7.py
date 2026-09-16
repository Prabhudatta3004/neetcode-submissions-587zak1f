class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        reader = writer = 0

        while reader < len(nums):
            if nums[reader] != nums[writer]:
                writer +=1
                nums[writer] = nums[reader]
                k +=1
            reader +=1
        return k