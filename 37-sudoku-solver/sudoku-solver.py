class Solution:
    def solveSudoku(self, mat):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets and collect empty cell positions
        for i in range(9):
            for j in range(9):
                if mat[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = mat[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def solve(index):
            if index == len(empty_cells):  # If all empty cells are filled, Sudoku is solved
                return True

            row, col = empty_cells[index]
            box_id = (row // 3) * 3 + (col // 3)

            for num in range(1, 10):
                num = str(num)
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_id]:
                    # Place the number
                    mat[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_id].add(num)

                    if solve(index + 1):  # Solve next empty cell
                        return True

                    # Backtrack
                    mat[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_id].remove(num)

            return False  # No valid number found, trigger backtracking

        solve(0)
