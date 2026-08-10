class Solution:

    def encode(self, strs: List[str]) -> str:
        master_str = ''
        for string in strs:
            master_str += str(len(string)) + "#" + string
        return master_str
    
    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            end = start

            while s[end] != '#':
                end +=1
            
            length = int(s[start:end])

            start = end + 1
            end = start + length
            res.append(s[start:end])
            start = end
        return res