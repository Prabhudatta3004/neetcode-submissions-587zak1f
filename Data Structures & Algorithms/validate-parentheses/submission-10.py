class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"]":"[","}":"{",")":"("}
        stack = []

        for ch in s:
            if ch not in lookup:
                stack.append(ch)
            else:
                if not stack or stack.pop()!= lookup[ch]:
                    return False
        return not stack