class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            nums1,nums2 = nums2,nums1
        
        start = 0
        end = len(nums1)
        total = (len(nums1)+ len(nums2))
        half = (total+1)//2

        while start <= end:
            mid = start + (end-start)//2

            i = mid
            j = half-i

            A_left = nums1[i-1] if i>0 else float('-inf')
            A_right= nums1[i] if i<len(nums1) else float('inf')
            B_left = nums2[j-1] if j>0 else float('-inf')
            B_right =nums2[j] if j<len(nums2) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total%2 == 1:
                    return (max(A_left,B_left))
                else:
                    return (max(A_left,B_left)+min(A_right,B_right))/2.0
            elif A_left> B_right:
                end = i-1
            else: 
                start = i+1