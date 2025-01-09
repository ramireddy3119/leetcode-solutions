class Solution:
    def minInsertions(self, s: str) -> int:
        def longestPalin(s1, s2):
            n = len(s1)
            m = len(s2)
            prev = [0] * (m + 1)
            for i in range(1, n + 1):
                curr = [0] * (m + 1)
                for j in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1]:
                        curr[j] = prev[j - 1] + 1
                    else:
                        curr[j] = max(prev[j], curr[j - 1])
                prev = curr
            return prev[m]
        
        n = len(s)
        rever = s[::-1]
        return n - longestPalin(s, rever)
