class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(start,end):
            while start<end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True
        

        def backtrack(start,curr_substring):
            if start == len(s):
                res.append(curr_substring[:])
                return
            
            for curr in range(start,len(s)):
                if isPalindrome(start,curr):
                    curr_substring.append(s[start:curr+1])
                    backtrack(curr+1,curr_substring)
                    curr_substring.pop()
        backtrack(0,[])
        return res