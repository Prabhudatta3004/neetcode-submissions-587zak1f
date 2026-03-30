class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup = {}
        for i,ch in enumerate(s):
            lookup[ch] = i

        
        count = 0

        end = 0
        res = []
        for i in range(len(s)):
            count +=1
            end = max(end,lookup[s[i]])
            if i == end:
                res.append(count)
                count = 0
        return res