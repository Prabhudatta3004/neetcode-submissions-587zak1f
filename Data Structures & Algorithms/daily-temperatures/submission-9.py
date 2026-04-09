class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for idx in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][0] <= temperatures[idx]:
                stack.pop()
            res[idx] = (stack[-1][1] - idx) if stack else 0
            stack.append([temperatures[idx],idx])
        return res