from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        window_lookup = {}

        start = end = 0
        min_val = float('inf')
        min_start = 0
        checklist = 0
        while end < len(s):
            window_lookup[s[end]] = window_lookup.get(s[end],0) + 1

            if s[end] in lookup and window_lookup[s[end]] == lookup[s[end]]:
                checklist +=1
            end +=1
            
            while checklist == len(lookup):
                if end-start < min_val:
                    min_val = (end-start)
                    min_start = start

                window_lookup[s[start]] -=1
                if s[start] in lookup and window_lookup[s[start]] < lookup[s[start]]:
                    checklist -=1
                start +=1
                
        if min_val == float('inf'):
            return ""
        
        return s[min_start:min_start+min_val]



