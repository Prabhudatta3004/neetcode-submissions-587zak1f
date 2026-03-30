class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## i will start two pointers from the start
        ## start will be fixed for comparison
        ## end keeps on movinf to give me good deals
        ## now when I move end I can check if value in end-value is
        ## > start then we increment j and keep checking
        ## if not we we return the value taht we stored as max profit


        max_profit = 0
        start,end = 0,0
        while end< len(prices):
            if prices[end] > prices[start]:
                max_profit = max(max_profit,prices[end]-prices[start])
            
            else:
                start = end
            
            end +=1
        return max_profit
