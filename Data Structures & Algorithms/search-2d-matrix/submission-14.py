class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row= 0
        end_row = len(matrix)-1

        while start_row <= end_row:
            mid = start_row + (end_row-start_row)//2

            if matrix[mid][0]> target:
                end_row= mid-1
            elif matrix[mid][-1] < target:
                start_row = mid+1
            else:
                break
        mid_row = mid
        start = 0
        end = len(matrix[0])-1

        while start<=end:
            mid = start + (end-start)//2

            if matrix[mid_row][mid]>target:
                end = mid-1
            elif matrix[mid_row][mid]<target:
                start = mid+1
            else:
                return True
        return False