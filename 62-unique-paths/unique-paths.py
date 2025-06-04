class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i,j,r,c,mat,memo):
            if i < 0 or i >= r or j < 0 or j >= c or mat[i][j] == 1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i == r-1 or j == c - 1:
                return 1
            memo[(i,j)]=dfs(i+1,j,r,c,mat,memo) + dfs(i,j+1,r,c,mat,memo)
            return memo[(i,j)]
        mat = [[0]*n for _ in range(m)]
        memo = {}
        print(mat)
        return dfs(0,0,m,n,mat,memo)
        