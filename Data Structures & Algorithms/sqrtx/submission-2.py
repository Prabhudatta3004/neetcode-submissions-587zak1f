class Solution:
    def mySqrt(self, x: int) -> int:
        ## positive numbers 
        ## Root of a number is basically reducing the number's power
        ## So since this is a non-negative number 1-n and we need to find
        ## the number
        if x == 0:
            return 0
        for i in range(1,x+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
                break

        ## TC: O(N)

    ## BINARY SEARCH

        start = 1
        end = x
        while start<=end:
            mid = start + (end-start)//2
            if mid*mid > x:
                end = mid-1
            elif mid*mid < x:
                start = mid+1
                return mid
            else:
                return mid
            