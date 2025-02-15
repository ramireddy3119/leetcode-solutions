class Solution:
    def isValid(self, sq: str, pos: int, sum_val: int, val: int) -> bool:
        if pos >= len(sq):
            return sum_val == val
        
        for i in range(len(sq) - pos):
            curr_val = int(sq[pos:pos + i + 1])
            if self.isValid(sq, pos + i + 1, sum_val + curr_val, val):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_number = 1
        for i in range(2, n + 1):
            sq = str(i * i)
            if self.isValid(sq, 0, 0, i):
                punishment_number += i * i
        return punishment_number