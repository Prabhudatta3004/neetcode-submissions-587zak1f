class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        lookup = set()
        max_count = 0
        while right < len(s):
            if s[right] not in lookup:
                lookup.add(s[right])
                max_count = max(max_count, right-left+1)
                right +=1
            else:
                lookup.remove(s[left])
                left +=1
        return max_count