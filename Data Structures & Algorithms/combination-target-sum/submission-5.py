class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx,curr_sum,path):
            if curr_sum == target:
                res.append(path[:])
                return
            
            if curr_sum > target:
                return 
            
            for idx in range(idx,len(nums)):
                path.append(nums[idx])
                dfs(idx,curr_sum+nums[idx],path)
                path.pop()
        dfs(0,0,[])
        return res