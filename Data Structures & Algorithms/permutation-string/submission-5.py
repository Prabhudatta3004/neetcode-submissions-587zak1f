class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_map=[0]*26

        for ch in s1:
            s1_freq_map[ord(ch)-ord('a')] +=1
        
        s2_freq_map=[0]*26

        start = end = 0

        while end<len(s2):
            s2_freq_map[ord(s2[end])-ord('a')] +=1
            end +=1

            if end-start == len(s1):
                if s1_freq_map == s2_freq_map:
                    return True
                
                s2_freq_map[ord(s2[start])-ord('a')] -=1
                start +=1
        return False