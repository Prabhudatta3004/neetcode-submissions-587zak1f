class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)
        prefix = strs[0] ## Taking the entire small string as initital prefix
        if not strs:
            return ""
        for i in range(1,n):
            while strs[i].find(prefix) !=0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix