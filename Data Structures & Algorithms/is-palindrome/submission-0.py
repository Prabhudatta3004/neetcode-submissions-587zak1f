class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## to check whether the string is palindrome or not
        ## I need a two pointer approach in which I need 
        ## to loop once through the string and have two pointers
        ## One from the start and the other from the ned
        ## Keep on checking if the values are same 
        ## but how long should they be going till i<j and J>i

        s = s.lower()
        final_s = ""
        for i in s:
            if i.isalnum():
                final_s += i
        i=0
        j= len(final_s) - 1
        if not final_s:
            return True
        while i<j and j>i:
            if final_s[i] != final_s[j]:
                return False
            i +=1
            j -=1
        return True