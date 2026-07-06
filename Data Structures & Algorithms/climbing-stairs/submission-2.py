class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(idx):
            if idx>n:
                return 0
            if idx == n:
                return 1
            if cache[idx] !=-1:
                return cache[idx]
            
            cache[idx] = dfs(idx+1) + dfs(idx+2)
            return cache[idx]
        return dfs(0)