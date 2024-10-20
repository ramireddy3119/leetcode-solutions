class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[0])
        dp = [[0 for _ in range(n)]for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(d,dg)
        return dp[0][0]


        