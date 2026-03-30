class FreqStack:

    def __init__(self):
        self.freq_map = {} ## num:freq 
        self.group = {} ## freq:[] stack of nums
        self.max_freq = 0
    def push(self, val: int) -> None:
        curr_freq = self.freq_map.get(val,0) + 1
        self.freq_map[val] = curr_freq

        if curr_freq > self.max_freq:
            self.max_freq = curr_freq
        
        if curr_freq not in self.group:
            self.group[curr_freq] = []

        self.group[curr_freq].append(val)


    def pop(self) -> int:
        val = self.group[self.max_freq].pop()

        self.freq_map[val] -=1

        if not self.group[self.max_freq]:
            self.max_freq -=1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()