# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = profit = 0
        for r in range(1,len(prices)):
            if prices[r]>=prices[l]:
                profit = max(profit, prices[r]-prices[l])
                r+=1
            else:
                l = r
                r+=1
        return profit