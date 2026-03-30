class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        super_string = ""

        for ch in s:
            if ch.isalnum():
                super_string +=ch.lower()

        
        start = 0
        end = len(super_string)-1

        while start<=end:
            if super_string[start] != super_string[end]:
                return False
            
            start +=1
            end -=1
        return True
