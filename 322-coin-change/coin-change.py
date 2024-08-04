class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        res = [n]*n
        res[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    res[i] = min(res[i],1+res[i-coins[j]])
        

        if res[amount] < amount + 1: return res[amount]
        return -1