class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        res = []
        n = len(code)
        if k > 0:
            for i in range(n):
                curr_sum = 0
                for j in range(i+1,i+k+1):
                    curr_sum += code[j%n]
                res.append(curr_sum)
        else:
            for i in range(n):
                curr_sum = 0
                for j in range(i-1, i+k-1, -1):
                    curr_sum += code[j % n]
                res.append(curr_sum)

        return res
