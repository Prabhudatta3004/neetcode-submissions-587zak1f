class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {} ## num:counter
        res = []
        for num in nums:
            count[num]= count.get(num,0) + 1
        
        for num,count in count.items():
            if count>math.floor(len(nums)//3):
                res.append(num)
        return res