class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def dfs(start,path):
            nonlocal res
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            
            for idx in range(start, len(nums)):
                path.append(nums[idx])
                dfs(idx,path)
                path.pop()
        dfs(0,[])
        return res
