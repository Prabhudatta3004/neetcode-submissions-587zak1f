class Solution:
    def isValid(self, s: str) -> bool:
        ## My idea is we can have a reader hashmap
        ## that can store closed as key and open as value
        ## We can push all open brackets into stack
        ## if we encounter a closed bracket we pop and we 
        ## check if it exists in the hashmap if not return false

        lookup ={")":"(", "}":"{", "]":"["}
        stack = []
        for string in s:
            if string in lookup:
                if stack and stack[-1] == lookup[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
            
        return True if not stack else  False