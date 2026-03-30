class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, path, path_sum):
            nonlocal target
            if path_sum == target:
                res.append(path[:])
                return
            if path_sum > target:
                return
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j+1,path,path_sum + nums[j])
                path.pop()
        dfs(0,[],0)
        return res