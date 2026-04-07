class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                if first != 0:
                    stack.append(int(second/first))
            else:
                stack.append(int(token))
        return stack.pop()