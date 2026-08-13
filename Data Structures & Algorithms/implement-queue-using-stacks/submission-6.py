class MyQueue:
    def __init__(self):
        self.entry_stack = []
        self.exit_stack = []
    def push(self,x)-> None:
        self.entry_stack.append(x)
    def pop(self)-> int:
        if self.exit_stack:
            return self.exit_stack.pop()
        else:
            while self.entry_stack:
                self.exit_stack.append(self.entry_stack.pop())
            return self.exit_stack.pop()
    def peek(self)-> int:
        if self.exit_stack:
            return self.exit_stack[-1]
        else:
            while self.entry_stack:
                self.exit_stack.append(self.entry_stack.pop())
            return self.exit_stack[-1]
    def empty(self)-> bool:
        if not self.entry_stack and not self.exit_stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()