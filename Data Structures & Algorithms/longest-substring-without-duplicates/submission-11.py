class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            while s[end] in lookup:
                lookup.remove(s[start])
                start +=1
            
            lookup.add(s[end])
            end +=1
            max_len = max(max_len,end-start)
            
        return max_len