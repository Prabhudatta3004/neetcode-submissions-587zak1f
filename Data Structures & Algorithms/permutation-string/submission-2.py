class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_hashmap = {}

        for ch in s1:
            if ch not in s1_hashmap:
                s1_hashmap[ch] = 0
            s1_hashmap[ch] +=1
        
        left,right = 0,0

        s2_hashmap = {}
        window_size = 0
        while right< len(s2):
            
            ## update the hashmap
            ## increment the window size
            ## increment the right pointer

            if s2[right] not in s2_hashmap:
                s2_hashmap[s2[right]] = 0
            s2_hashmap[s2[right]] += 1
            window_size += 1
            right +=1

            if window_size == len(s1):
                if s2_hashmap == s1_hashmap:
                    return True
                
                window_size -= 1
                s2_hashmap[s2[left]] -= 1
                if s2_hashmap[s2[left]] == 0:
                    del s2_hashmap[s2[left]]
                left +=1
        
        return False