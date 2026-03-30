class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        majority = math.floor(n//3)

        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] +=1


        for i in hashmap:
            if hashmap[i] > majority:
                result.append(i)
        
        return result