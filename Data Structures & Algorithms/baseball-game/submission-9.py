class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            elif ops == "D" and len(stack) >= 1:
                stack.append(2*stack[-1])
            elif ops == "C" and len(stack) >= 1:
                stack.pop()
            else:
                stack.append(int(ops))
        return sum(stack)
