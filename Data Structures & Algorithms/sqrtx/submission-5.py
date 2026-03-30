class Solution:
    def mySqrt(self, x: int) -> int:
        ## positive numbers 
        ## Root of a number is basically reducing the number's power
        ## So since this is a non-negative number 1-n and we need to find
        ## the number
 
        ## TC: O(N)

    ## BINARY SEARCH

        start = 1
        end = x
        res = 0
        while start<=end:
            mid = start + (end-start)//2
            if mid*mid > x:
                end = mid-1
            elif mid*mid < x:
                start = mid+1
                res = mid
            else:
                return mid
        return res
            