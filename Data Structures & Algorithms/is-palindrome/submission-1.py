class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        final_s = ""

        for i in s:
            if i.isalnum():
                final_s+=i
        
        length= len(final_s)

        i=0
        j=length-1

        while i<j and j>i:
            if final_s[i] != final_s[j]:
                return False
            i +=1
            j -=1
        return True