class Solution:
    def countAndSay(self, n: int) -> str:
        def buildNextTerm(s):
            res = ""
            count = 1
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    res += str(count) + s[i-1]
                    count = 1
            res += str(count) + s[-1]
            return res
        ans = "1"
        for i in range(1,n):
            ans = buildNextTerm(ans)
        return ans