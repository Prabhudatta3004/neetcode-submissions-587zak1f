class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        targets = set(s)

        max_count = 0

        for target in targets:
            start = end = 0
            count = 0

            while end<len(s):
                if s[end] != target:
                    count +=1
                end +=1

                while count > k:
                    if s[start] != target:
                        count -=1
                    start +=1
                
                max_count = max(max_count, end-start)
        return max_count