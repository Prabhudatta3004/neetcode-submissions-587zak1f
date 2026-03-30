class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] ## this will store the operands and the final ans

        for token in tokens:
            if token == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1+num2)
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2-num1)
            elif token == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2*num1)
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(int(num2/num1))
            else:
                stack.append(token)
        return int(stack[-1])