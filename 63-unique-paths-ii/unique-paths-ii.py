class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][col - 1] == 1:
            return 0
        dp =[[0 for _ in range(col)] for _ in range(rows)]
        dp[0][0] = 1
        for i in range(rows):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    continue
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[rows-1][col-1]

