class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,state,running_sum):
            if running_sum == target:
                res.append(state[:])
                return
            if running_sum>target:
                return
            for idx in range(start,len(nums)):
                state.append(nums[idx])
                backtrack(idx,state,running_sum+nums[idx])
                state.pop()
        backtrack(0,[],0)
        return res