class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        writer = reader = 0

        while reader<len(nums):
            if nums[reader]!=nums[writer]:
                writer +=1
                k+=1
                nums[writer]=nums[reader]
            reader+=1
        return k