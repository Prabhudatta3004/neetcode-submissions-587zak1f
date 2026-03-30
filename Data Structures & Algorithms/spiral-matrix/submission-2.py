class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res = []
        while left<=right and top<=bottom:

            ## loop for left to right

            for i in range(left,right+1):
                res.append(matrix[top][i])
            top +=1

            ## loop from top to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -=1

            ## Now I need to check for row matrix or col matrix
            ## before I operate further

            if not left<=right or not top<=bottom:
                break
            
            # now from right to left starting from bottom

            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom -=1

            ## from bottom to top
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left +=1
        return res