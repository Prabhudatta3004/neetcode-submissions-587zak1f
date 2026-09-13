class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        farthest = 0
        for idx in range(len(nums)):

            if idx > farthest:
                return False
            
            farthest = max(farthest,idx+nums[idx])

            if farthest > target:
                return True
        return True
        