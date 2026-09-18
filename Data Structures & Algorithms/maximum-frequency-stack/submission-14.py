class FreqStack:

    def __init__(self):
        self.lookup = defaultdict(int)## per node count
        self.freq = defaultdict(list) ## freq-> list of vals
        self.max_freq = float('-inf')

    def push(self, val: int) -> None:
        self.lookup[val] += 1
        if self.lookup[val]>self.max_freq:
            self.max_freq = self.lookup[val]
        self.freq[self.lookup[val]].append(val)

    def pop(self) -> int:
        val = self.freq[self.max_freq].pop()
        if not self.freq[self.max_freq]:
            self.max_freq -=1
        self.lookup[val] -=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()