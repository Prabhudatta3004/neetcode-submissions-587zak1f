class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                first = stack.pop()
                last = stack.pop()
                stack.append(last-first)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                first = stack.pop()
                last = stack.pop()
                stack.append(int(last/first))
            else:
                stack.append(int(token))
        
        return stack[-1]