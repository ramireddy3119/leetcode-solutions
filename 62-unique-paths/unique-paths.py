class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp ={}
        def noOfPaths(i,j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            left = noOfPaths(i,j-1)
            up = noOfPaths(i-1,j)
            dp[(i,j)] = left + up
            return dp[(i,j)]
        return noOfPaths(m-1,n-1)