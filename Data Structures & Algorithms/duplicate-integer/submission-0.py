class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for ele in nums:
            if ele in hashmap:
                return True
            hashmap[ele] = True       

        return False