class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #intuition is to push when we encounter a number
        ## Pop twice for binary operation based on the operand
        ## always push the result as a result of which we can easily 
        ## do the operation

        res = 0
        stack = []
        for n in tokens:
            if n == "+":
                res  = stack.pop() + stack.pop()
                stack.append(res)
            elif n == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(float(b/a))
                stack.append(res)
            else:
                stack.append(int(n))
        return stack[0]