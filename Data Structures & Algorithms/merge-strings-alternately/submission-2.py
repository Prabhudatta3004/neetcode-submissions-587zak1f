class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        res = []
        while idx<len(word1) and idx<len(word2):
            res.append(word1[idx])
            res.append(word2[idx])
            idx +=1
        
        if idx < len(word1):
            res.append(word1[idx:])
        if idx < len(word2):
            res.append(word2[idx:])
        return "".join(res)