class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res = []

        while top<=bottom and left<=right:
            ## left--right
            for idx in range(left, right+1):
                res.append(matrix[top][idx])
            top +=1

            ## top to down
            for idx in range(top,bottom+1):
                res.append(matrix[idx][right])
            right -=1

            if not(top<=bottom and left<=right):
                return res
            
            for idx in range(right,left-1,-1):
                res.append(matrix[bottom][idx])
            bottom -=1

            for idx in range(bottom,top-1,-1):
                res.append(matrix[idx][left])
            left +=1
        return res