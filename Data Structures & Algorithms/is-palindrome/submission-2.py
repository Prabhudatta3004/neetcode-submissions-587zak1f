class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""
        for c in s:
            if c.isalnum():
                str1+=c.lower()

        i = 0
        j = len(str1) - 1

        while i<j:
            if str1[i] != str1[j]:
                return False
            j -=1
            i +=1 
        return True