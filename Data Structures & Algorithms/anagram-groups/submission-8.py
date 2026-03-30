class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for word in strs:
            freq_map = [0] * 26
            for ch in word:
                freq_map[ord(ch)-ord('a')] +=1
            
            lookup[tuple(freq_map)].append(word)

        res = []
        for key,val in lookup.items():
            res.append(val)
        return res