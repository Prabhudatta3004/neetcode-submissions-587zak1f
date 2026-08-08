class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = [0]*26
        freq_map_t = [0]*26

        for ch in s:
            freq_map_s[ord(ch) - ord('a')] +=1
        for ch in t:
            freq_map_t[ord(ch)-ord('a')] +=1
        
        return freq_map_t == freq_map_s