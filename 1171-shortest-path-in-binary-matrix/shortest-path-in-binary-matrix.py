class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return -1
        queue = deque([(0,0,1)])
        visited = [[float('inf')]*cols for _ in range(rows)]
        end = (rows-1,cols-1)
        visited[0][0] = 1
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1) 
        ]

        while queue:
            r,c,dist = queue.popleft()
            if (r,c) == end:
                return visited[r][c]
            for dr,dc in directions:
                nr,nc = r + dr ,c + dc
                if 0 <= nr < rows and 0 <= nc < cols and  visited[nr][nc] == float('inf') and grid[nr][nc] != 1:
                    visited[nr][nc] = dist + 1
                    queue.append((nr,nc,dist+1))
        return -1
        