class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[0])
        dp = {}
        def minTotal(i,j):
            if i == n-1:
                return triangle[n-1][j]
            # if j == m-1:
            #     return triangle[m-1][i]
            if (i,j) in dp:
                return dp[(i,j)]
            d = triangle[i][j] + minTotal(i+1,j)
            dg = triangle[i][j] + minTotal(i+1,j+1)
            dp[(i,j)] = min(d,dg)
            return dp[(i,j)]
        return minTotal(0,0)

        