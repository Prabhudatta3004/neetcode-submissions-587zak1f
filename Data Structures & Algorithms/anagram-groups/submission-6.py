class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## create a hashmap lookup
        ## {similar_score: [list of words]}

        lookup = defaultdict(list)

        for word in strs:
            freq_map = [0] * 26

            for ch in word:
                freq_map[ord(ch)-ord('a')] +=1
            lookup[tuple(freq_map)].append(word)
        
        res = []

        for _,word in lookup.items():
            res.append(word)
        
        return res