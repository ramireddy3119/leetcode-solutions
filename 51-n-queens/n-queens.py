class Solution:
    def solveNQueens(self, n: int):
        def isSafe(board, row, col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True
        
        def solve(board, row):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if isSafe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)
                    board[row] = -1 
        
        def print_solutions(solutions, n):
            result = []
            for sol in solutions:
                board = []
                for row in range(n):
                    row_str = ['.' for _ in range(n)]
                    row_str[sol[row]] = 'Q'
                    board.append("".join(row_str))
                result.append(board)
            return result
        res = []
        board = [-1] * n
        solve(board, 0)
        return print_solutions(res, n)

