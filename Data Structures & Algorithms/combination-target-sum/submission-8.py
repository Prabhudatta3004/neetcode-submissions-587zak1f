class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,running_sum,path):
            if running_sum == target:
                res.append(path[:])
                return
            
            if running_sum > target:
                return
            
            for idx in range(i,len(nums)):
                path.append(nums[idx])
                dfs(idx,running_sum+nums[idx],path)
                path.pop()
        dfs(0,0,[])
        return res