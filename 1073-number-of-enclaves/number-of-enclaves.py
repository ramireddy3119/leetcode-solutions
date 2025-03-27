class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != 1:
                return
            board[i][j] = '#'  # Mark as visited
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:  # Move in 4 directions
                dfs(i + x, j + y)

        rows, cols = len(board), len(board[0])

        # Start DFS from border 'O's
        for i in range(rows):
            if board[i][0] == 1:
                dfs(i, 0)
            if board[i][cols - 1] == 1:
                dfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == 1:
                dfs(0, j)
            if board[rows - 1][j] == 1:
                dfs(rows - 1, j)

        # Convert remaining 'O' to 'X' and '#' back to 'O'
        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    count += 1
        return count
        