from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx<=1:
                return 0
            
            one_step = dfs(idx-1) + cost[idx-1]
            two_step = dfs(idx-2) + cost[idx-2]

            return min(one_step,two_step)
        return dfs(len(cost))