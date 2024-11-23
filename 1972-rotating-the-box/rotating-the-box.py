class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        matrix = [[box[j][i] for j in range(len(box))] for i in range(len(box[0]))]
        for row in matrix:
            row.reverse()
        
        def fall_stones(matrix):
            for col in range(len(matrix[0])):
                empty_row = len(matrix) - 1
                for row in reversed(range(len(matrix))):
                    if matrix[row][col] == '*':
                        empty_row = row - 1
                    elif matrix[row][col] == '#':
                        matrix[row][col], matrix[empty_row][col] = '.', '#'
                        empty_row -= 1
        
        fall_stones(matrix)
        
        return matrix

