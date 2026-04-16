class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1

        while start <= end:
            mid = start+ (end-start)//2

            if target > matrix[mid][-1]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                break
        mid_row = mid
        start = 0
        end =len (matrix[0]) - 1

        while start <= end:
            mid = start + (end-start)//2

            if matrix[mid_row][mid] == target:
                return  True
            elif  matrix[mid_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
        
