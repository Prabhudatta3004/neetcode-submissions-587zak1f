class FreqStack:

    def __init__(self):
        self.freq_map = {} ## this will store val:freq
        self.group_map = {} ## freq: [elements]
        self.max_freq = 0

    def push(self, val: int) -> None:
        
        freq = self.freq_map.get(val,0) + 1
        self.freq_map[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq
        
        if freq not in self.group_map:
            self.group_map[freq] = []
        self.group_map[freq].append(val)


    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()

        self.freq_map[val] -=1

        if not self.group_map[self.max_freq]:
            self.max_freq -=1
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()