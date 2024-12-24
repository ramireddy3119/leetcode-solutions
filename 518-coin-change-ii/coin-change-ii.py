class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # def findWays(ind,tar):
        #     if ind == 0:
        #         return 1 if tar%coins[ind] == 0 else 0
        #     if dp[ind][tar] != -1:
        #         return dp[ind][tar]
        #     notTake = findWays(ind-1,tar)
        #     take = 0
        #     if coins[ind] <= tar:
        #         take = findWays(ind,tar-coins[ind])
        #     dp[ind][tar] = take+notTake
        #     return dp[ind][tar]
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            dp[0][i] = 1 if i%coins[0] == 0 else 0
        for ind in range(1,n):
            for tar in range(amount+1):
                notTaken = dp[ind-1][tar]
                take = 0
                if coins[ind] <= tar:
                    take = dp[ind][tar-coins[ind]]
                dp[ind][tar] = take + notTaken
        return dp[n-1][amount]
            
        
        