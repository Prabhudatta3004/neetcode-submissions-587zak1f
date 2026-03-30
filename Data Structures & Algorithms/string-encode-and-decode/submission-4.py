class Solution:

    def encode(self, strs: List[str]) -> str:
        super_string = ""
        '''my string : len + # + string'''
        for st in strs:
            super_string += str(len(st)) + "#" + st
        return super_string
    def decode(self, s: str) -> List[str]:
        '''How shall we decode : lets read the string;
        the first element is our number in string format
        convert that back to number move to start of the string
        marked by special character: one loop to get the length
        then we can just add the number to slice the string'''

        start, end = 0,0
        res = []
        while end < len(s):
            start = end
            while s[end] != "#":
                end +=1
            length = s[start:end]
            length = int(length)
            start = end + 1
            end = start + length
            res.append(s[start:end])
            start = end
        return res
            


            