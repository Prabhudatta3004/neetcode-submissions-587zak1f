class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        lookup ={"}":"{","]":"[",")":"("}
        for ch in s:
            if ch in lookup:
                if not stack or stack.pop() != lookup[ch]:
                    return False
            else:
                stack.append(ch)
        if not stack:
            return True
        else:
            return False