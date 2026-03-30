class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        max_freq = 0
        start,end = 0,0
        freq = {}

        while end<len(s):
            ## grow
            freq[s[end]]  = freq.get(s[end],0) + 1
            max_freq = max(max_freq,freq[s[end]])

            while end-start+1 - max_freq > k:
                freq[s[start]] -= 1
                start +=1
            
            res = max(res, end-start+1)
            end +=1
        return res