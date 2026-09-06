class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix)-1

        while left<right:
            top = left
            bottom = right

            for i in range(right-left):
                topleft = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]
                
                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] = topleft
            
            left +=1
            right -=1