class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        tt = time//(n-1)
        return (time%(n-1)+1) if tt %2==0 else (n-time%(n-1))
        
        