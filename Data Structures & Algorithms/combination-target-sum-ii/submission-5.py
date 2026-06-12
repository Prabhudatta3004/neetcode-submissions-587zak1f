class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, path, running_sum):
            if running_sum == target:
                res.append(path[:])
                return
            if running_sum > target:
                return 
            
            for idx in range(index, len(candidates)):
                if idx > index and candidates[idx] == candidates[idx-1]:
                    continue
                
                path.append(candidates[idx])
                dfs(idx+1, path, running_sum+ candidates[idx])
                path.pop()
        dfs(0,[],0)
        return res
                