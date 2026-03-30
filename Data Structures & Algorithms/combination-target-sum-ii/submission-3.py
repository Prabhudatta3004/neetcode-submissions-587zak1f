class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start,path_sum,path):
            if path_sum == target:
                res.append(list(path))
                return
            if path_sum > target:
                return
            
            for i in range(start,len(candidates)):
                if i>start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path_sum+candidates[i],path)
                path.pop()
        backtrack(0,0,[])
        return res
