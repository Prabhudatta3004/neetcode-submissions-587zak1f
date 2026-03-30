class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_element = path.split('/')

        for ele in path_element:
            if stack and ele == ".." :
                stack.pop()
            elif ele not in ['.','..',""]:
                stack.append(ele)
        
        return "/" + "/".join(stack)