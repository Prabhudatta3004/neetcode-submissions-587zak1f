class MinStack:

    def __init__(self):
        self.stack = []
        self.support_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.support_stack[-1] if self.support_stack else val)
        self.support_stack.append(val)

    def pop(self) -> None:
        self.support_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.support_stack[-1]
