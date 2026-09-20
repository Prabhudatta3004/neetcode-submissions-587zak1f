class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        for ch in s1:
            s1_freq[ord(ch)-ord('a')]+=1
        
        start = 0
        end = 0
        window_freq = [0]*26
        while end<len(s2):
            window_freq[ord(s2[end])-ord('a')]+=1
            end +=1

            if end-start == len(s1):
                if window_freq == s1_freq:
                    return True
                window_freq[ord(s2[start])-ord('a')]-=1
                start +=1
        return False
