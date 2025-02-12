class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def find(ind,buy,cap):
            if ind == len(prices) or cap == 0:
                return 0
            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]
            if buy:
                m1 =  max(-prices[ind]+find(ind+1,0,cap),find(ind+1,1,cap))
            else:
                m1 =  max(prices[ind]+find(ind+1,1,cap-1),find(ind+1,0,cap))
            dp[ind][buy][cap] = m1
            return dp[ind][buy][cap]
        dp = [[[-1 for _ in range(3)]for _ in range(2)]for _ in range(len(prices))]
        return find(0,1,2)
        