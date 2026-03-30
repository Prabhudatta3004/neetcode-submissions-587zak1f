class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_a = {}
        hash_b = {}

        ## Storing the values for s

        for i in s:
            if i not in hash_a:
                hash_a[i] = 1
            else:
                hash_a[i] +=1

        for i in t:
            if i not in hash_b:
                hash_b[i] = 1
            else:
                hash_b[i] +=1

        return (hash_a == hash_b)