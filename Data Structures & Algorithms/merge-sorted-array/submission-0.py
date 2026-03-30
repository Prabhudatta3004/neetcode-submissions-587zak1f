class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        temp1, temp2 = 0, 0

        while temp1 < m and temp2 < n:
            if nums1[temp1] <= nums2[temp2]:
                res.append(nums1[temp1])
                temp1 += 1
            else:
                res.append(nums2[temp2])
                temp2 += 1

        if temp1 < m:
            res.extend(nums1[temp1:m])
        if temp2 < n:
            res.extend(nums2[temp2:n])

        nums1[:] = res
