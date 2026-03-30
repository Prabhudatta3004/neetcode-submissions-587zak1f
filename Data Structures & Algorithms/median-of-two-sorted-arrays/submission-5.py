class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        total = len(nums1) + len(nums2)
        half = (total+1)//2
        left = 0
        right = len(nums1)

        while left<=right:
            mid = left + (right-left)//2
            i = mid
            j = half - i


            leftA = nums1[i-1] if i>0 else float('-inf')
            rightA = nums1[i] if i < len(nums1) else float("inf")
            leftB = nums2[j-1] if  j > 0 else float('-inf')
            rightB = nums2[j] if j < len(nums2) else float('inf')

            if leftA <= rightB and leftB<= rightA:
                if total%2 == 1:
                    return (max(leftA,leftB))        
                else:
                   return(max(leftA,leftB) + min(rightA,rightB))/2.0

            elif leftA > rightB:
                right = i - 1
            else:
                left = i + 1 
          
