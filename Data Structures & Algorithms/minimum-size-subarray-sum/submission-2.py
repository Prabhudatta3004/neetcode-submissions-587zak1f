import math
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_count = math.inf

        left,right = 0,0
        subarray_sum = 0
        while right<len(nums):
            subarray_sum += nums[right]
            right +=1
            
            while subarray_sum>=target:
                min_count = min(min_count, right-left)
                subarray_sum -= nums[left]
                left +=1 
        return min_count if min_count != math.inf else 0