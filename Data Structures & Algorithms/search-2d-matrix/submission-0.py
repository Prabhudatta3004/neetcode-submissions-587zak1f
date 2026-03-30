class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0])-1

        row_len = len(matrix)-1

        while(i>=0 and i<=row_len and j>=0 and j<len(matrix[0])):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -=1
            if matrix[i][j] < target:
                i += 1
        return False