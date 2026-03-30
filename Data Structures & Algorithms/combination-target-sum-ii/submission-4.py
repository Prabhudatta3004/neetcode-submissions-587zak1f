class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start,curr_sum,path):
            if curr_sum == target:
                res.append(path[:])
                return
            if curr_sum > target:
                return
            for idx in range(start,len(candidates)):
                if idx > start and candidates[idx-1] == candidates[idx]:
                    continue
                path.append(candidates[idx])
                dfs(idx+1,curr_sum+candidates[idx],path)
                path.pop()
        dfs(0,0,[])
        return res