class Solution:
    def romanToInt(self, s: str) -> int:
        mpp = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        prev = 0
        for i in s[::-1]:
            if mpp[i] >= prev:
                num += mpp[i]
            else: num -= mpp[i]
            prev = mpp[i]
        return num

        