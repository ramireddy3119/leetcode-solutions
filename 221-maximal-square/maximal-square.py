class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        max_square = float('-inf')

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if j == 0 or i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                max_square = max(max_square,dp[i][j])
        
        return max_square * max_square
        