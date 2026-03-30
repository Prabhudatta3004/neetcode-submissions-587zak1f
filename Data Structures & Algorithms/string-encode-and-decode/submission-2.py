class Solution:

    def encode(self, strs: List[str]) -> str:
        mama_string = ""
        for s in strs:
            mama_string += str(len(s)) + "#" + s
        return mama_string
        
    def decode(self, s: str) -> List[str]:
        i= 0
        final_list = []

        while i<len(s):
            j=i 
            while s[j] !='#':
                j+=1
            length = int (s[i:j])
            i=j+1
            j= i+length
            final_list.append(s[i:j])
            i=j
        return final_list