class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                word = ''
                while stack[-1] != "[":
                    word = stack.pop() + word
                
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)* word)
        return "".join(stack)
        