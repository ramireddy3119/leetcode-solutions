class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = 0
        zeros = 0
        maxi = 0
        for i in s:
            if i == '1':
                ones += 1
        for i in range(n-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            maxi = max(maxi, ones + zeros)
        return maxi
        

        