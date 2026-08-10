from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## frequency
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        ## fill the bucket
        for idx,val in freq.items():
            bucket[val].append(idx)
        
        res = []

        for idx in range(len(bucket)-1,0,-1):

            if not bucket[idx]:
                continue
            
            for num in bucket[idx]:
                res.append(num)
                if len(res) == k:
                    return res