class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for string in strs:
            freq_map = [0]*26
            for ch in string:
                freq_map[ord(ch)-ord("a")] +=1
            if tuple(freq_map) in lookup:
                lookup[tuple(freq_map)].append(string)
            else:
                lookup[tuple(freq_map)] = [string]
        
        res = []
        for idx,val in lookup.items():
            res.append(val)
        return res