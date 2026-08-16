class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        candidate = end
        def divides_to_k(max_sum):
            count = 1
            subarray_sum = 0

            for num in nums:
                if subarray_sum + num > max_sum:
                    count +=1
                    subarray_sum = num
                else:
                    subarray_sum +=num
            return count <= k
        
        while start <= end:
            mid = start + (end-start)//2

            if divides_to_k(mid):
                candidate = mid
                end = mid-1
            else:
                start = mid+1
        return candidate