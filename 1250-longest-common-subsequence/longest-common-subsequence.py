class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def longsub(ind1,ind2):
            if ind1 < 0 or ind2 < 0:
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + longsub(ind1-1, ind2-1)
            else:
                dp[ind1][ind2]= max(longsub(ind1-1,ind2),longsub(ind1,ind2-1))
            return dp[ind1][ind2]
        return longsub(m-1,n-1)