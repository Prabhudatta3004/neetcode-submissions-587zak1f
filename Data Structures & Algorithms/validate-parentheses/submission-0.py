class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"}":"{", "]":"[",")":"("}
        stack = []

        for n in s:
            if n in lookup:
                if stack and stack[-1] == lookup[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        
        return True if not stack else False
