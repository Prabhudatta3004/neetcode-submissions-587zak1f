class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        set_s = [0] * 26
        set_t = [0] * 26

        ## lets create the frequency map for s

        for ch in s:
            set_s[ord(ch)-ord('a')] +=1

        for ch in t:
            set_t[ord(ch)-ord('a')] +=1

        if set_s == set_t:
            return True

        else:
            return False
            