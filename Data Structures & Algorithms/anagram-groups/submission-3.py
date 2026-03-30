class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            lookup = [0] * 26 ## This the hash lookup for each string
            
            for i in s:
                    lookup[ord(i) - ord('a')] +=1
            res[tuple(lookup)].append(s)
        
        return list(res.values())
