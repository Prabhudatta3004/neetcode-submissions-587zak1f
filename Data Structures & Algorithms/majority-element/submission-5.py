class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for idx in range(1,len(nums)):
            if nums[idx] == candidate:
                count +=1
            if nums[idx] != candidate:
                count -=1
            if count == 0:
                candidate = nums[idx]
                count = 1
        return candidate