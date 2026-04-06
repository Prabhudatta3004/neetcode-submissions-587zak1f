class Solution:
    def isPalindrome(self, s: str) -> bool:
        easy_string = ''

        for ch in s:
            if  ch.isalnum():
                easy_string += ch.lower()
        
        left =0
        right = len(easy_string)-1

        while left <= right:
            if easy_string[left] !=  easy_string[right]:
                return False
            left +=1
            right -=1
        return True