class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reachability = 0
        farthest = 0
        jumps = 0
        for idx in range(len(nums)-1):
            farthest = max(farthest,idx+nums[idx])

            if idx == max_reachability:
                jumps +=1
                max_reachability = farthest
        return jumps