class Solution:
    def getNumber(self,n):
        summ = 0
        while n > 0:
            digit = n % 10
            summ += digit * digit
            n //= 10
        return summ 
    def isHappy(self, n: int) -> bool:
        mapp  = set()
        while n != 1 and n not in mapp:
            mapp.add(n)
            n = self.getNumber(n)
        return n == 1

    