class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" and len(stack) >= 2:
                stack.append(stack.pop() + stack.pop())
            elif token == "-" and len(stack) >=2:
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "*" and len(stack)>=2:
                stack.append(stack.pop() * stack.pop())
            elif token == "/" and len(stack) >=2:
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(token))
        return stack[-1]