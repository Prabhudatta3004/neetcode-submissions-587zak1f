class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## freq map for s1:

        freq1 = [0]*26

        for ch in s1:
            freq1[ord(ch)-ord('a')] +=1

        
        freq2 = [0]*26

        start,end = 0,0
        window_size = 0
        while end<len(s2):
            freq2[ord(s2[end]) - ord('a')] +=1
            end +=1 
            window_size +=1

            if window_size == len(s1):
                if freq1 == freq2:
                    return True
                
                freq2[ord(s2[start]) - ord('a')] -=1
                start +=1
                window_size -=1
        return False