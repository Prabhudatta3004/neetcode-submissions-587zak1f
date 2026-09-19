class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        candidate = end
        def can_divide(largest_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum+num > largest_sum:
                    count +=1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k
        
        while start<=end:
            mid = start +(end-start)//2

            if can_divide(mid):
                candidate = mid
                end = mid-1
            else:
                start = mid+1
        return candidate