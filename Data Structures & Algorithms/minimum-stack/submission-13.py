class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack :
            self.stack.append((val,val))
        else:
            min_value = min(self.stack[-1][1],val)
            self.stack.append((val,min_value))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
