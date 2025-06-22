class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0,len(s),k):
            temp = s[i:i+k]
            if len(temp) == k:
                res.append(temp)
            else:
                temp += (k-len(temp))*fill
                res.append(temp)
        return res