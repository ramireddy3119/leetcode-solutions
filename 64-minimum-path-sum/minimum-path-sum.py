class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return float('inf')
            if i == r-1 and j == c-1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            up = grid[i][j] + dfs(i+1,j)
            down = grid[i][j] + dfs(i,j+1) 
            memo[(i,j)] = min(up,down)
            return memo[(i,j)]
        r = len(grid)
        c = len(grid[0])
        memo = {}
        return dfs(0,0)

        