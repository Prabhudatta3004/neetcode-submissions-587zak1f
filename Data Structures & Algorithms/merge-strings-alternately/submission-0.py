class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res= []
        temp1 = 0
        temp2 = 0

        while temp1< len(word1) and temp2 < len(word2) :

            res.append(word1[temp1])
            res.append(word2[temp2])
            temp1 +=1
            temp2 +=1
        
        if temp1<len(word1):
            res.append(word1[temp1:])
        if temp2<len(word2):
            res.append(word2[temp2:])

        return ''.join(res)
