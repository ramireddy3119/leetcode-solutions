class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0]*len(code)
        # res = []
        # if k > 0:
        #     for i in range(n):
        #         curr_sum = 0
        #         for j in range(i+1,i+k+1):
        #             curr_sum += code[j%n]
        #         res.append(curr_sum)
        # else:
        #     for i in range(n):
        #         curr_sum = 0
        #         for j in range(i-1, i+k-1, -1):
        #             curr_sum += code[j % n]
        #         res.append(curr_sum)
        code += code
        prefix_sum = []
        curr_sum = 0
        for i in range(len(code)):
            curr_sum += code[i]
            prefix_sum.append(curr_sum)
        res = []
        if k >0:
            for i in range(n):
                res.append(prefix_sum[i+k]-prefix_sum[i])
        else:
            k = abs(k)
            for i in range(n,2*n):
                res.append(prefix_sum[i-1]-prefix_sum[i-k-1])    
        return res
