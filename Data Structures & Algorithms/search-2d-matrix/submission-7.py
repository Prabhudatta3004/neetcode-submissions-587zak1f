class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid_row = start + (end-start)//2

            if matrix[mid_row][0] > target:
                end = mid_row - 1
            elif matrix[mid_row][-1] < target:
                start = mid_row + 1
            else :
                break
        
        start = 0
        end = len(matrix[0])-1

        while start <= end:
            mid = start + (end-start)//2

            if matrix[mid_row][mid] < target:
                start = mid+1
            elif matrix[mid_row][mid] > target:
                end = mid-1
            else:
                return True
        return False
        
            