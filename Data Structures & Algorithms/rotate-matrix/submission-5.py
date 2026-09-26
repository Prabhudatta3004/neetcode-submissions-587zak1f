class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top_left = float('inf')

        left = 0
        right = len(matrix[0])-1

        while left<right:
            top = left
            bottom = right
            for idx in range(right-left):
                ## store top_left:
                top_left = matrix[top][left+idx]
                ## moving bottom_left to top left
                matrix[top][left+idx] = matrix[bottom-idx][left]
                ## moving bottom_rigth to bottom_left
                matrix[bottom-idx][left] = matrix[bottom][right-idx]
                ##moving top right to bottom right
                matrix[bottom][right-idx] = matrix[top+idx][right]
                ## moving top_left to top_right
                matrix[top+idx][right] = top_left
            left +=1
            right -=1
                