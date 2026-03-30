class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_jump = 0

        for i in range(len(nums)):

            if i>current_jump:
                return False
            
            current_jump= max(current_jump, i + nums[i])

            if current_jump > len(nums)-1:
                return True
        return True