class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            for idx in range(start, len(candidates)):
                # Skip duplicate choices at the same recursion level
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue

                # Candidates are sorted, so nothing later can fit
                if candidates[idx] > remaining:
                    break

                path.append(candidates[idx])
                dfs(idx + 1, remaining - candidates[idx], path)
                path.pop()

        dfs(0, target, [])
        return res