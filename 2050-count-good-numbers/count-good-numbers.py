class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        def binaryExp(a,b):
            res = 1
            while b:
                if b & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return res
        return (binaryExp(4,n//2)*binaryExp(5,n-n//2))%MOD
        