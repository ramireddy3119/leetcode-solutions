class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        arr = [0]*len(s)
        for i in range(1,n-1):
            if s[i-1]  == s[i] and s[i] == s[i+1]:
                arr[i] = 1
        res = ""
        for i in range(n):
            if arr[i] == 0:
                res += s[i]
        return res


        