class Solution:
    def simplifyPath(self, path: str) -> str:
        strings = path.split('/')
        stack = []

        for string in strings:
            if string == "..":
                if stack:
                    stack.pop()
            elif string not in ['','.','..']:
                stack.append(string)
        return "/" + "/".join(stack)