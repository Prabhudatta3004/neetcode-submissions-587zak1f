class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:

        ## for decoding we need to unpack the entire
        ## big string into the smaller ones

        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i=j
        return res