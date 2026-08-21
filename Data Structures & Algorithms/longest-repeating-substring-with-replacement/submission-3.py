class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        max_len = 0
        for target in chars:
            start = end = 0
            count = 0
            while end < len(s):

                if s[end] != target:
                    count +=1
                end +=1

                if count > k:
                    if s[start] != target:
                        count -=1
                    start +=1
                
                max_len = max(max_len,end-start)
        return max_len
                

