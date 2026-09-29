class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start,path):
            nonlocal k,n
            if len(path) == k:
                res.append(path[:])
                return 
            
            for idx in range(start,n+1):
                path.append(idx)
                backtrack(idx+1,path)
                path.pop()
        backtrack(1,[])
        return res