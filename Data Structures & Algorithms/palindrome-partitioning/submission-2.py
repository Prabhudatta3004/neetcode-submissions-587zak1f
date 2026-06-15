class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(substring):
            return substring == substring[::-1]
        def dfs(start,path):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start,len(s)):
                substring = s[start:end+1]
                if is_palindrome(substring):
                    path.append(s[start:end+1])
                    dfs(end+1,path)
                    path.pop()
        dfs(0,[])
        return res