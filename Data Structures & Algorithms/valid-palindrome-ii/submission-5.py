class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(start,end):
            while start<end:
                if s[start] == s[end]:
                    start +=1
                    end -=1
                else:
                    return False
            return True
        
        start = 0
        end = len(s)-1

        while start < end:
            if s[start] == s[end]:
                start +=1
                end -=1
            else:
                return is_palindrome(start+1,end) or is_palindrome(start,end-1)
        return True
