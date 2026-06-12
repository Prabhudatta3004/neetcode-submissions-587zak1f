class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(start,path):
            nonlocal k
            nonlocal n
            if len(path) == k:
                res.append(path[:])
            
            for idx in range(start,n+1):

                path.append(idx)
                dfs(idx+1,path)
                path.pop()
        dfs(1,[])
        return res
