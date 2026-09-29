class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx in range(len(strs[0])):
            for s in strs:
                if idx == len(s) or s[idx] != strs[0][idx]:
                    return s[:idx]
        return strs[0]