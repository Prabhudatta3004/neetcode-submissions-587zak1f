class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        largest=0
        count = 0
        for n in nums:
            if n not in hashset:
                hashset.add(n)
        
        for n in nums:
            if n-1 not in hashset:
                count = 1
                while n+count in hashset:
                    count +=1
            largest = max(count,largest)
        return largest