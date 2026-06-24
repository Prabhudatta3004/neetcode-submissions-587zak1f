class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = writer = 0
        k=1

        while reader < len(nums):

            if nums[writer] == nums[reader]:
                reader +=1
            else:
                writer +=1
                k+=1
                nums[writer] = nums[reader]
        return k