class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way for 1 step, 2 ways for 2 steps
        if n <= 2:
            return n
        
        # prev2 represents ways to reach (i-2)
        # prev1 represents ways to reach (i-1)
        prev2 = 1 
        prev1 = 2
        
        # We start from the 3rd step up to n
        for idx in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1