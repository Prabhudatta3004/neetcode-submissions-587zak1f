#from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #@cache
        cache = [-1] * (len(cost)+1)
        def dfs(idx):
            if idx<=1:
                return 0
            if cache[idx] != -1:
                return cache[idx]
            one_step = dfs(idx-1) + cost[idx-1]
            two_step = dfs(idx-2) + cost[idx-2]
            
            cache[idx] = min(one_step,two_step)
            return cache[idx]
        return dfs(len(cost))