class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = [[p,s] for p, s in zip(position, speed)]
        stack =[]

        l.sort(reverse = True)

        for p,s in l:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)