class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        candidate = end

        def max_sum(limit):
            cut = 1
            total_sum = 0
            for num in nums:
                if total_sum + num > limit:
                    cut +=1
                    total_sum = num
                else:
                    total_sum +=num
            return cut <= k
        
        while start <= end:
            mid = start + (end-start)//2
            if max_sum(mid):
                candidate = mid
                end = mid - 1
            else:
                start = mid + 1
        return candidate
