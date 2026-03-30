class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(curr_start,path,total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return

            
            for choice in range(curr_start,len(candidates)):
                if choice>curr_start and candidates[choice-1] == candidates[choice]:
                    continue
                path.append(candidates[choice])
                backtrack(choice+1,path,total + candidates[choice])
                path.pop()
            
        backtrack(0,[],0)

        return res