class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_lookup = defaultdict(list) ## freqmap: words

        for s in strs:
            freq = [0]*26

            for ch in s:
                freq[ord(ch)-ord('a')] +=1
            anagram_lookup[tuple(freq)].append(s)
            ## this will either create a new entry or append
        res = []

        for words in anagram_lookup.values():
            res.append(words)
        return res
