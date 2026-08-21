class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = float('-inf')
        start = end = 0
        chars = set()
        if not s:
            return 0
        while end<len(s):

            while s[end] in chars:
                chars.remove(s[start])
                start +=1
            chars.add(s[end])
            end +=1

            max_len = max(max_len,end-start)
        return max_len