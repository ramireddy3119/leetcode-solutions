class Solution:
    def countGoodNumbers(self, n: int) -> int:
        a= (n+1)//2
        b=n//2
        mod = 10**9+7
        return pow(5,a,mod) *pow(4,b,mod)%mod
        
        