class MinStack:

    def __init__(self):
        self.stack = []
        self.minele = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minele = val
        elif val >= self.minele:
            self.stack.append(val)
        else:
            # Store encoded value and update minele
            self.stack.append(2 * val - self.minele)
            self.minele = val

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.minele:
            # Retrieve previous minele
            self.minele = 2 * self.minele - top

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        if top >= self.minele:
            return top
        else:
            return self.minele

    def getMin(self) -> int:
        return self.minele if self.stack else None
