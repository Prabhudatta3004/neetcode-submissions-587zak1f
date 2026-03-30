class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        lookup = set()   # use set instead of list for O(1) lookup
        max_size = 0

        while end < len(s):
            if s[end] not in lookup:
                lookup.add(s[end])
                max_size = max(max_size, end - start + 1)
                end += 1
            else:
                # remove from left until duplicate is gone
                lookup.remove(s[start])
                start += 1

        return max_size
