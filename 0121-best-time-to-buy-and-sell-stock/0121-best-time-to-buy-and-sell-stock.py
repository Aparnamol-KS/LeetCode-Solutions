class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_profit = 0
        for price in prices:
            if(price < min_price):
                min_price = price
            else:
                pro = price - min_price
                max_profit = max(max_profit,pro)
        return max_profit


