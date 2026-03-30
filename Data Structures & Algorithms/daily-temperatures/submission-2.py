class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## we need to check greater element to the right
        ## we can iterate from right to left
        ## We can store two things values and indices
        ## we need to check the values for greater towards right
        ## store result as the difference between the indices

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1,-1,-1):
            ## first we check if the stack exists and then stack top value
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            ## after removing all less elements we might have
            ## a greater element or we might not
            ## if we dont have a greater element we already intiated the 
            ##result with 0 if not we store the difference between
            ## ith index and the stack tops index
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result