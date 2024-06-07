# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = prices[0]
        for price in prices[1:]:
            if price<prev:
                prev = price
            else:
                res+= price-prev
                prev = price
        return res