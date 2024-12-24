class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def findWays(ind,tar):
            if ind == 0:
                return 1 if tar%coins[ind] == 0 else 0
            if dp[ind][tar] != -1:
                return dp[ind][tar]
            notTake = findWays(ind-1,tar)
            take = 0
            if coins[ind] <= tar:
                take = findWays(ind,tar-coins[ind])
            dp[ind][tar] = take+notTake
            return dp[ind][tar]
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        return findWays(len(coins)-1,amount)
            
        
        