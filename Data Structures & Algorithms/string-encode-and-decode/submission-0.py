class Solution:

    def encode(self, strs: List[str]) -> str:
        ##Important to identify the smaller strings
        ##For Identification we have a method of adding the size
        ## as well as adding a hash to indicate the delimitier

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res= []
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i=j
        return res