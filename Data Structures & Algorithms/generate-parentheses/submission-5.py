class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path,opened,closed):
            if opened == closed == n:
                res.append(''.join(path))
                return
            if opened<n:
                path.append("(")
                dfs(path,opened+1,closed)
                path.pop()
            if closed<opened:
                path.append(")")
                dfs(path,opened,closed+1)
                path.pop()
        dfs([],0,0)
        return res