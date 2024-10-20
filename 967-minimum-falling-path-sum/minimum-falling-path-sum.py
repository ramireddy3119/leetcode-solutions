class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = {} 
        def minFall(i, j):
            
            if j < 0 or j >= n:
                return float('inf')

            if i == 0:
                return matrix[0][j]
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            up = matrix[i][j] + minFall(i - 1, j)
            left_diag = matrix[i][j] + minFall(i - 1, j - 1)
            right_diag = matrix[i][j] + minFall(i - 1, j + 1)
            
            dp[(i, j)] = min(up, left_diag, right_diag)
            return dp[(i, j)]

        return min(minFall(n - 1, j) for j in range(n))
