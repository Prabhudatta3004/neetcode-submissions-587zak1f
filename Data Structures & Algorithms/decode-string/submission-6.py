class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                word = ""

                while stack[-1] != "[":
                    word = stack.pop() + word
                
                stack.pop()

                k = ''

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * word)
        return "".join(stack)

                