# 714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        hold = -prices[0]
        for price in prices[1:]:
            hold = max(hold, profit-price)
            profit = max(profit, hold+price-fee)
        return profit