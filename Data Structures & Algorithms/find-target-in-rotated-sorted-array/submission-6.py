class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start,end):
            while start <=end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        def min_ele(start,end):
            while start < end:
                mid = start + (end-start)//2
                if nums[mid] > nums[end]:
                    start = mid + 1
                elif nums[mid] <= nums[end]:
                    end = mid
            return end
        
        min_idx = min_ele(0,len(nums)-1)
        ans1 = binary_search(0,min_idx-1)
        ans2 = binary_search(min_idx,len(nums)-1)

        return max(ans1,ans2)