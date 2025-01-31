from typing import List

class Solution:
    def __init__(self):
        self.dir = [-1, 0, 1, 0, -1]

    def isValid(self, n: int, x: int, y: int) -> bool:
        return 0 <= x < n and 0 <= y < n

    def markIsland(self, grid: List[List[int]], island_number: int, n: int, x: int, y: int) -> int:
        grid[x][y] = island_number
        count = 1
        for i in range(4):
            newX = x + self.dir[i]
            newY = y + self.dir[i + 1]
            if self.isValid(n, newX, newY) and grid[newX][newY] == 1:
                count += self.markIsland(grid, island_number, n, newX, newY)
        return count

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_size = {}
        island_number = 2

        # Mark islands
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    island = self.markIsland(grid, island_number, n, x, y)
                    island_size[island_number] = island
                    island_number += 1

        # Try to convert each 0 to 1 one by one
        max_size = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    islands = set()
                    for i in range(4):
                        newX = x + self.dir[i]
                        newY = y + self.dir[i + 1]
                        if self.isValid(n, newX, newY):
                            islands.add(grid[newX][newY])
                    # Iterate and find total size of current island
                    curr_island = 1
                    for key in islands:
                        curr_island += island_size.get(key, 0)
                    max_size = max(max_size, curr_island)

        return max_size if max_size != 0 else n * n