class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [-1] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for idx in range(3,n+1):
            dp[idx] = dp[idx-1] + dp[idx-2]
        return dp[n]