class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word1 = s1.split()
        word2 = s2.split()
        mpp = {}
        for i in word1:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1
            
        for j in word2:
            if j in mpp:
                mpp[j] += 1
            else:
                mpp[j] = 1
        res = []
        for key,value in mpp.items():
            if value == 1:
                res.append(key)
        
        return res
