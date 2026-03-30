class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        col_0 = False
        rows = len(matrix)
        cols = len(matrix[0])
        ## i need to check for the first row
        ## if my first row is 0 i will mark matrix[r][0]
        for r in range(rows):
            if matrix[r][0] == 0:
                col_0 = True
            for c in range(1,cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
        if col_0:
            for r in range(rows):
                matrix[r][0] = 0