class Solution:
    def maxProfit(self,k, prices):
        if not prices:
            return 0

        n = len(prices)

        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            maxDiff = -prices[0] 
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]

        