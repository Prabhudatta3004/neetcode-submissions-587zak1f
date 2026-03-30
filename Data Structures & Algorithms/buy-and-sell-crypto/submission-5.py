class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 0

        max_profit = 0

        while right < len(prices):
            can_grow = prices[right] > prices[left]

            if can_grow:
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left = right
            
            right +=1
        return max_profit
        
