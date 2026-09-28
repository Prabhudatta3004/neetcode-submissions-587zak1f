class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        max_len = 0
        seen = set()
        while end<len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start +=1
            seen.add(s[end])
            max_len = max(max_len,len(seen))
            end +=1
        return max_len
