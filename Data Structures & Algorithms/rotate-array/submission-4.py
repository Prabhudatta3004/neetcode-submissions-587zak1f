class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # Optimization: rotating by n is the same as not rotating at all
        k %= n 
        
        for _ in range(k):
            # 1. Save the last element
            previous = nums[n - 1]
            
            # 2. Shift all elements to the right by 1
            for i in range(n):
                # Swap current element with the 'previous' one
                nums[i], previous = previous, nums[i]