class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def find(ind,buy):
            if ind == len(prices):
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy:
                m1 =  max(-prices[ind]+find(ind+1,0),find(ind+1,1))
            else:
                m1 =  max((prices[ind]+find(ind+1,1))-fee,find(ind+1,0))
            dp[ind][buy] = m1
            return dp[ind][buy]
        dp = [[-1 for _ in range(2)]for _ in range(len(prices))]
        return find(0,1)