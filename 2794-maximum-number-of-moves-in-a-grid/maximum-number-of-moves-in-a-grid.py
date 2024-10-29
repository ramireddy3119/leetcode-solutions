class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = set(range(m))  
        for j in range(n - 1):
            next_set = set()
            for i in q:
                for k in (i - 1, i, i + 1): 
                    if 0 <= k < m and grid[i][j] < grid[k][j + 1]:
                        next_set.add(k)
            if not next_set:
                return j 
            q = next_set
        return n - 1  
