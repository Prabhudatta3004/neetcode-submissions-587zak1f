class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        smaller_left = [-1] * len(heights)
        smaller_right = [len(heights)] * len(heights)
        stack =[]
        ## find smaller towards left
        for idx in range(len(heights)):
            while stack and stack[-1][1] >= heights[idx]:
                stack.pop()
            if stack:
                smaller_left[idx] = stack[-1][0]
            stack.append([idx,heights[idx]])
        stack = []
        ## find smaller towards right
        for idx in range(len(heights)-1,-1,-1):
            while stack and stack[-1][1] >= heights[idx]:
                stack.pop()
            if stack:
                smaller_right[idx] = stack[-1][0]
            stack.append([idx,heights[idx]])
        
        for idx in range(len(heights)):
            area = heights[idx] * (smaller_right[idx] - smaller_left[idx]-1)
            max_area = max(max_area,area)
        return max_area