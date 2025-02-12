class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0] * len(prices) for _ in range(3)]
        
        for k in range(1, 3):
            maxDiff = -prices[0]
            for j in range(1, len(prices)):
                dp[k][j] = max(dp[k][j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[k-1][j] - prices[j])
        
        return dp[2][-1]
