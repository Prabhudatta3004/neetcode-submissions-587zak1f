class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ele in s:
            if ele != ']':
                stack.append(ele)
            else:
                curr_str = ''
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str

                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * curr_str)
        
        return ''.join(stack)
            
