class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left_small = [-1] * n
        right_small = [n] * n
        stack = []

        # Find nearest smaller to the left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_small[i] = stack[-1]
            stack.append(i)

        stack = [] # Clear stack for the next pass

        # Find nearest smaller to the right
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_small[i] = stack[-1]
            stack.append(i)

        # Calculate max area
        max_area = 0
        for i in range(n):
            width = right_small[i] - left_small[i] - 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area