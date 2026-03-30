class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ## we can use a stack to just keep all the elements

        ## we have 3 different operations that can be performed
        stack = []
        for i in range(len(operations)):
            if stack and operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif stack and operations[i] == "C":
                stack.pop()
            elif stack and operations[i] == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(operations[i]))
        return sum(stack)