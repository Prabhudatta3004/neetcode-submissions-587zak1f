class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [-1]*(n+1)
        def dfs(idx):
            if idx==0:
                return 0
            if idx == 1 or idx ==2:
                return 1
            if cache[idx] != -1:
                return cache[idx]
            cache[idx] = dfs(idx-1) + dfs(idx-2) + dfs(idx-3)
            return cache[idx]
        return dfs(n)