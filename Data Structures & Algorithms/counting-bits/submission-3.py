class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)

        for idx in range(n+1):
            num = idx
            while num:
                res[idx] += num&1
                num = num>>1
        return res