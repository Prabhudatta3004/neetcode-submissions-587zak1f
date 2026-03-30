class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for ch in s:
            # If it's a closing bracket
            if ch in lookup:
                # Check if stack is empty OR top of stack doesn't match
                if not stack or stack.pop() != lookup[ch]:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(ch)
        
        # If stack is empty, all brackets were matched correctly
        return not stack