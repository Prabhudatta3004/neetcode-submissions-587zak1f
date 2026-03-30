class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## for subgroups I think that their character frequency map 
        ## should be equal, then we can group them
        ## how to unpack that then

        character_frequency =[0] * 26 ## should be created for all strings
        ## after taht we can just append that string to this key
        ## but we need to pass this frequency map as key, to another list

        res = defaultdict(list)
        for s in strs:
            character_frequency = [0]*26
            for c in s:
                character_frequency[ord(c)-ord('a')] +=1
            
            res[tuple(character_frequency)].append(s)

        return list(res.values())