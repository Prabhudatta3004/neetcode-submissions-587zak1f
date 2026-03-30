class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0]*26
        for ch in s1:
            freq_s1[ord(ch)-ord("a")] +=1
        
        freq_s2 = [0]*26

        start = end = 0
        while end < len(s2):
            freq_s2[ord(s2[end])-ord('a')] +=1
            end +=1

            if end-start == len(s1):
                if freq_s1 == freq_s2 :
                    return True
                
                freq_s2[ord(s2[start]) - ord('a')] -=1
                start +=1
        return False