class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        super_string = ""
        for ch in s:
            if ch.isalnum():
                super_string += ch.lower() 
        
        ##print(super_string)

        i=0  
        j= len(super_string)-1

        while i<j:
            if super_string[i] != super_string[j]:
                return False
            
            i +=1
            j -=1
        return True