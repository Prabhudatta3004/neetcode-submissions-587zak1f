from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1

        for n, c in hashmap.items():
            bucket[c].append(n)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
