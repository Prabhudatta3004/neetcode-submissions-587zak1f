class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, path_sum):
            nonlocal target
            if path_sum == target:
                res.append(path[:])
                return
            if path_sum > target:
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j,path,path_sum + nums[j])
                path.pop()
        dfs(0,[],0)
        return res