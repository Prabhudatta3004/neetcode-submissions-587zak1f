class Solution:
    def decodeString(self, s: str) -> str:
        ## i can see that i need to push all
        ## elements into the stack 
        ## when i see a "]" i need to start 
        ## poping from my stack, i need to stop somewhere
        ## when i see [ then I pop 1 more time to get the number
        ## but the number can be any number of digit( okay I can keep
        ## poping till its all digits

        stack = []

        for ele in s:
            if ele != "]":
                stack.append(ele)
            else:
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop()+ curr_str
                
                ## need to remove "["
                stack.pop()
                k= ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k)*curr_str)
        return "".join(stack)