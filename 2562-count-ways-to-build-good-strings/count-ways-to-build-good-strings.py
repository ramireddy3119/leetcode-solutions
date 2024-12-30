class Solution:
    def countGoodStrings(self,low, high, zero, one):
        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1 

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD

        return result
