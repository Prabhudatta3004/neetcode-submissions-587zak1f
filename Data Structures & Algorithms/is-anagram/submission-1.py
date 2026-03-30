class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup_s={}
        lookup_t={}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            lookup_s[s[i]] = 1 + lookup_s.get(s[i], 0)
            lookup_t[t[i]] = 1 + lookup_t.get(t[i],0)
        return lookup_s == lookup_t
