class Solution:

    def encode(self, strs: List[str]) -> str:
        super_string = ""
        for s in strs:
            super_string += str(len(s)) + "#" + s
        return super_string
    def decode(self, s: str) -> List[str]:
        ## we have got the superstring
        ## when we unpack , lets take a two pointers
        ## one pointer is a seeker of the delimiter
        ## when that pointer reaches the delimiter
        ## from start to end is the len(s)
        ## then we can move start to end+1
        ## and end = start+len(str)
        ## store superstring(start:end)
        ## then move start = end and repeate
        ## while end < len(super_string)

        start = 0
        res = []
        while start< len(s):
            end = start
            while s[end] != "#":
                end +=1
            
            length = int(s[start:end])
            start = end+1
            end = start+length
            res.append(s[start:end])
            start = end

        return res        
            