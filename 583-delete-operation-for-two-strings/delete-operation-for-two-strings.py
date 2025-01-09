class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for ind1 in range(1,m+1):
            for ind2 in range(1,n+1):
                if word1[ind1-1] == word2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]= max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        val = dp[m][n]
        return (m-val)+(n-val)
        