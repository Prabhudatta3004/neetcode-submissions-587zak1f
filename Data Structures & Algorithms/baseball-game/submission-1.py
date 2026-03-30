class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == "+":
                stack.append(stack[-1]+stack[-2])
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(ops))
        final_sum = 0
        while stack:
            final_sum += stack.pop()
        return final_sum