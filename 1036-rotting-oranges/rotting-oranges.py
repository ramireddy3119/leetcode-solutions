from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = deque()
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        time = 0
        while queue:
            r,c,time = queue.popleft()
            for dx, dy in directions:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr,nc,time + 1))
        if fresh_count > 0:
            return -1
        return time

                    
                
        