# 123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)   
        minPrices = [0]*n 
        maxPrices = [0]*n 
        minPrice = prices[0]
        maxPrice = prices[-1]
        profit = 0
        for i in range(1,n):
            minPrice = min(minPrice, prices[i])
            minPrices[i] = max(minPrices[i-1],prices[i]-minPrice)

        for i in range(n-2,-1,-1):
            maxPrice = max(maxPrice, prices[i])
            maxPrices[i] = max(maxPrices[i+1],maxPrice-prices[i])

        for i in range(n):
            profit = max(profit, minPrices[i]+maxPrices[i])
        
        return profit