class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ## -A---B--------C--------Destination
        
        aggregated = [(p,s) for p,s in zip(position,speed)]
        aggregated.sort(reverse = True)

        ## C------B-------A
        stack = []
        for p,s in aggregated:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)