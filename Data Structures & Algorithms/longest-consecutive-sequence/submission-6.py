class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)

        max_count = 0

        for num in nums:
            if num-1 not in lookup:
                count = 1
                while num+count in lookup:
                    count+=1
                max_count = max(max_count,count)

        return max_count