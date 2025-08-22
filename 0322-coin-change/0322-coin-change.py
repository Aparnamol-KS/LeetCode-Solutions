from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount

        # dp[i][j] = min coins needed to make sum j using first i coins
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # Base case: 0 coins needed to make sum 0
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]   # can't take this coin
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])  

        return -1 if dp[m][n] == float('inf') else dp[m][n]
