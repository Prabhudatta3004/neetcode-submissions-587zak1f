class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}

        for i,ch in enumerate(s):
            last_seen[ch] = i
        
        res = []
        count = 0
        max_seen = 0
        for i,ch in enumerate(s):
            count +=1
            max_seen = max(max_seen,last_seen[ch])

            if i == max_seen:
                res.append(count)
                count = 0
        return res