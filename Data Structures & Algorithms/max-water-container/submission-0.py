class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        area = 0
        i=0
        j= len(heights)-1

        while i<j:
            area = (j-i) * min(heights[i], heights[j])

            if area > maxarea:
                maxarea = area
            if heights[i]<heights[j]:
                i +=1
            else:
                j -=1
        return maxarea