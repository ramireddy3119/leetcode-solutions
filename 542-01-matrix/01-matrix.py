from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        dist = [[-1] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))  
                    dist[i][j] = 0 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = d + 1
                    queue.append((nr, nc, d + 1))

        return dist
