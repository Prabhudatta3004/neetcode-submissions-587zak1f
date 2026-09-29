class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] ## stores the subsets
        def backtrack(start,state):
            res.append(state[:])

            for idx in range(start,len(nums)):
                state.append(nums[idx])
                backtrack(idx+1,state)
                state.pop()
        backtrack(0,[])
        return res