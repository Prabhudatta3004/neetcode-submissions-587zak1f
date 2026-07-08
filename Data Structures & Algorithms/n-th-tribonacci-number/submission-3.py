class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        if n ==2:
            return 1
        cache = [-1] * (n+1)

        cache[0] = 0
        cache[1],cache[2] = 1,1

        for idx in range(3,n+1):
            cache[idx] = cache[idx-1] + cache[idx-2] + cache[idx-3]
        return cache[n]            