class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0

        new_string = ''

        while ptr1 <len(word1) or ptr2<len(word2):
            if ptr1 < len(word1):
                new_string += word1[ptr1]
                ptr1 +=1
            if ptr2 < len(word2):
                new_string += word2[ptr2]
                ptr2 +=1
        return new_string