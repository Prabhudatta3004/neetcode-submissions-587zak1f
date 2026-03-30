class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        left=[-1] * len(heights)
        right=[len(heights)] * len(heights)
        max_area = 0
        ## finding smaller element to the left
        stack= []

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            left[i]= stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        ## finding smaller element to the right
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right[i]= stack[-1] if stack else len(heights)
            stack.append(i)

        
        for i in range(len(heights)):
            width = right[i]-left[i]-1
            area = heights[i] * width
            max_area = max(max_area,area)

        return max_area
