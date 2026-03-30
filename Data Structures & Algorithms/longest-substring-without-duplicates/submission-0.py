class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_set ={}
        start = end = 0
        maximum = 0
        while end < len(s):
            
            count_set[str(s[end])] = count_set.get(s[end], 0) + 1

            if (len(count_set) == (end-start+1)):
                maximum = max(maximum, end-start+1)
                end +=1
            elif (len(count_set)< (end-start+1)):
                while (len(count_set)< (end-start+1)):
                    count_set[s[start]] -=1
                    if count_set[s[start]] == 0:
                        del count_set[s[start]]
                    start +=1
                end +=1
        return maximum