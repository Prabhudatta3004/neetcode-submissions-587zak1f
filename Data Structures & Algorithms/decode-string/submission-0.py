class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                ## we need to get the string and k 
                st = ""
                while stack[-1] != "[":
                    st = stack.pop() + st ## adding pop then the prev (since going backwards)
                stack.pop()## to remove the opening bracket
                ## now each open bracket has a number before it
                ## it can be double-triple digit so
                k= ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # adding pop then the prev (since going backwards)
                stack.append(int(k)*st)

        return "".join(stack)
