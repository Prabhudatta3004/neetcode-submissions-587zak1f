class Solution:
    def simplifyPath(self, path: str) -> str:
        path_elements = path.split('/')

        res = []

        for ele in path_elements:
            if ele == "..":
                if res:
                    res.pop()
            elif ele not in ["",".",".."]:
                res.append(ele)
        return "/" + "/".join(res)