class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = [0]*26
        freq_t = [0]*26
        for ch in s:
            freq_s[ord(ch)-ord('a')] +=1
        
        for ch in t:
            freq_t[ord(ch)-ord('a')] +=1
        
        if freq_s == freq_t:
            return True
        return False