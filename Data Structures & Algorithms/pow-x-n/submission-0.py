class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n == 0:
                return 1
            if n<0: ## for roots
                return 1/pow(x,-n)
            
            if n%2 == 0:
                val = pow(x,n//2)
                return val * val
            else:
                return x * pow(x,n-1)
        return pow(x,n)