from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i, j, r, c, mat, memo):
            if i < 0 or i >= r or j < 0 or j >= c or mat[i][j] == 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if i == r - 1 and j == c - 1:
                return 1
            memo[(i, j)] = dfs(i + 1, j, r, c, mat, memo) + dfs(i, j + 1, r, c, mat, memo)
            return memo[(i, j)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        return dfs(0, 0, m, n, obstacleGrid, memo)
