class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        encoded_string = s
        start = end = 0
        while start < len(encoded_string):
            #end = start
            while encoded_string[end] !="#":
                end +=1
            length = int(s[start:end])

            start = end+1
            end = start + length
            res.append(encoded_string[start:end])
            start = end
        return res
