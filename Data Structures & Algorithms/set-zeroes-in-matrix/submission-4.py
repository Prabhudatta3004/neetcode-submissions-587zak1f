class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col= False
        
        for row in range(0,len(matrix)):
            if matrix[row][0] == 0:
                first_col = True
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col]==0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col:
            for r in range(len(matrix)):
                matrix[r][0] = 0

