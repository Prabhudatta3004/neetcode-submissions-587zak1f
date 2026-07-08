class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        if n ==2:
            return 1

        prev3 = 0
        prev2,prev = 1,1
        for idx in range(3,n+1):
            idx = prev + prev2 + prev3
            prev3 = prev2
            prev2 = prev
            prev = idx
        return prev           