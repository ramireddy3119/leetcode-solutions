class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min = -2**31 
        max = 2**31-1
        if dividend == divisor:
            return 1
        sign = True
        if dividend >= 0 and divisor < 0: sign = False
        if dividend <= 0 and divisor > 0: sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while(n >= d):
            cnt = 0
            while(n >= (d<<(cnt+1))):
                cnt += 1
            ans += 1<<cnt
            n-=(d<<cnt)
        
        if ans == 1<<31 and sign:
            return max
        if ans == (1<<31) and not sign:
            return min
        return ans if sign else -ans