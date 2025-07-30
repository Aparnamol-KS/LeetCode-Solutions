class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for i in range(len(prices)):
            sell = prices[i]
            profit = sell-buy
            ans = max(profit,ans)
            buy = min(buy,prices[i])
        return ans


