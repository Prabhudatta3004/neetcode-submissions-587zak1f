class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = {} ## Taking this for the lookup of elements

        for num in nums:
            if num in val:
                return True
            val[num] = 1
        return False

