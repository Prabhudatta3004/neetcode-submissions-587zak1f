class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(stack)>=2 and token == "+":
                stack.append(stack.pop()+stack.pop())
            elif len(stack)>=2 and token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif len(stack)>=2 and token == "*":
                stack.append(stack.pop()*stack.pop())
            elif len(stack)>=2 and token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(token))
        return stack.pop()