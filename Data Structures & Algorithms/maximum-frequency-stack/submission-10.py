class FreqStack:

    def __init__(self):
        self.count = {} ## per node counter
        self.lookup = {} ## count : [list of numbers having this count]
        self.max_val = 0 ## maximum value we have seen so far from where we can get the element
    def push(self, val: int) -> None:
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1
        
        self.max_val = max(self.max_val,self.count[val])

        if self.count[val] in self.lookup:
            self.lookup[self.count[val]].append(val)
        else:
            self.lookup[self.count[val]] = [val]

    def pop(self) -> int:
        val = self.lookup[self.max_val].pop()
        if not self.lookup[self.max_val]:
            self.max_val -=1
        self.count[val] -=1
        return val




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()