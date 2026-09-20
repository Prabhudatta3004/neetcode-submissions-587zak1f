class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        targets = set(s)
        max_len = 0
        for target in targets:
            start = 0
            end = 0
            count=0
            while end<len(s):
                if s[end] != target:
                    count +=1
                while count>k:
                    if s[start]!= target:
                        count -=1
                    start +=1
                max_len = max(max_len,end-start+1)
                end +=1
        return max_len