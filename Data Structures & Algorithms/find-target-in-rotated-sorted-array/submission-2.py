class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums,start,end,target):

            while start<=end:
                mid = start +(end-start)//2

                if  nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid+1
                else:
                    end = mid-1
            return -1

        def find_pivot(nums):
            start = 0
            end = len(nums)-1

            if nums[start]<= nums[end]:
                return start
            
            while start<=end:

                mid = start + (end-start)//2
                prev = (mid-1) % len(nums)
                nxt = (mid+1) % len(nums)
                if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                    return mid
                elif nums[mid]>nums[end]:
                    start = mid + 1
                else:
                    end = mid
            

        pivot = find_pivot(nums)
        first_half = binary_search(nums,0,pivot-1,target) 
        second_half = binary_search(nums,pivot,len(nums)-1,target)

        if first_half != -1:
            return first_half
        else:
            return second_half
