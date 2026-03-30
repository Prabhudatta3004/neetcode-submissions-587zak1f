class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop()+stack.pop())
            elif ele == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif ele == "*":
                stack.append(stack.pop()*stack.pop())
            elif ele == "/":
                first = stack.pop()
                second = stack.pop() 
                stack.append(int(second/first))     
            else:
                stack.append(int(ele))
        return stack[-1]     
                 