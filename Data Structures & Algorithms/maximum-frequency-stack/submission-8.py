class FreqStack:

    def __init__(self):
        self.freqmap = defaultdict(int) ## for each element freq_map
        self.maxfreq = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.freqmap[val] +=1
        
        if self.freqmap[val] > self.max_count:
            self.max_count = self.freqmap[val]
        
        self.maxfreq[self.freqmap[val]].append(val)
        

    def pop(self) -> int:

        max_list = self.maxfreq[self.max_count]

        val = max_list.pop()

        self.freqmap[val] -=1

        if not max_list:
            self.max_count -=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()