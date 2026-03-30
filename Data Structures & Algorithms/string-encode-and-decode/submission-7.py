class Solution:

    def encode(self, strs: List[str]) -> str:
        super_string = ""
        for s in strs:
            super_string += str(len(s)) + "#" + s
        return super_string
    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            end = start
            while s[end] != "#":
                end +=1
            
            length = int(s[start:end])
            start = end+1
            end = start+length
            res.append(s[start:end])
            start = end

        return res        
            