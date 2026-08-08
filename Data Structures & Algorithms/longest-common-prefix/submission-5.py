class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for idx in range(len(strs[0])):
            for string in strs:
                if idx == len(string):
                    return string[:]
                elif string[idx] != strs[0][idx]:
                    return string[:idx]
        return strs[0]