class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr = 0
        length = len(s)
        while ptr<length//2:
            s[ptr],s[length-ptr-1] = s[length-ptr-1], s[ptr]
            ptr +=1
        