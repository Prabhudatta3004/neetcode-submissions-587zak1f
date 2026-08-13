class MinStack:
    def __init__(self):
        self.minstack = []
    def push(self,val:int)->None:
        if not self.minstack:
            self.minstack.append((val,val))
        else:
            self.minstack.append((val,min(val,self.minstack[-1][1])))

    def pop(self)->None:
        self.minstack.pop()
    def top(self)->int:
        return self.minstack[-1][0]
    def getMin(self)->int:
        return self.minstack[-1][1]
    
