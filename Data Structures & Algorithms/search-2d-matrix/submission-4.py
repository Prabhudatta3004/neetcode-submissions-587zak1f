class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## first thing we need to find the mid_row 
        ## that has the element

        top_row = 0
        bottom_row = len(matrix)-1

        while top_row<=bottom_row:
            mid_row = top_row + (bottom_row-top_row)//2

            if target> matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target< matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else:
                break
        
        ## we got the mid row, now we can search the element in
        ## the mid_row

        start = 0
        end = len(matrix[0])-1

        while start<=end:
            mid = start + (end-start)//2

            if target < matrix[mid_row][mid]:
                end = mid - 1
            elif target > matrix[mid_row][mid]:
                start = mid + 1
            else:
                return True
        return False