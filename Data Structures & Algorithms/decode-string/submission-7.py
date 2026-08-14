class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch !="]":
                stack.append(ch)
            else:
                word = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                
                stack.append(int(number) * word)
        return ''.join(stack)