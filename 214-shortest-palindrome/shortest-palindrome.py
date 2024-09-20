class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        original = s
        newStr = s + "#" + s[::-1]

        lps = [0]*(2*n+1)
        i = 0
        j = 1
        while j < len(newStr):
            if newStr[i] == newStr[j]:
                lps[j] = i+1
                i += 1
                j += 1
            
            elif j == len(newStr): break
            else:    
                if i > 0:
                    i = lps[i-1]
                else:
                    lps[j] = 0
                    j += 1
        
        diff = n - lps[-1]

        res = s[::-1][:diff] + original
        return res
        