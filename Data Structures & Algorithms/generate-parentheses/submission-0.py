class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN,closeN):
            ## Base condition since we get all the
            ## required combinations at the leaf nodes
            if openN==closeN==n:
                res.append(''.join(stack))
                return
            
            ## for open brackets

            if openN < n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()

            ## For closed brackets
            if closeN< openN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res