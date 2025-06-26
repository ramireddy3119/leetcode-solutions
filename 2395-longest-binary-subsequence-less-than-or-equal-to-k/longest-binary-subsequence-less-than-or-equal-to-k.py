class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        power = 0
        val = 0
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                val += 2**power
            if val <= k:
                count += 1
            else:
                break
            power += 1
        for j in range(i):
            if s[j] == '0':
                count += 1
        return count