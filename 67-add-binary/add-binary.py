class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a,2)
        n2 = int(b,2)
        total = n1 + n2
        res = bin(total)
        return res[2:]
        