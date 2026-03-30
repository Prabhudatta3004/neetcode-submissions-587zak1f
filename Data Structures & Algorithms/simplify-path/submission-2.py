class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split("/")
        ##print(elements)
        stack = []

        for ele in elements:
            if ele == "..":
                if stack:
                    stack.pop()
            elif ele not in [".","..",""]:
                stack.append(ele)
        return "/" + "/".join(stack)