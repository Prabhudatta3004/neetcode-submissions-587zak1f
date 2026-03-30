class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1 ##Input: x = 13 start = 1, end = 13
        end = x

        while start<=end:
            mid = start +(end-start)//2 ##mid = 5

            if mid*mid > x:   
                end = mid-1 ## end = 4, start = 4
            elif mid*mid < x:
                start = mid+1  
            else:
                return mid
        return end    ##        