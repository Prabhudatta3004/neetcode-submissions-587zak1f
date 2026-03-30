class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## we need to make sure that when the closed and 
        ## open count are same as the given n , we store the state
        ## else we can increase open brackets as long as they are less
        # than the n, and the closed count should always be less than the
        ## open count

        res =[]
        def backtrack(path,closed,opened):
            if opened == closed == n:
                res.append("".join(path))
                return
            if opened<n:
                path.append("(")
                backtrack(path,closed,opened+1)
                path.pop()
            if closed<opened:
                path.append(")")
                backtrack(path,closed+1,opened)
                path.pop()
        backtrack([],0,0)

        return res
