class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ## anagrams and the permutations are the same

        lookup_t = {}
        lookup_s = {}

        for ch in s:
            if ch not in lookup_s:
                lookup_s[ch] = 1
            
            lookup_s[ch] +=1
        for ch in t:
            if ch not in lookup_t:
                lookup_t[ch] = 1
            lookup_t[ch] +=1

        return lookup_t == lookup_s