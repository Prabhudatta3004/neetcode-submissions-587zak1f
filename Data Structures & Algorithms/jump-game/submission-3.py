class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        target = len(nums)-1

        for idx in range(len(nums)):
            if idx > farthest:
                return False
            
            farthest = max(farthest,idx+nums[idx])
            if idx >= target:
                return True
                