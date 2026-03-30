class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        state = []
        def backtrack(openC, closeC):
            ## base condition
            if openC == closeC == n:
                res.append("".join(state))
                return

            ## for the open bracket 
            if openC<n:
                state.append("(")
                backtrack(openC+1,closeC)
                state.pop()

            ## for the close bracket

            if closeC<openC:
                state.append(")")
                backtrack(openC, closeC+1)
                state.pop()

        backtrack(0,0)
        return res