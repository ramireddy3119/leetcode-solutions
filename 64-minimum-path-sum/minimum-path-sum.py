class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = {}
        def minPath(i,j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            if (i,j) in dp:
                return dp[(i,j)]
            up = grid[i][j] + minPath(i-1,j)
            left = grid[i][j] + minPath(i,j-1)
            
            dp[(i,j)] = min(up,left)
            return dp[(i,j)]
        return minPath(rows-1,cols-1)