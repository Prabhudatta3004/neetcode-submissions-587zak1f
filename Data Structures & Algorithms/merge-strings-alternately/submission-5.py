class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""

        ptr1 = 0
        ptr2 = 0

        while ptr1<len(word1) and ptr2<len(word2):
            merged_string += word1[ptr1]
            ptr1 +=1

            merged_string += word2[ptr2]
            ptr2 +=1
        
        if ptr1 < len(word1):
            merged_string += word1[ptr1:]
        if ptr2 < len(word2):
            merged_string += word2[ptr2:]
        
        return merged_string