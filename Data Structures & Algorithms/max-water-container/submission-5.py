class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_area = 0
        while start < end:
            height = min(heights[start],heights[end])
            area = height * (end-start)
            max_area = max(max_area,area)
            if heights[start] < heights[end]:
                start +=1
            else:
                end -=1
        return max_area