class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        start = end = 0

        def calculate_frequency_map (string):
            freq = [0]*26
            for c in string:
                freq[ord(c)-ord('a')] += 1
            return freq
        
        s1_freq = calculate_frequency_map (s1)
        k = len(s1)
        window_freq= [0]*26
        while end < len(s2):
            window_freq[ord(s2[end]) - ord('a')] +=1
            if end-start+1 < k:
                end +=1
            elif end-start+1 == k:
                if window_freq == s1_freq:
                    return True
                
                window_freq[ord(s2[start])-ord('a')] -=1
                start +=1
                end +=1
        return False