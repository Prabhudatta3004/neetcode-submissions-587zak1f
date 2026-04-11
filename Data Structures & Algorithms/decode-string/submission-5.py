class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ele in s:
            if ele != "]":
                stack.append(ele)
            else:
                word = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k)* word)
        
        return ''.join(stack)