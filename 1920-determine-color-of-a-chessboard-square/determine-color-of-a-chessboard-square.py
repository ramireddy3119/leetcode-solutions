class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
      
        n = int(coordinates[1])
        if coordinates[0] == 'a':
            n += 1
        elif coordinates[0] == 'b':
            n += 2
        elif coordinates[0] == 'c':
            n += 3
        elif coordinates[0] == 'd':
            n += 4
        elif coordinates[0] == 'e':
            n += 5
        elif coordinates[0] == 'f':
            n += 6
        elif coordinates[0] == 'g':
            n += 7
        else:
            n += 8
        return n % 2 != 0
        