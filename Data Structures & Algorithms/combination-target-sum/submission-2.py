class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,path,curr_sum):
            if curr_sum == target:
                res.append(list(path))
                return
            if curr_sum > target:
                return
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,path,curr_sum+nums[i])
                path.pop()
        backtrack(0,[],0)
        return res