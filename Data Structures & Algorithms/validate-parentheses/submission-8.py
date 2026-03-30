class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")":"(","}":"{","]":"["}
        stack = []
        for ele in s:
            if ele in lookup:
                if not stack or stack.pop() != lookup[ele]:
                    return False
            else:
                stack.append(ele)
        return not stack