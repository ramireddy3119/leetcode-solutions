class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary = 0
        secondary = 0
        n = len(mat)

        for i in range(n):
            primary += mat[i][i]
            secondary += mat[i][n-i-1]
        if n % 2 == 1:
            center = mat[n // 2][n // 2]
            return primary + secondary - center

        return primary + secondary
        