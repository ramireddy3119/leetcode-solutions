class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        count = 1
        for i in range(len(s)):
            if i > 0:
                if s[i-1] == s[i]:
                    count += 1
                else:
                    count = 1
            if count < 3:
                res += s[i]
                
        return res
