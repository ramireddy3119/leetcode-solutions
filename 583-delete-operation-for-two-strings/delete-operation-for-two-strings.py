class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        prev = [0]*(n+1) 
        for ind1 in range(1,m+1):
            curr = [0]*(n+1)
            for ind2 in range(1,n+1):
                if word1[ind1-1] == word2[ind2-1]:
                    curr[ind2] = 1 + prev[ind2-1]
                else:
                    curr[ind2]= max(prev[ind2],curr[ind2-1])
            prev = curr
        val = prev[n]
        return (m-val)+(n-val)
        