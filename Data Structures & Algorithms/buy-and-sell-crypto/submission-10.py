class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_profit = 0

        while end<len(prices):
            if prices[end] < prices[start]:
                start = end
            profit = prices[end]-prices[start]
            max_profit = max(max_profit,profit)
            end +=1
        return max_profit