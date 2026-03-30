class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr_level = 0
        jumps = 0
        if len(nums)<1:
            return 0
        
        for i in range(len(nums)-1):

            farthest = max(farthest,i+nums[i])

            if i == curr_level:
                jumps +=1
                curr_level = farthest
            if curr_level >= len(nums)-1:
                break
        return jumps