from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)] 
        visited = set()
        visited.add((0, 0))

        results = {}
        points = 0
        
        sorted_queries = sorted(queries)
        index = 0 
        
        while index < len(sorted_queries):
            query = sorted_queries[index]

            while min_heap and min_heap[0][0] < query:
                val, r, c = heappop(min_heap)
                points += 1

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            
            results[query] = points
            index += 1

        return [results[q] for q in queries]
