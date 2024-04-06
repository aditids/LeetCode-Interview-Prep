# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = l = 0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit+=prices[r]-prices[l]
                l = r
            else:
                l+=1
        return profit 