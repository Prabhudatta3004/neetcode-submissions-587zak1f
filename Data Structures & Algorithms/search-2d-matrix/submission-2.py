class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## I need to find the row that will have the target

        ## I can compare the target with the mid_row's 1st element
        ## if the target is less. it is likely that this is the row
        ## if not if target > mid_row{last value} ## I need to bring
        ## top row to mid_row+1 and else bottom row comes up

        top_row = 0
        bottom_row = len(matrix)-1
        
        while top_row<=bottom_row:
            mid_row = (top_row+bottom_row)//2

            if target > matrix[mid_row][-1]:
                top_row = mid_row+1
            elif target<matrix[mid_row][0]:
                bottom_row = mid_row-1
            else:
                break
        
        row = mid_row
        start = 0
        end = len(matrix[0])-1

        while start<=end:
            mid = start + (end-start)//2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                start = mid + 1
            else:
                end = mid-1
        return False